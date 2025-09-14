# L-System Plant Simulation 🌱

This project uses an **L-system (Lindenmayer system)** with **turtle graphics** to generate and draw a fractal-like plant structure.

---

## How It Works
An **L-system** is a string rewriting system often used to model the growth of plants.  
- Start with an **axiom** (initial word).  
- Apply **production rules** iteratively to expand the word.  
- Interpret the word as drawing instructions using turtle graphics.

---

## Rules Used
- **Axiom (initial word):** `X`  
- **Rules:**  
  - `X → F+[[X]-X]-F[-FX]+X`  
  - `F → FF`  

---

## Drawing Commands
- `F` → Move forward (draw a line).  
- `+` → Turn right by a fixed angle.  
- `-` → Turn left by a fixed angle.  
- `[` → Save current position and heading (push to stack).  
- `]` → Restore last saved position and heading (pop from stack).  

This stack mechanism allows branching, which is why the plant looks realistic.

---

## Parameters
- **Angle:** `25°`  
- **Length:** `5` (step size for forward moves)  
- **Iterations:** `5`  

Increasing iterations creates more detailed plants 🌿.

---

## Requirements
- Python 3.x  

The `turtle` module is part of the Python standard library, so no extra installation is required.

---

## How to Run
```bash
python lsystem_plant.py
