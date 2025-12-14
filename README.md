# MarketRiskSentinel 🛡️

**High-Performance Hybrid Risk Engine (C/Python)**

## 🚀 Overview
MarketRiskSentinel is a financial analytics library designed to bridge the gap between Python's flexibility and C's raw speed. It implements standard risk metrics (**Parametric VaR**) and prepares the foundation for large-scale Monte Carlo simulations using **contiguous memory allocation**.

## 🏗️ Architecture
The system follows a dual-layer architecture to optimize the **Critical Execution Path**:
1.  **Python Layer (API):** Handles data ingestion, OOP modeling, and orchestration using Abstract Base Classes.
2.  **C Kernel (Compute):** Manages heavy computation and manual memory allocation (`malloc`) to optimize **CPU Cache Locality**.

## 🛠️ Tech Stack
- **Core:** C (GCC) for memory management and performance loops.
- **Analytics:** Python 3.9+, NumPy, SciPy.
- **Design:** Object-Oriented Programming (OOP), Factory Pattern.

## 📂 Structure
- `src/c_core/`: Low-level kernels using direct heap allocation.
- `src/python/`: Risk models and statistical engines.

## 🔧 Build & Run
```bash
# Compile the C Kernel
gcc src/c_core/risk_engine.c -o risk_engine

# Run the memory simulation
'./risk_engine'
```

Developed by Duarte Abraços as part of a research initiative into High-Frequency Risk Systems.