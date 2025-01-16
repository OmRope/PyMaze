# PyMaze Algorithm Visualizer

## Overview
PyMaze Algorithm Visualizer is an interactive application that allows users to create and solve mazes using various pathfinding algorithms. The platform is designed to provide an educational and engaging experience, helping users understand the mechanics and functionality of algorithms such as BFS, DFS, A*, and Dijkstra. Through this tool, users can explore how different algorithms perform on mazes of varying complexities.

## Features

### Maze Generation
- Create a maze of custom dimensions and complexity.
- Set maze dimensions to any size.
- Control the complexity with a loop percentage, which determines the maze's intricacy.

### Pathfinding Algorithms
Visualize and compare the following pathfinding algorithms:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A* Search**
- **Dijkstra's Algorithm**

### Algorithm Comparison
- Compare the performance of two algorithms:
  - Path length
  - Execution time

### Customizable Parameters
- **Maze Dimensions**: Set the width and height of the maze.
- **Loop Percentage**: Determines the complexity of the maze.
- **Start and End Points**: Define custom start and end points for pathfinding algorithms.

# Getting Started

## Prerequisites
Ensure you have the following installed:

- Python 3.7 or later
- Required libraries:
  - `tkinter`
  - `pymaze`

Install additional dependencies if needed:
```bash
pip install pymaze
```

## Installation
Clone the repository:
```bash
git clone https://github.com/OmRope/PyMaze.git
cd PyMaze
```

Run the main script:
```bash
python main.py
```

---

# Usage

### Step 1: Configure the Maze
- Input maze dimensions (rows and columns).
- Set the loop percentage for complexity (1-100%).

### Step 2: Define Start and End Points
- Choose whether to specify the end coordinates manually or use the default.

### Step 3: Select an Algorithm
- Choose a pathfinding algorithm to solve the maze.

### Step 4: Compare Algorithms (Optional)
- Select two algorithms to compare their performance metrics.

---

# Visual Components

## Tkinter GUI
- **Canvas Creation**: The GUI enables interactive maze generation and solving.
- **Control Panel**: Buttons and input fields for algorithm selection and configuration.

---

# Available Algorithms

### Breadth-First Search (BFS)
- Explores the shortest path by expanding all neighbors at the current depth.

### Depth-First Search (DFS)
- Explores paths by going deep before backtracking.

### A* Search
- Combines heuristic and path cost for optimal pathfinding.

### Dijkstra's Algorithm
- Finds the shortest path by expanding nodes with the least cumulative cost.

---

# Code Structure
- `main.py`: Entry point of the application.
- `agents.py`: Defines agent behaviors for maze traversal.
- `pymaze`: Core library for maze generation and visualization.

---

# Demo
Run the application:
```bash
python main.py
```
Follow the prompts in the console to create and solve a maze.
Visualize the results on the graphical interface.

---

# Future Enhancements
- Add more algorithms (e.g., Greedy Best-First Search).
- Implement 3D mazes for advanced visualization.
- Provide detailed performance analysis graphs.

---

# Contributing
Feel free to fork this repository and submit pull requests. Contributions are always welcome!


