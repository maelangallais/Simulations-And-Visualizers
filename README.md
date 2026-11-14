# 🔬 Simulations & Visualizers

A collection of **scientific simulations, cellular automata, and algorithm visualizers** written in MicroPython for the **NumWorks** calculator.

---

## 📂 Scripts Included

### Conway's Game of Life
[`game_of_life.py`](game_of_life.py) · *Created February 06, 2024*

Real-time simulation of **John Conway's Game of Life** cellular automaton on the `320 × 222` Kandinsky screen:
- Configurable cell resolution via the `m` parameter (default `m = 8`, minimum `4` on NumWorks hardware).
- Runs continuously without artificial frame delays to maximize iteration speed on the calculator.

### Sorting Algorithm Visualizer
[`sorting_visualizer.py`](sorting_visualizer.py) · *Algorithm Visualization*

Visualizes two classic sorting algorithms side-by-side on a shuffled array of **80 bars** using `kandinsky`:
- **Bubble Sort** (simple, $O(n^2)$).
- **Quick Sort** (divide-and-conquer, $O(n \log n)$ average).

### Mach-Zehnder Interferometer Visualizer
[`mach_zehnder_interferometer.py`](mach_zehnder_interferometer.py) · *Created June 03, 2026*

Parametric `turtle` geometry visualizer for **Mach-Zehnder interferometers** (`d(L, R, S, I)`):
- `L`: Total interferometer length.
- `R`: Bending radius of the curved waveguides (must satisfy $R > L / 4$).
- `S`: Flat section length along the interferometer arm (must satisfy $S < L$).
- `I`: Orientation toggle.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `turtle`, `ion`, `math`, `random`, `time`).
