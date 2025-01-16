# PyMaze - Maze Game

**Overview**

PyMaze Algorithm Visualizer is an interactive application designed to create and solve mazes using various pathfinding algorithms. It provides an educational platform for understanding the mechanics of algorithms like BFS, DFS, A*, and Dijkstra in a visual and engaging way. 

**Features:**

* **Maze Generation: ** Generates customizable mazes with varying levels of complexity and obstacles.
* **Algorithm Selection: ** Choose from multiple pathfinding algorithms:
    * Breadth-First Search (BFS)
    * Depth-First Search (DFS)
    * A* Search
    * Greedy Best-First Search
* **Algorithm Comparison: ** Compare the performance (path length and execution time) of two algorithms.
* **Customizable Parameters: **
         * Maze dimensions
         * Loop percentage (determines complexity)
         * Start and end points


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


