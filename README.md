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

This project implements a highly optimized pedestrian evacuation simulation using Jupedsim with advanced performance enhancements including parallel processing, numba acceleration, and vectorized operations. The simulation models complex evacuation scenarios with thousands of agents while maintaining computational efficiency.

## Features

- **Parallel agent distribution** using ThreadPoolExecutor
- **Numba-accelerated distance calculations** for nearest exit computation
- **Vectorized operations** for efficient geometric calculations
- **Caching mechanism** for geometry loading
- **Memory-efficient position processing**
- **Optimized visualization** with reduced rendering overhead
- **Progress reporting** during simulation execution
- **Batch agent addition** for improved performance

## Quick Start

1. **Clone the repository**
2. **Install dependencies**
3. **Run the simulation**
4. **Execute all cells** to see the evacuation simulation in action!

## Installation

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
