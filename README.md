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

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Performance Benchmarks](#performance-benchmarks)
- [Visualization](#visualization)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Overview

This project provides a robust and highly optimized framework for **pedestrian evacuation analysis** using the **JuPedSim** library. It leverages advanced techniques—parallel agent distribution, Numba-accelerated computations, smart caching, and efficient visualization—to simulate building evacuations in realistic scenarios. Designed for scalability, clarity, and speed, it is suitable for both research and practical safety analysis.

---

## Features

- 🚀 **Parallel Agent Distribution**: Agents are distributed across spawn areas using `ThreadPoolExecutor` for fast, multi-core setup.
- 💨 **Numba-Accelerated Calculations**: Critical functions (e.g., nearest exit lookup) are compiled to machine code using Numba for speed.
- 🧠 **Smart Caching**: Building geometry is loaded with `lru_cache`, minimizing disk I/O.
- 📊 **Efficient Data Handling**: NumPy vectorized operations accelerate distance calculations and geometry manipulations.
- 🖼️ **Optimized Visualization**: Fast plotting with NumPy and Matplotlib for both setup and evacuation animation.
- 📝 **Progress Reporting**: Live simulation progress updates for long runs.
- 🏃 **Batch Agent Addition**: Agents are added per spawn area batch for scalable performance.
- 🔄 **Scenario Flexibility**: Easily configure spawn/exit assignments, motivation factors, and speed distributions.

---

## Quick Start

1. **Clone the repository**
    ```bash
    git clone https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git
    cd Jupedsim-Evacuation-Analysis
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    # Or install individually if needed:
    pip install jupedsim pedpy shapely numpy matplotlib numba
    ```

3. **Run the simulation**
    - Open the `Ped1 - Copy.ipynb` Jupyter notebook.
    - Run all cells to execute the evacuation simulation from setup to animation.

---

## Installation

### Prerequisites

- Python 3.8+
- Jupyter Notebook

### Dependencies

Install required libraries with pip:

```bash
pip install jupedsim pedpy shapely numpy matplotlib numba
```

If you use conda/miniconda, you may prefer:

```bash
conda install numpy matplotlib shapely
pip install jupedsim pedpy numba
```

---

## Usage

### Running in Jupyter

- Open `Ped1 - Copy.ipynb` in Jupyter.
- Each cell is documented and walks through:
    - Importing libraries
    - Loading building geometry (`HC.wkt`)
    - Defining exits and spawn areas
    - Parallel agent distribution and exit assignment
    - Batch agent addition and scenario configuration
    - Visualization of setup and evacuation
    - Simulation loop and progress reporting
    - Animation and summary results

### Custom Scenario Configuration

Change the scenarios in the notebook to adjust:
- **active_spawns:** Which spawn areas are active
- **exit_assignments:** Manual assignment of exits to spawn areas
- **T_motivation:** Motivation factor for agent movement
- **speed_mean / speed_std:** Walking speed statistics

---

## Configuration

### Scenario Parameters

Each scenario can be configured with:
- `active_spawns`: List of booleans indicating which spawn areas to use
- `exit_assignments`: List (per spawn) of exit indices or custom exit assignments
- `T_motivation`: Motivation factor for movement
- `speed_mean`: Mean walking speed (m/s)
- `speed_std`: Standard deviation of walking speed

### Building Geometry

- Geometry is loaded from WKT file (`HC.wkt`)
- Exits and spawn areas are shaped as polygons, and agent distributions are controlled per area

---

## Performance Benchmarks

- Agent distribution and exit assignment are parallelized—setup is fast even for hundreds/thousands of agents.
- Numba-accelerated functions (e.g., nearest exit lookup) are orders of magnitude faster than pure Python.
- Smart caching and batch operations minimize memory footprint and maximize speed.

---

## Visualization

- Initial configuration plot: Shows walkable area, exits, spawns, and agent positions.
- Animated evacuation: Simulation trajectory is read from SQLite and animated with live progress reporting.

---

## Project Structure

```
├── Ped1 - Copy.ipynb         # Jupyter notebook: main simulation code
├── HC.wkt                    # Building geometry (WKT format)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── *.sqlite                  # Output trajectory files per scenario
├── data/                     # Additional data files (if any)
├── docs/                     # Documentation (optional)
```

---

## Contributing

Contributions are welcome!
- Fork the repository and submit a pull request.
- Please format code clearly and document any new features or bug fixes.
- Add tests or example notebooks for new functionality.

---

## FAQ

**Q:** How do I add new exits or spawn areas?
**A:** Edit the respective polygons in the notebook cells and update the scenario configuration.

**Q:** Can I use different algorithms for agent distribution?
**A:** Yes, replace the distribution function or update parameters as needed.

**Q:** How can I export results for further analysis?
**A:** Trajectories are saved to SQLite files; use pandas or custom scripts to extract metrics.

**Q:** How to handle large simulations?
**A:** The framework is optimized for scalability. Increase batch sizes or parallelism if needed, and monitor memory usage.

---

## Citation

If you use this software for academic research, please cite:

```
@software{Kandil_Jupedsim_Evac_2024,
  author = {Kandil, Mohamed},
  title = {Jupedsim Evacuation Analysis},
  year = {2024},
  url = {https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis}
}
```

---

## Acknowledgments

- JuPedSim team for the core simulation library
- NumFOCUS and open-source contributors for supporting scientific Python
- All contributors to this project

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
