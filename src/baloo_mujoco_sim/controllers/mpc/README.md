# Baloo MPPI Controller

This directory contains the Model Predictive Path Integral (MPPI) controller implementations for the Baloo dual-arm soft robot:

- [`mpc_controller.py`](file:///home/radlab/baloo-ws/baloo-mujoco-sim/src/baloo_mujoco_sim/controllers/mpc/mpc_controller.py): The main MPPI controller using Latin Hypercube Sampling (LHS) boxes and parallelized MuJoCo rollouts with multiprocessing.
- [`mpc_controller_optuna.py`](file:///home/radlab/baloo-ws/baloo-mujoco-sim/src/baloo_mujoco_sim/controllers/mpc/mpc_controller_optuna.py): Optuna hyperparameter optimization script for tuning MPPI weights.

## In-Depth Mathematical & Tuning Guide

For the full theoretical derivations, variable definitions, cost-reward duality explanations, comparisons between RL and MPPI, and analysis of departures from classical MPPI (Williams et al.), see the comprehensive documentation:

👉 **[MPPI & RL Theoretical Formulations, Cost Duality & Tuning Guide](../../../../docs/mppi_guide.html)**
