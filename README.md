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

- Overview  
- Theoretical Background  
- Real-World Applications  
- Ethical Considerations  
- Features  
- Quick Start  
- Installation  
- Project Structure  
- Contributing  
- License

---

## Overview

This project provides a robust and highly optimized framework for **pedestrian evacuation analysis** using the **JuPedSim** library. It leverages advanced techniques—parallel agent distribution, Numba-accelerated computations, smart caching, and efficient geometry handling—to simulate building evacuations in realistic scenarios. Designed for scalability, clarity, and speed, it is suitable for both research and practical safety analysis.


---

## Theoretical Background

Pedestrian dynamics is a multidisciplinary field combining physics, behavioral science, and computational modeling. Key concepts include:

- **Social Force Model**: Pedestrians are influenced by forces—toward exits, away from obstacles, and from other agents.  
  ![Social Force Model](https://upload.wikimedia.org/wikipedia/commons/4/4e/Social_force_model_diagram.png)

- **Microscopic vs. Macroscopic Models**:  
  - *Microscopic*: Simulates each pedestrian individually  
  - *Macroscopic*: Treats crowds as fluid-like entities

- **Bottleneck Behavior**:  
  ![Bottleneck Simulation](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bottleneck_simulation.png)  
  Narrow exits cause congestion and delay; modeling helps optimize layouts.

- **Density & Flow Rate**:  
  ![Crowd Density Heatmap](https://upload.wikimedia.org/wikipedia/commons/7/7f/Crowd_density_heatmap.png)  
  These metrics are critical for evaluating evacuation performance.

JuPedSim is an open-source framework enabling detailed pedestrian simulations using XML-based scenario definitions. It supports routing algorithms, geometry configurations, and agent behaviors.

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

├── Ped1 - Copy.ipynb         # Main simulation notebook  
├── HC.wkt                    # Building geometry  
├── requirements.txt          # Dependencies  
├── README.md                 # Documentation  
├── data/                     # Input files  
├── docs/                     # Optional documentation  
├── figures/                  # Reserved for future visual assets  
├── *.sqlite                  # Output trajectory files (optional)

---

## Contributing

Pull requests are welcome. Please:

- Format code clearly  
- Document new features  
- Add tests or examples if possible

---

## License

MIT License. See `LICENSE` for details.
