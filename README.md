<p align="center">
  <a href="https://www.uni-wuppertal.de/en/">
    <img src="https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis/blob/main/figures/philunet_case_logo_bergische_universitaet_wuppertal.jpg" alt="Bergische Universität Wuppertal Logo" width="220" style="margin-right: 40px;">
  </a>
  <a href="https://www.jupedsim.org/">
    <img src="https://www.jupedsim.org/stable/_static/jupedsim.svg" alt="JuPedSim Logo" width="160" style="margin-right: 40px;">
  </a>
  <a href="https://www.python.org/">
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="200">
  </a>
</p>

# **Jupedsim Evacuation Analysis**
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

## 🚨 High-performance pedestrian evacuation simulation with parallel processing & Numba acceleration
<p align="center">
  <img src="figures/demo.gif" width="700" alt="Evacuation Simulation Demo">
</p>

## 📑 Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Quick Start](#quick-start)
- [Theoretical Background](#theoretical-background)  
- [Input & Output Formats](#input--output-formats)  
- [Real-World Applications](#real-world-applications)  
- [Ethical Considerations](#ethical-considerations)  
- [Roadmap](#roadmap)  
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)  
- [Contributing](#contributing)  
- [License](#license)

## Overview
This project delivers a **scalable, realistic, and lightning-fast** framework for simulating building evacuations using **JuPedSim**.  
It combines **parallel agent distribution**, **Numba-accelerated computations**, and **efficient geometry handling** for advanced crowd analysis.  

Designed for:
- **Researchers** studying pedestrian dynamics
- **Safety engineers** optimizing evacuation plans
- **Urban planners** improving public space layouts

## Features
🚀 **High Performance** – Parallel simulation with `ThreadPoolExecutor`  
🔥 **Numba Acceleration** – JIT speed-ups for heavy math  
🗺 **Flexible Geometry** – Import `.wkt` or XML building layouts  
📊 **Detailed Analytics** – Density heatmaps, bottleneck detection, evacuation times  
🎯 **Customizable Agents** – Adjustable speeds, behaviors, and spawn zones  
📈 **Visual Outputs** – Real-time plots & post-simulation analysis

<p align="center">
  <img src="figures/heatmap.gif" width="550" alt="Pedestrian Density Heatmap">
</p>

## Quick Start

```bash
git clone https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git
cd Jupedsim-Evacuation-Analysis
pip install -r requirements.txt
```

### Run in Jupyter Notebook

```bash
jupyter notebook "Ped1 - Copy.ipynb"
```

### Or run a Python script directly

```python
from jupedsim import Simulation
sim = Simulation(geometry="HC.wkt", agents=200)
sim.run()
sim.plot_heatmap()
```

## Theoretical Background

### 🔹 Social Force Model
Pedestrians are modeled as particles influenced by **attractive forces** (towards exits) and **repulsive forces** (from obstacles and others).
This model is a cornerstone of microscopic pedestrian dynamics simulations. For a detailed description of the model, refer to the resources at [https://pedestriandynamics.org/models/](https://pedestriandynamics.org/models/).

<p align="center">
  <img src="figures/social_force_model.png" width="500" alt="Social Force Model">
</p>
---

### 🔹 Bottleneck Behavior
When many agents attempt to pass through a narrow exit, congestion forms, reducing flow efficiency.

<p align="center">
  <img src="figures/bottleneck_example.png" width="500" alt="Bottleneck Behavior">
</p>
---

### 🔹 Pedestrian Flow Heatmaps
Heatmaps visualize crowd density and movement intensity to identify congestion hotspots.

<p align="center">
  <img src="figures/pedestrian_heatmap.png" width="500" alt="Pedestrian Flow Heatmap">
</p>
---

### 🔹 Microscopic vs. Macroscopic Models
- **Microscopic**: Simulates each pedestrian individually (detailed interactions).  
- **Macroscopic**: Treats crowds as continuous flows (good for large-scale analysis).  

JuPedSim primarily uses **WKT** geometry definitions for simulation.

Tested on: **Intel i7-11800H, 16GB RAM, Python 3.10**

## Real-World Applications
🏟 **Event planning** – Stadium crowd dispersal  
🏢 **Architecture** – Optimizing exit placements  
🚉 **Transport hubs** – Reducing congestion  
🏙 **Urban design** – Public space flow analysis

## Ethical Considerations
- **Privacy**: Real-world data must be anonymized  
- **Inclusivity**: Account for individuals with varied mobility needs  
- **Transparency**: Document assumptions and limitations of the model

## Roadmap
- [x] Parallel agent simulation
- [x] Heatmap visualizations
- [ ] Adaptive route choice AI

## Troubleshooting
**Q:** Simulation runs slowly  
**A:** Ensure Numba is enabled, use Python ≥3.9, and reduce visualization frequency.

**Q:** How do I change exits?  
**A:** Edit the `.wkt` file to define new exit polygons.

**Q:** Output file is empty  
**A:** Check that spawn zones and exits are correctly defined in geometry.

## Acknowledgments
This project was developed as a practical assignment for the **Pedestrian Dynamics** course at the **Bergische Universität Wuppertal**. We extend our gratitude to:

* **Mohcine Chraibi** for supervision and guidance. His personal page is available at [https://www.chraibi.de/](https://www.chraibi.de/).
* The **JuPedSim** development team for providing the powerful simulation framework. More information is available on the official website: [https://www.jupedsim.org/stable/](https://www.jupedsim.org/stable/).
* The **Python** community for the essential tools and libraries (Numba, Matplotlib, etc.) that made high-performance analysis possible.
## Contributing

We welcome contributions of all kinds — bug fixes, performance improvements, documentation updates, and new features.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines, coding standards, and workflow instructions before submitting a pull request.

## License
MIT License – see [LICENSE](LICENSE) for details.
