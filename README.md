# Jupedsim Evacuation Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Jupedsim](https://img.shields.io/badge/Jupedsim-0.2.0-green.svg)
![Optimized](https://img.shields.io/badge/Optimized-Performance-orange.svg)

**High-performance pedestrian evacuation simulation with parallel processing and numba acceleration**

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Optimization Techniques](#optimization-techniques)
- [Project Structure](#project-structure)
- [Simulation Scenarios](#simulation-scenarios)
- [Results](#results)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## 📖 Overview

This project implements a highly optimized pedestrian evacuation simulation using Jupedsim with advanced performance enhancements including parallel processing, numba acceleration, and vectorized operations. The simulation models complex evacuation scenarios with thousands of agents while maintaining computational efficiency.

## ✨ Features

- **Parallel agent distribution** using ThreadPoolExecutor
- **Numba-accelerated distance calculations** for nearest exit computation
- **Vectorized operations** for efficient geometric calculations
- **Caching mechanism** for geometry loading
- **Memory-efficient position processing**
- **Optimized visualization** with reduced rendering overhead
- **Progress reporting** during simulation execution
- **Batch agent addition** for improved performance

## 🛠 Installation

### Prerequisites
- Python 3.8+
- Jupyter Notebook

### Dependencies

```bash
pip install shapely pathlib matplotlib jupedsim pedpy numpy numba
