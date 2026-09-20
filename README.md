# AI Practical Task

This repository contains two Artificial Intelligence practical tasks.

## Part 1 – Heuristic Search using A*

A* Search is used to find the shortest path from a START node to a GOAL node.

Formula:

f(n) = g(n) + h(n)

Where:

- g(n) = actual cost from START to the current node
- h(n) = estimated cost from current node to GOAL
- f(n) = total estimated cost

### Graph

S → A = 3  
S → C = 2  
A → B = 4  
B → D = 5  
C → D = 2

### Result

Final Path:

S → C → D

Total Cost:

4

---

## Part 2 – Local Search in Continuous Space

Hill Climbing is a local search algorithm that starts from an initial solution and continuously moves towards a better neighboring solution.

Function:

f(x) = (x - 5)^2 + 10

### Result

Approximate x:

5.0

Minimum value of f(x):

10.0

---

## Technologies Used

- Python
- A* Search
- Hill Climbing
