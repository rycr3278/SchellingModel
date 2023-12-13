# Schelling's Model of Segregation Simulation

## Overview
This Python simulation is a simplified representation of Schelling's Model of Segregation. The model demonstrates how individual preferences in residential choices can lead to widespread segregation, even when those preferences are not extreme. Developed by Thomas Schelling in the 1970s, this model is a classic example in the study of how small personal biases can lead to significant societal impacts.

## Model Description
In our simulation, the 'world' consists of two types of agents: Winter Sports Fans and Summer Sports Fans. These agents prefer to live in neighborhoods where there are at least some neighbors with similar interests. The world is represented as a 10x10 grid where each cell can either be empty (vacant) or occupied by one of the two types of agents.

## Scenarios
The simulation includes three different scenarios to model various levels of neighbor preference:

1. **Scenario 1**: Each home must have less than 4 neighbors of the same type.
2. **Scenario 2**: Each home must have between 1 and 4 neighbors of the same type.
3. **Scenario 3**: Adapted for fans of both Winter and Summer sports, with similar neighbor preferences as Scenario 2.

## Simulation Process
- The grid is initialized with an equal number of both types of sports fans, with some homes left vacant.
- The simulation then iteratively moves agents (sports fans) to vacant homes if their neighborhood preference is not satisfied.
- The process repeats until a stable state is achieved where all agents meet their neighborhood preferences or when a maximum number of iterations is reached.

## Visualization
The simulation results are visualized using `matplotlib`, showing the grid before and after the segregation process. Different colors in the grid represent different types of agents, and vacant homes. A legend is provided to help interpret the grid colors.

## How to Run
To begin the simulation, run main.py and select a scenario (1, 2, or 3) and execute the corresponding function (`check1`, `check2`, or `check3`). The initial and final states of the world will be displayed, along with explanatory prints detailing the process and results.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
