# Pedestrian Evacuation Analysis with JuPedSim

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen.svg" alt="Completed">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Simulation-JuPedSim-green.svg" alt="JuPedSim">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT License">
  <a href="https://kandil2001.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-kandil2001.github.io-2ea44f.svg" alt="Portfolio">
  </a>
</p>

A completed JuPedSim-based evacuation study for a university building layout.

The project explores how pedestrian placement, exit assignment, and scenario assumptions affect trajectories and total evacuation time. It is a simulation and analysis exercise, not a certified building-safety assessment or a globally optimized evacuation model.

<p align="center">
  <img src="figures/heatmap.gif" width="760" alt="Pedestrian evacuation simulation">
</p>

## Main features

- building geometry loaded from a WKT file
- nine manually defined exit areas
- configurable pedestrian spawn areas and group sizes
- scenario-specific exit assignments
- agent placement using JuPedSim distribution utilities
- SQLite trajectory output and notebook animation
- runtime and evacuation-time comparison between scenarios
- selected setup calculations using NumPy, Numba, and `ThreadPoolExecutor`

## Study setup

The building is represented as a walkable geometry with exit polygons placed around the available doors. Pedestrians are generated inside selected spawn areas and assigned to exits according to the active scenario.

Each scenario can change:

- active spawn areas
- group sizes
- available exits
- walking-speed parameters
- time-gap settings
- exit-assignment restrictions

This makes it possible to compare defined evacuation scenarios without rebuilding the complete setup.

## Simulation workflow

The workflow in `EvacuationAnalysis.ipynb`:

1. loads the building geometry from `HC.wkt`
2. defines exit and spawn polygons
3. generates valid initial pedestrian positions
4. assigns an exit to each pedestrian group
5. configures and runs the JuPedSim simulation
6. saves trajectories and calculates evacuation time
7. animates and compares the scenarios

The exit-assignment logic uses exit centroids together with scenario-specific restrictions. The geometrically nearest door is not always the most sensible route through the building, so the restrictions encode the assumptions of each scenario.

## Running the notebook

```bash
git clone https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git
cd Jupedsim-Evacuation-Analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook EvacuationAnalysis.ipynb
```

Package compatibility depends on the installed JuPedSim and PedPy versions. The current `requirements.txt` records the required packages but is not a locked environment file.

## Repository structure

```text
EvacuationAnalysis.ipynb   simulation and analysis workflow
HC.wkt                     building geometry
requirements.txt           Python dependencies
figures/                   selected animation used in the README
```

## Scope and limitations

This completed repository is an educational pedestrian-dynamics study.

Its documented scope is:

- one building geometry
- manually defined exits and spawn areas
- scenario-based exit restrictions
- centroid-informed assignment logic
- trajectory and evacuation-time comparison
- no experimental calibration

The project does **not** calculate a globally optimal path through the complete geometry. It also does not establish regulatory compliance, crowd safety certification, or experimentally validated evacuation predictions.

Possible follow-up research includes path-based exit assignment, sensitivity analysis, additional layouts, repeated stochastic runs, and validation against measured pedestrian-flow data.

## Acknowledgments

This project was developed for the Pedestrian Dynamics course at Bergische Universität Wuppertal.

Thanks to **Mohcine Chraibi** for supervision and guidance, and to the JuPedSim development team for the simulation framework.

## Author

Ahmed Kandil — [Portfolio](https://kandil2001.github.io/) · [LinkedIn](https://www.linkedin.com/in/ahmed-kandil03/) · [ORCID](https://orcid.org/0009-0007-2724-4565)

Released under the [MIT License](LICENSE).
