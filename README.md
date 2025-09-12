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
- [Scenario Results](#scenario-results)
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

## Scenario Results

Below you can find ready-to-edit sections for **all six scenarios**.  
Each section includes:

- The scenario config (copy-paste from the notebook)
- A code snippet illustrating how to run it
- Space for adding images, figures, and results

---

### Scenario 1

**Configuration:**
```python
scenarios["Scenario 1"] = {
    "active_spawns": [False, True, False, False, False, False],
    "exit_assignments": [None, [3], None, None, None, None],
    "T_motivation": 5,
    "speed_mean": 1.2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 1", scenarios["Scenario 1"])
```

**Insert your figure(s) below:**  
*(Paste image, plot, or animation here)*

![Scenario 1 Figure](./figures/scenario1.png) <!-- Replace with your plot -->

**Insert results/numbers below:**  
*(Paste evacuation time, agent stats, etc.)*

---

### Scenario 2

**Configuration:**
```python
scenarios["Scenario 2"] = {
    "active_spawns": [False, True, False, False, False, False],
    "exit_assignments": [None, [0], None, None, None, None],
    "T_motivation": 5,
    "speed_mean": 1.2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 2", scenarios["Scenario 2"])
```

**Insert your figure(s) below:**  
*(Paste image, plot, or animation here)*

![Scenario 2 Figure](./figures/scenario2.png)

**Insert results/numbers below:**  
*(Paste evacuation time, agent stats, etc.)*

---

### Scenario 3

**Configuration:**
```python
scenarios["Scenario 3"] = {
    "active_spawns": [True, False, True, True, True, True],
    "exit_assignments": [None, None, [3], [0, 1], [4, 5, 6, 7], [4, 5, 6, 7]],
    "T_motivation": 5,
    "speed_mean": 1.2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 3", scenarios["Scenario 3"])
```

**Insert your figure(s) below:**  
![Scenario 3 Figure](./figures/scenario3.png)

**Insert results/numbers below:**

---

### Scenario 4

**Configuration:**
```python
scenarios["Scenario 4"] = {
    "active_spawns": [False, False, True, True, True, True],
    "exit_assignments": [None, None, [3], [0, 1], [4, 5, 6, 7], [4, 5, 6, 7]],
    "T_motivation": 5,
    "speed_mean": 1.2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 4", scenarios["Scenario 4"])
```

**Insert your figure(s) below:**  
![Scenario 4 Figure](./figures/scenario4.png)

**Insert results/numbers below:**

---

### Scenario 5

**Configuration:**
```python
scenarios["Scenario 5"] = {
    "active_spawns": [True, True, True, True, True, True],
    "exit_assignments": None,
    "T_motivation": 5,
    "speed_mean": 1.2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 5", scenarios["Scenario 5"])
```

**Insert your figure(s) below:**  
![Scenario 5 Figure](./figures/scenario5.png)

**Insert results/numbers below:**

---

### Scenario 6

**Configuration:**
```python
scenarios["Scenario 6"] = {
    "active_spawns": [True, True, True, True, True, True],
    "exit_assignments": None,
    "T_motivation": 5,
    "speed_mean": 2,
    "speed_std": 0.05,
}
```

**How to run:**
```python
evacuation_time, sim_time = run_simulation_optimized("Scenario 6", scenarios["Scenario 6"])
```

**Insert your figure(s) below:**  
![Scenario 6 Figure](./figures/scenario6.png)

**Insert results/numbers below:**

---

## Usage

See the [Scenario Results](#scenario-results) section above for step-by-step scenario execution and blank slots for your outputs.

---

## Configuration

*(...the rest of your README content remains here as in the previous version)*

---

## License

MIT License
