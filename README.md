# 🤖 Python Robot Pathfinding

![Python](https://img.shields.io/badge/Python-3.x-blue)

![Algorithm](https://img.shields.io/badge/Algorithm-A*-yellow)

![License](https://img.shields.io/badge/License-MIT-green) 

![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📘 Overview

This repository contains the final project for the **“An Introduction to Programming using Python”** course from **Coursera**, completed as part of my **B.Tech in Computer Science and Engineering** curriculum.

The goal of this project is to demonstrate a robust, from-scratch implementation of a complex pathfinding algorithm. The script builds a "brain" for a robot to find the shortest possible path from a starting point ('R') to a goal ('G') in a 2D text-based grid, navigating around obstacles ('X').

The project's two primary objectives are:

1. To implement the **A* (A-Star) search algorithm** using foundational Python data structures.
    
2. To provide a **step-by-step console animation** of the robot's movement along the calculated optimal path.
    

---

## 📂 Repository Structure

```
robot-pathfinding-using-python/
│
├── README.md
└── robot.py
```

The repository is built around a single, self-contained Python script (`robot.py`) that includes all helper functions, the A* algorithm logic, and the final visualization.

---

## ⚙️ Setup and Usage

### 1. Clone the Repository

```
git clone https://github.com/Vishwajit1610/robot-pathfinding-using-python
cd robot-pathfinding-using-python
```

### 2. Create a Virtual Environment (Recommended)

```
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```

### 3. Install Dependencies

This project uses only Python's built-in libraries (`heapq` and `time`), so **no `requirements.txt` file or external package installation is necessary.**

### 4. Run the Script

Simply run the `robot.py` file to see the pathfinding and animation in your terminal:

```
python robot.py
```

---

## 🧩 Project Components

### 🧠 The A* Algorithm Engine

The **"brain"** of the robot is a complete implementation of the A* search algorithm. It efficiently finds the shortest path by always exploring the most promising square on the grid. It makes this decision using a heuristic formula:

**`f(n) = g(n) + h(n)`**

- **`g(n)`:** The true cost (number of steps) from the start to the current square `n`.
    
- **`h(n)`:** The heuristic, or estimated cost, from `n` to the goal. This project uses the **Manhattan distance** for a fast and effective estimate.
    

### 📦 Key Data Structures

- **`heapq` (Priority Queue):** The `open_set` list is managed as a priority queue to ensure the algorithm always processes the square with the lowest `f_score` first.
    
- **`g_score` (Dictionary):** Tracks the "pedometer" cost (the `g(n)` value) for each explored square.
    
- **`came_from` (Dictionary):** Stores the "breadcrumb trail" used to reconstruct the final path by tracing it backward from the goal.
    

### 🎬 Console Animation

The "legs" of the robot. Once the A* algorithm finds the optimal path, a dedicated animation loop takes over to provide a step-by-step visualization:

1. The initial grid state is displayed.
    
2. The loop iterates through the calculated path.
    
3. In each step, the robot's previous position is updated (leaving a `●` trail), and the robot `'R'` is drawn in its new position.
    
4. The grid is re-printed, and `time.sleep()` is called to create a visible, step-by-step movement.
    

---

## 🧠 Key Learning Outcomes

- Practical, from-scratch implementation of the **A* pathfinding algorithm**.
    
- Proficient use of **`heapq`** to manage a priority queue for an efficient search.
    
- Advanced use of **dictionaries** for cost-tracking (`g_score`) and path reconstruction (`came_from`).
    
- Strong procedural programming practices by separating logic into helper functions (`is_move_valid`, `reconstruct__path`, etc.).
    
- Creating dynamic **console-based animations** and visualizations using `print` and `time.sleep`.
    

---

## 🚀 Future Additions

This project serves as a strong foundation for more advanced work:

- **Graphical Interface:** Rebuild the visualization using a library like **Pygame** or **Tkinter** to create a graphical, real-time representation (as seen in the project's inspiration image).
    
- **Weighted Grids:** Introduce "difficult terrain" (e.g., 'water' or 'mud') that costs more than 1 step to move through, testing the full power of the A* algorithm.
    
- **Dynamic Obstacles:** Add logic for the robot to re-calculate its path if a new 'X' appears in its way.
    

---

## 👨‍💻 Author

**Vishwajit Mohol**

**B.Tech CSE | 2nd Year Student**

**Course: An Introduction to Programming using Python -> Coursera (University Curriculum)**

**Building mastery in algorithms and Python through first principles and structured learning.**

##### 📫 Connect with me:

[![GitHub Profile](https://img.shields.io/badge/GitHub-Vishwajit1610-black?logo=github)](https://github.com/Vishwajit1610)  

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn-Vishwajit%20Mohol-blue?logo=linkedin)](https://www.linkedin.com/in/vishwajit-mohol)

---

## ⚖️ License

This project is licensed under the MIT License. Feel free to use and adapt the material with proper attribution.

```
MIT License

Copyright (c) 2025 Vishwajit Mohol

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---