# Jupedsim Evacuation Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Jupedsim](https://img.shields.io/badge/Jupedsim-0.2.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)
![Last Commit](https://img.shields.io/github/last-commit/Kandil2001/Jupedsim-Evacuation-Analysis)
![Issues](https://img.shields.io/github/issues/Kandil2001/Jupedsim-Evacuation-Analysis)

**High-performance pedestrian evacuation simulation with parallel processing and Numba acceleration**

---

## Table of Contents

## Table of Contents

- [Overview](#overview)  
- [Theoretical Background](#theoretical-background)  
- [Real-World Applications](#real-world-applications)  
- [Ethical Considerations](#ethical-considerations)  
- [Features](#features)  
- [Quick Start](#quick-start)  
- [Installation](#installation)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)

---

## Overview

This project provides a robust and highly optimized framework for **pedestrian evacuation analysis** using the **JuPedSim** library. It leverages advanced techniques—parallel agent distribution, Numba-accelerated computations, smart caching, and efficient geometry handling—to simulate building evacuations in realistic scenarios. Designed for scalability, clarity, and speed, it is suitable for both research and practical safety analysis.


---

## Theoretical Background

Pedestrian dynamics is the study of how individuals and crowds move through space. It blends physics, behavioral psychology, and computational modeling to simulate realistic movement—especially in evacuation scenarios.

### 🔹 Social Force Model

This foundational model treats pedestrians as particles influenced by virtual forces:

- **Attractive forces** pull individuals toward goals (e.g., exits).
- **Repulsive forces** push them away from obstacles and other people.
- The combination of these forces governs movement patterns.

![Social Force Model](https://upload.wikimedia.org/wikipedia/commons/4/4e/Social_force_model_diagram.png)

In this diagram:
- Arrows represent directional forces acting on a pedestrian.
- The person adjusts their path based on nearby agents, walls, and their destination.

---

### 🔹 Bottleneck Behavior

When many agents attempt to pass through a narrow exit, congestion forms. This is known as **bottleneck behavior**, and it’s critical in evacuation planning.

![Bottleneck Evacuation](https://commons.wikimedia.org/wiki/File:Collective_crowd_patterns_Bottleneck_experiment_Participants_passing_through_a_bottleneck_during_a_simple_evacuation_situation_Moussa%C3%AFd_%26_al._2016_Figure1.jpg)

This image shows participants in a controlled evacuation experiment. Notice how density increases near the bottleneck, slowing overall flow.

---

### 🔹 Pedestrian Flow Heatmaps

Heatmaps visualize crowd density and movement intensity across a space. They’re used to identify high-traffic zones and optimize layouts.

![Pedestrian Flow Heatmap](https://www.isarsoft.com/_next/image?url=https%3A%2F%2Fisarsoft.com%2F_images%2Farticles%2Fheatmap-traffic-flow.png&w=1080&q=75)

In this example:
- Red zones indicate high pedestrian density.
- Blue zones show low activity.
- Architects and safety engineers use these maps to redesign space for smoother flow.

---

### 🔹 Microscopic vs. Macroscopic Models

- **Microscopic models** simulate each pedestrian individually, capturing detailed interactions.
- **Macroscopic models** treat crowds as continuous flows, similar to fluids—useful for large-scale analysis.

---

JuPedSim supports these modeling approaches and allows researchers to define building layouts, spawn zones, and exit strategies using XML and WKT formats. It’s widely used in safety engineering, urban planning, and evacuation research.


---

## Real-World Applications

- **Architecture**: Optimize exit placements and corridor widths  
- **Event Planning**: Ensure safe crowd dispersal in stadiums and venues  
- **Transportation Hubs**: Manage congestion in airports and stations  
- **Urban Design**: Analyze pedestrian flow in public spaces

---

## Ethical Considerations

- **Privacy**: Real-world data must be anonymized  
- **Inclusivity**: Account for diverse mobility needs  
- **Transparency**: Document assumptions and limitations

---

## Features

- Parallel agent distribution using `ThreadPoolExecutor`  
- Numba-accelerated distance calculations  
- Vectorized geometry operations  
- Real-time progress reporting  
- Optimized rendering and memory usage  
- Modular design for easy extension

---

## Quick Start
```bash
git clone https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git
cd Jupedsim-Evacuation-Analysis
pip install -r requirements.txt
```
Open `Ped1 - Copy.ipynb` in Jupyter and run all cells.

---

## Installation
```bash
pip install jupedsim pedpy shapely numpy matplotlib numba
```
```bash
conda install numpy matplotlib shapely
pip install jupedsim pedpy numba
```

---

## Project Structure
```
├── Ped1 - Copy.ipynb         # Main simulation notebook  
├── HC.wkt                    # Building geometry  
├── requirements.txt          # Dependencies  
├── README.md                 # Documentation  
├── data/                     # Input files  
├── docs/                     # Optional documentation  
├── figures/                  # Reserved for future visual assets  
├── *.sqlite                  # Output trajectory files (optional)
```
---

## Contributing

Pull requests are welcome. Please:

- Format code clearly  
- Document new features  
- Add tests or examples if possible

---

## License

MIT License. See `LICENSE` for details.
