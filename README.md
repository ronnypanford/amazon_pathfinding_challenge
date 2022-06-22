# amazon_pathfinding_challenge

To run:

Run python main.py

Pass the following where necessary

*REQUIRED*
 --grid-width: The width of the grid. e.g. --grid-width 3

 --grid-height: The height of the grid. e.g. --grid-height 3

 --start: The starting point of the pathfinder. e.g. --start (0,0)

 --end: The ending point of the pathfinder (delivery destination). e.g --end (5,5)

*OPTIONAL*
 --obstacle: Use this to place an obstacle on the grid (Can be used multiple times to place multiple obstacles).
        e.g. --obstacle (0,0)      .............. ....for a single obstacle
            --obstacle (0,0) --obstacle (1,1)......... for multiple obstacles

 --random-obstacles: Use this to add random obstacles on the grid. e.g. --random-obstacles 10 where 10 is the number of obstacles to place

 --obstacle-unremoveable: Raise this flag to make obstacles unremoveable. Thus no paths can suggest an obstacle to be removed if it cannot find a clear path.

Example usage:

python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (1,5) --obstacle (0,1) --obstacle (1,0) --random-obstacles 4 --obstacles-unremoveable

python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (1,5) --obstacle (0,1) --obstacle (1,0) --random-obstacles 2

python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (3,5) --obstacle (2,1) --obstacle (1,2)

python main.py --grid-width 3 --grid-height 3 --start (0,0) --end (2,2) --obstacle (0,1) --obstacle (1,0) --obstacle (1,1) --obstacles-unremoveable

python main.py --grid-width 3 --grid-height 3 --start (0,0) --end (2,2) --obstacle (0,1) --obstacle (1,0) --obstacle (1,1)
