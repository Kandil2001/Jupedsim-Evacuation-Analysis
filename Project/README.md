<p align="center">
  <a href="https://www.uni-wuppertal.de/en/">
    <img src="figures/buw_logo_official.svg" alt="University of Wuppertal Logo" width="220" style="margin-right: 40px;">
  </a>
  <a href="https://www.jupedsim.org/">
    <img src="https://www.jupedsim.org/stable/_static/jupedsim.svg" alt="JuPedSim Logo" width="160" style="margin-right: 40px;">
  </a>
  <a href="https://www.python.org/">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="200">
  </a>
</p>

# 🏫 HC Building Evacuation Analysis

**High-performance evacuation study of the HC building using JuPedSim and Python**  

This project implements and analyzes different evacuation scenarios for the HC building at **Bergische Universität Wuppertal**.  
It focuses on **scenario design, simulation setup, analysis, and recommendations**.

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Badge">
  </a>
  <a href="https://www.jupedsim.org/">
    <img src="https://img.shields.io/badge/JuPedSim-0.2.0-green.svg" alt="JuPedSim Badge">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License Badge">
  </a>
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/Contributions-Welcome-orange.svg" alt="Contributions Badge">
  </a>
</p>


## 📑 Table of Contents
- [Contents](#-contents)  
- [Objectives](#-objectives)  
- [Getting Started](#-getting-started)  
- [Baseline Simulation](#-baseline-simulation)  
- [Foyer Event (Exhibition) Scenario](#-foyer-event-exhibition-scenario)  
- [Fire in Cafeteria Scenario](#-fire-in-cafeteria-scenario)  
- [Evacuation Time Curve](#-evacuation-time-curve)  
- [Density Heatmap](#-density-heatmap)  
- [Scenario Animation](#-scenario-animation)  
- [Run Multiple Scenarios in Parallel](#-run-multiple-scenarios-in-parallel)  
- [Insights & Recommendations](#-insights--recommendations)  
- [Acknowledgments](#-acknowledgments)
- [Contributing](#-contributing)  
- [License](#-license) 


## Contents
- `Project_HC.pdf` → Project description & assignment statement  
- `HC.wkt` → Building floor plan in WKT format  
- `Ped1.ipynb` → Main Jupyter Notebook with simulations, analysis, and visualizations  
- `results/` → Generated plots, heatmaps, and animations  

## Objectives
The study aims to:
1. **Model the HC building ground floor** with JuPedSim.  
2. **Simulate evacuation scenarios**, including:
   - Baseline evacuation during normal lectures  
   - Foyer exhibitions with increased density  
   - Fire in the cafeteria with blocked exits  
3. **Analyze results**: evacuation times, congestion hotspots, and bottlenecks.  
4. **Provide recommendations** for safe event capacity and exit design.  

## Getting Started
### 1️⃣ Open the Notebook
```bash
jupyter notebook "Ped1.ipynb"
```
### 2️⃣ Run All Cells

The notebook will:
- Load the building geometry (`HC.wkt`)  
- Spawn agents according to the defined scenario  
- Run JuPedSim simulations  
- Generate results in `.sqlite` and visualization formats

## Baseline Simulation

```python
from jupedsim import Simulation

# 200 agents, normal lecture scenario
sim = Simulation(geometry="HC.wkt", agents=200)
sim.run()
sim.save("results/baseline.sqlite")
```

## Foyer Event (Exhibition) Scenario

```python
from jupedsim import Simulation

# Higher density due to foyer event
sim = Simulation("HC.wkt", agents=350)

# Define spawn zone in foyer
sim.set_spawn_zone("foyer", n_agents=150)

sim.run()
sim.save("results/foyer_event.sqlite")
```

## Fire in Cafeteria Scenario
```python
from jupedsim import Simulation

# 250 agents, cafeteria exit blocked
sim = Simulation("HC.wkt", agents=250)
sim.block_exit("cafeteria_exit")

sim.run()
sim.save("results/fire_cafeteria.sqlite")
```

## Evacuation Time Curve
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load trajectory data (after export)
df = pd.read_csv("results/baseline.csv")

# Compute evacuation times
evac_times = df.groupby("agent_id")["t"].max()

# Plot cumulative evacuation curve
plt.step(sorted(evac_times), range(len(evac_times)))
plt.xlabel("Time (s)")
plt.ylabel("Evacuated agents")
plt.title("Evacuation Curve - Baseline Scenario")
plt.show()
```

## Density Heatmap
```python
# Save pedestrian density heatmap
sim.plot_heatmap(output="results/heatmap_baseline.png")

# Or display inline (Jupyter)
sim.plot_heatmap()
```

## Scenario Animation
```python
# Export as GIF
sim.animate(output="results/baseline.gif", fps=15)

# Export as MP4
sim.animate(output="results/baseline.mp4", fps=30)
```
## Run Multiple Scenarios in Parallel
```python
from concurrent.futures import ThreadPoolExecutor
from jupedsim import Simulation

scenarios = [
    {"name": "baseline", "agents": 200},
    {"name": "foyer_event", "agents": 350},
    {"name": "fire_cafeteria", "agents": 250}
]

def run_scenario(cfg):
    sim = Simulation("HC.wkt", agents=cfg["agents"])
    if cfg["name"] == "fire_cafeteria":
        sim.block_exit("cafeteria_exit")
    sim.run()
    sim.save(f"results/{cfg['name']}.sqlite")

with ThreadPoolExecutor() as executor:
    executor.map(run_scenario, scenarios)
```

## Insights & Recommendations
- **Bottlenecks** appear at foyer and cafeteria exits under high load.  
- **Evacuation times** rise significantly during events and fires.  
- **Recommendation**:  
  - Limit maximum capacity during foyer exhibitions.  
  - Redesign exits or add alternative escape routes to improve flow.  
## Acknowledgments
- Project assignment: *Pedestrian Dynamics – Practical Project*  
- Supervisor: **Prof. Mohcine Chraibi**  
- Tools: **JuPedSim**, **Python (Numba, Matplotlib, Pandas)**  

## Contributing

We welcome contributions of all kinds — bug fixes, performance improvements, documentation updates, and new features.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines, coding standards, and workflow instructions before submitting a pull request.

## License
MIT License – see [LICENSE](LICENSE) for details.

