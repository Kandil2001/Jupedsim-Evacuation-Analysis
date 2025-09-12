<div style="border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 8px;">

# Jupedsim Evacuation Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Jupedsim](https://img.shields.io/badge/Jupedsim-0.2.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)
![Last Commit](https://img.shields.io/github/last-commit/Kandil2001/Jupedsim-Evacuation-Analysis)
![Issues](https://img.shields.io/github/issues/Kandil2001/Jupedsim-Evacuation-Analysis)

**High-performance pedestrian evacuation simulation with parallel processing and numba acceleration**

[Quick Start](#quick-start) • [Features](#features) • [Usage](#usage) • [Examples](#examples)

</div>

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

## Overview

This project provides a robust and highly optimized framework for **pedestrian evacuation analysis** using the **Jupedsim** library. By leveraging advanced performance techniques like **parallel processing** with `ThreadPoolExecutor`, **Numba acceleration**, and **vectorized operations**, the simulation can efficiently model complex evacuation scenarios involving thousands of agents. The codebase is designed for both researchers and practitioners who need to analyze human behavior in emergency situations without being limited by computational constraints.

## Features

This project includes several key optimizations to ensure high-performance simulation:

* 🚀 **Parallel Agent Distribution**: Utilizes `ThreadPoolExecutor` to distribute agent spawning across multiple CPU cores, dramatically reducing setup time for large-scale simulations.
* 💨 **Numba-Accelerated Calculations**: Compiles critical functions, such as finding the nearest exit, to machine code using **Numba**, resulting in significant speed improvements.
* 🧠 **Smart Caching**: Implements an `lru_cache` for geometry files, ensuring the building layout is loaded from disk only once, even if called multiple times.
* 📊 **Efficient Data Handling**: Uses **vectorized NumPy operations** for fast, memory-efficient distance calculations and geometric manipulations.
* 🖼️ **Optimized Visualization**: Includes a streamlined plotting function that uses NumPy arrays to reduce rendering overhead and efficiently visualize the simulation setup.
* 📝 **Progress Reporting**: Provides real-time updates on simulation progress, which is particularly useful for long-running scenarios.
* 🏃 **Batch Agent Addition**: Agents are added in batches per spawn area to enhance the efficiency of the simulation setup.

## Quick Start

Get started with the simulation in just a few steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git](https://github.com/Kandil2001/Jupedsim-Evacuation-Analysis.git)
    cd Jupedsim-Evacuation-Analysis
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the simulation:**
    Open the `Ped1 ` Jupyter Notebook.
4.  **Execute all cells** to see the evacuation simulation in action, from setup to final animation.

## Installation

### Prerequisites

* Python 3.8+
* Jupyter Notebook

### Dependencies

Install the required packages using pip:

```bash
pip install jupedsim pedpy shapely numpy matplotlib numba
```

### Prerequisites
- Python 3.8+
- Jupyter Notebook

### Dependencies

Install the required dependencies using the package manager of your choice.

## Usage

### Basic Simulation

Load geometry and define areas, then run a specific scenario with your configuration.

### Custom Scenario Configuration

Create custom scenarios with different parameters including active spawns, exit assignments, motivation factors, and speed settings.

## Configuration

### Scenario Parameters

Each scenario can be configured with these parameters:

- active_spawns: List of booleans indicating which spawn areas to use
- exit_assignments: Custom exit assignments for each spawn area
- T_motivation: Motivation factor affecting agent movement
- speed_mean: Mean walking speed of agents (m/s)
- speed_std: Standard deviation of walking speeds

### Building Geometry

The simulation uses WKT format for building geometry with multiple exit points and spawn areas with different agent distributions.

## Performance Benchmarks

The implementation includes several optimizations that significantly improve performance with detailed metrics on speed improvements and memory reduction.

## Visualization

The framework includes comprehensive visualization capabilities for simulation setup, evacuation animation, and results analysis.

## Project Structure

The project is organized with directories for data, notebooks, documentation, and configuration files.

## Contributing

We welcome contributions to enhance this evacuation simulation framework with guidelines on how to contribute, development setup, and testing procedures.

## FAQ

Common questions about adding exit points, using different distribution algorithms, handling large simulations, and exporting results.

## Citation

Citation information for academic use of this software.

## Acknowledgments

Acknowledgments to the JuPedSim team, NumFOCUS community, and open source contributors.

## License

This project is licensed under the MIT License.
