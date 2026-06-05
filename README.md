# Pedestrian Evacuation Analysis with JuPedSim

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Simulation-JuPedSim-green.svg" alt="JuPedSim">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
  <a href="https://kandil2001.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-kandil2001.github.io-2ea44f.svg" alt="Portfolio">
  </a>
</p>

This repository contains my JuPedSim-based evacuation study for a university building layout. I built it to explore how pedestrian placement, exit selection, and scenario assumptions affect evacuation behaviour and total evacuation time.

The notebook defines the walkable geometry, creates pedestrian groups, assigns exits, runs the simulation, and reviews the resulting trajectories.

<p align="center">
  <img src="figures/heatmap.gif" width="760" alt="Pedestrian evacuation simulation">
</p>

## Main features

- Building geometry loaded from a WKT file
- Nine manually defined exit areas
- Configurable pedestrian spawn areas and group sizes
- Scenario-specific exit assignments
- Agent placement using JuPedSim distribution utilities
- SQLite trajectory output and notebook animation
- Runtime and evacuation-time comparison between scenarios
- Selected setup calculations using NumPy, Numba, and `ThreadPoolExecutor`

## Study setup

The building is represented as a walkable geometry, with exit polygons placed around the available doors. Pedestrians are generated inside selected spawn areas and assigned to exits according to the active scenario.

Each scenario can change the active spawn areas, group sizes, available exits, walking-speed parameters, and time-gap settings. This makes it possible to compare evacuation strategies without rebuilding the complete setup.

## How the simulation works

The workflow in `EvacuationAnalysis.ipynb` follows these steps:

1. Load the building geometry from `HC.wkt`.
2. Define exit and spawn polygons.
3. Generate valid initial pedestrian positions.
4. Select an exit for each pedestrian group.
5. Configure and run the JuPedSim simulation.
6. Save the trajectories and calculate the evacuation time.
7. Animate and compare the scenarios.

The exit-selection logic uses exit centroids and scenario-specific restrictions. The restrictions are needed because the geometrically nearest door is not always the most sensible route through the building.

## Running the notebook

```bash
git clone https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git
cd Jupedsim-Evacuation-Analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook EvacuationAnalysis.ipynb
```

Package compatibility may depend on the installed JuPedSim version.

## Repository structure

```text
EvacuationAnalysis.ipynb   simulation and analysis workflow
HC.wkt                     building geometry
requirements.txt           Python dependencies
figures/                   selected animation used in the README
```

## Notes and limitations

This is an educational pedestrian-dynamics study, not a certified evacuation or building-safety model.

The current version focuses on one building geometry with manually defined exits, spawn areas, and scenario assumptions. Exit selection is based partly on centroid distance and does not calculate a globally optimal route through the complete geometry. The simulation has also not been calibrated against experimental evacuation data.

Useful next steps include path-based exit selection, systematic sensitivity studies, additional building layouts, and validation against measured pedestrian-flow data.

## Acknowledgments

This project was developed for the Pedestrian Dynamics course at Bergische Universität Wuppertal.

Thanks to **Mohcine Chraibi** for his supervision and guidance, and to the JuPedSim development team for providing the simulation framework.

## Author

Ahmed Kandil — [Portfolio](https://kandil2001.github.io/) · [GitHub](https://github.com/Kandil2001) · [LinkedIn](https://www.linkedin.com/in/ahmed-kandil03/)

Released under the [MIT License](LICENSE).
