# 🔬 Simulations & Visualizers

A collection of **scientific simulations, cellular automata, and algorithm visualizers** written in MicroPython for the **NumWorks** calculator.

---

## 📂 Scripts Included

### Conway's Game of Life *(Flagship Project)*
[`game_of_life.py`](game_of_life.py) · *Created February 06, 2024*

Real-time simulation of **John Conway's Game of Life** cellular automaton on the `320 × 222` Kandinsky screen with toroidal (wrap-around) edges:
- **Screen-as-Memory & Sub-Grid Buffering**: Instead of holding the entire grid in RAM, the script reads cell states directly from the screen via `kandinsky.get_pixel()` and processes the board in `t × t` sub-grids, buffering only the block contours (`gc`) to compute borders and corners afterwards without overwriting neighbor states.
- **Automatic Block Sizing**: `t` is computed from the grid dimensions (`max(8, min(round((w * h) ** (1 / 3) - 1), 40))`) and automatically adjusted if `w % (t + 1) == 1` or `h % (t + 1) == 1` to avoid 1-pixel edge slivers.
- **Resolution & Hardware Notes**: Configurable cell size via `m` (default `m = 6`). The minimum supported resolution on NumWorks hardware is now **`m = 2`** (down from `4`). At `m = 2`, iterations are very slow because of pixel-by-pixel screen reads, but RAM no longer saturates.
- **Flexible Initialization**: Start with a random primordial soup using `init_random()`, or place built-in patterns (`glider`, `lightweight_spaceship`, `koks_galaxy`)—or your own `;`-delimited patterns parsed with `decode()`—using `init_form(x, y, pattern)`.

Tweak `m`, mix built-in spaceships and oscillators, or design your own patterns—you can experiment freely with the simulation without running into memory limits.

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
