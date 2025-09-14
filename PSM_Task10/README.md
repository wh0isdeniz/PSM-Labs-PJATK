# Customizable Game of Life 🟩⬜

This project implements a **customizable version of Conway's Game of Life**, where users can define and dynamically change the survival and birth rules during the simulation.

---

## Features
- **Cyclic boundaries** (edges wrap around like a torus 🌐).  
- **Custom rules**:
  - Define **survival rules** (how many neighbors keep a cell alive).  
  - Define **birth rules** (how many neighbors bring a new cell to life).  
- **Dynamic rule changes**: every 5 generations, you can decide to change the rules.  
- **Graphical text-based display**:  
  - `⬛` = alive cell  
  - `⬜` = dead cell  

---

## Example Rules
- **Classic Game of Life**:  
  - Survival: `2,3`  
  - Birth: `3`  

- **HighLife** (famous variant):  
  - Survival: `2,3`  
  - Birth: `3,6`  

You can experiment with many more!

---

## How It Works
1. The grid is initialized randomly with live (`1`) and dead (`0`) cells.  
2. For each cell:
   - Count the **8 neighbors** (with cyclic wrapping).  
   - Apply **survival rules** (if alive).  
   - Apply **birth rules** (if dead).  
3. The simulation runs for 20 generations by default, with pauses between steps.  
4. Every 5 generations, you can choose whether to change the rules.  

---

## Requirements
- Python 3.x  
- `numpy`  

---

## How to Run
```bash
python custom_game_of_life.py
