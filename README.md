# Conway's Game of Life

Conway's Game of Life simulates the lives of simple cells that obey algorithmic
laws. Each cell will interact with each of it's eight neighbors; horizontal,
vertical and diagonal cells. Each loop of the program is one generation, and
cells will die or be born according to the laws they obey.

## Laws
* Each cell interacts with it's adjacent eight cells.
* Each cell has two states, dead (0) or alive (1).
* Any live cell with fewer than two live neighbors (0 or 1) will die.
* Any live cell with two or three live neighbors lives to the next generation.
* Any live cell with more than three (4+) live neighbors dies.
* Any dead cell with exactly three live neighbors becomes a live cell.

## How to Download and Run
Simply copy the git repository to your device! Ensure you have the requirements
installed, which for this is only pygame for the graphics. Then just use the
python command to run!

## Current State
Cells will loop around so the space is finite versus infinite. The game starts in
the paused state so the user can create their own start state.

## Controls
Exc - Quit  
P - Pause/Unpause  
Left Arrow - Slow Time  
Right Arrow - Quicken Time  
#### When Paused
Left Click - Create Life  
Right Click - End Life  

## TODO
- [X] Fix window and array size mismatch
- [X] Fix looping of cells and clean up adjacent count function
- [X] Create way to more easily create start states
- [X] Add Speed Control
- [X] Add Pause and UnPause
- [ ] Create Random Life Button