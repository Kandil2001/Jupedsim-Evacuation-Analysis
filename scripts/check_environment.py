from __future__ import annotations

import json
import math
import tempfile
from importlib.metadata import version
from pathlib import Path

import jupedsim as jps
import matplotlib
import numba
import numpy as np
import pedpy
import plotly
import shapely
from jupedsim.internal.notebook_utils import animate, read_sqlite_file  # noqa: F401
from shapely.geometry import Polygon


EXPECTED_VERSIONS = {
    "jupyter": "1.1.1",
    "jupedsim": "1.4.2",
    "matplotlib": "3.11.1",
    "numba": "0.66.0",
    "numpy": "2.4.6",
    "pedpy": "1.5.0",
    "plotly": "6.9.0",
    "shapely": "2.1.2",
}


def check_versions() -> None:
    mismatches: list[str] = []
    for package, expected in EXPECTED_VERSIONS.items():
        installed = version(package)
        if installed != expected:
            mismatches.append(f"{package}: expected {expected}, installed {installed}")

    if mismatches:
        raise SystemExit("Version mismatch:\n- " + "\n- ".join(mismatches))


def check_notebook_metadata() -> None:
    notebook = json.loads(Path("EvacuationAnalysis.ipynb").read_text(encoding="utf-8"))
    python_version = notebook["metadata"]["language_info"]["version"]
    if python_version != "3.12.8":
        raise SystemExit(f"Unexpected notebook Python version: {python_version}")


def check_numba() -> None:
    @numba.njit
    def squared_distance(a: np.ndarray, b: np.ndarray) -> float:
        delta = a - b
        return float(np.dot(delta, delta))

    value = squared_distance(np.array([1.0, 2.0]), np.array([4.0, 6.0]))
    if not math.isclose(value, 25.0):
        raise SystemExit(f"Unexpected Numba result: {value}")


def check_jupedsim_api() -> None:
    geometry = Polygon([(0.0, 0.0), (10.0, 0.0), (10.0, 5.0), (0.0, 5.0)])
    walkable_area = pedpy.WalkableArea(geometry)
    if walkable_area.polygon.area <= 0.0:
        raise SystemExit("PedPy walkable area is invalid.")

    spawn = Polygon([(1.0, 2.0), (2.0, 2.0), (2.0, 3.0), (1.0, 3.0)])
    positions = jps.distribute_by_number(
        polygon=spawn,
        number_of_agents=1,
        distance_to_agents=0.2,
        distance_to_polygon=0.2,
        seed=1,
    )
    if len(positions) != 1:
        raise SystemExit(f"Expected one generated position, received {len(positions)}")

    exit_area = Polygon([(9.0, 2.0), (10.0, 2.0), (10.0, 3.0), (9.0, 3.0)])

    with tempfile.TemporaryDirectory() as temporary_directory:
        trajectory_file = Path(temporary_directory) / "smoke.sqlite"
        writer = jps.SqliteTrajectoryWriter(output_file=trajectory_file)
        simulation = jps.Simulation(
            model=jps.CollisionFreeSpeedModel(),
            geometry=geometry,
            trajectory_writer=writer,
        )
        exit_id = simulation.add_exit_stage(exit_area)
        journey_id = simulation.add_journey(jps.JourneyDescription([exit_id]))
        simulation.add_agent(
            jps.CollisionFreeSpeedModelAgentParameters(
                journey_id=journey_id,
                stage_id=exit_id,
                position=positions[0],
                time_gap=1.0,
                desired_speed=1.2,
            )
        )

        for _ in range(5):
            simulation.iterate()

        writer.close()
        if simulation.delta_time() <= 0.0:
            raise SystemExit("JuPedSim returned an invalid time step.")
        if not trajectory_file.is_file() or trajectory_file.stat().st_size == 0:
            raise SystemExit("JuPedSim did not create a trajectory database.")


def main() -> None:
    matplotlib.use("Agg")
    _ = plotly.__version__
    check_versions()
    check_notebook_metadata()
    check_numba()
    check_jupedsim_api()
    print("Pinned Python environment and JuPedSim notebook APIs are compatible.")


if __name__ == "__main__":
    main()
