# PyMaze - Maze Game

Overview
PyMaze Algorithm Visualizer is an interactive application designed to create and solve mazes using various pathfinding algorithms. It provides an educational platform for understanding the mechanics of algorithms like BFS, DFS, A*, and Dijkstra in a visual and engaging way. 

**Features:**

* **Maze Generation:** Generates customizable mazes with varying levels of complexity and obstacles.
* **Algorithm Selection:** Choose from multiple pathfinding algorithms:
    * Breadth-First Search (BFS)
    * Depth-First Search (DFS)
    * A* Search
    * Greedy Best-First Search
* **Visualization:** Dynamically visualizes the pathfinding process in real-time, allowing users to observe how each algorithm explores the maze.
* **Algorithm Comparison:** Observe the strengths and weaknesses of different algorithms in navigating the maze and dealing with various obstacles.

**Challenges and Complexities:**

* **Maze Design:** Designing mazes with varying levels of difficulty and interesting obstacle layouts to challenge the pathfinding algorithms.
* **Algorithm Implementation:** Correctly implementing the pathfinding algorithms, ensuring efficiency and accuracy.
* **Visualization:** Creating a clear and intuitive visualization of the pathfinding process, highlighting the current node, explored nodes, and the final path.

**Algorithm Descriptions:**

**Breadth-First Search (BFS)**

* **Exploration:** Explores all nodes at the current depth level before moving to the next level.
* **Data Structure:** Uses a Queue.
* **Time Complexity:** O(b^d) where b is the branching factor and d is the depth.
* **Strengths:** Guaranteed to find the shortest path.

**Depth-First Search (DFS)**

* **Exploration:** Explores a single path as deeply as possible before backtracking.
* **Data Structure:** Uses a Stack.
* **Time Complexity:** O(b^m) where b is the branching factor and m is the maximum depth.
* **Strengths:** Can find all possible paths, but may not be the shortest.

**A* Search**

* **Exploration:** Uses a heuristic function to estimate the distance to the goal, guiding the search.
* **Data Structure:** Typically uses a Priority Queue.
* **Time Complexity:** O(b^d) in the best case, but can be slower in practice depending on the heuristic.
* **Strengths:** Efficient and guaranteed to find the shortest path if the heuristic is admissible.

**Greedy Best-First Search**

* **Exploration:** Prioritizes nodes closest to the goal based on a heuristic.
* **Data Structure:** Uses a Priority Queue.
* **Time Complexity:** O(b^d)
* **Strengths:** Efficient in finding a path quickly, but may not always find the shortest path.

**Working of PyMaze**

1. **Algorithm Selection:** Choose the desired pathfinding algorithm.
2. **Maze Generation:** Generate a maze with varying complexity and obstacles.
3. **Visualization:** Run the selected algorithm and visualize its exploration process step-by-step.

