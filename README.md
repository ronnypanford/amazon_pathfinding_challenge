# amazon_pathfinding_challenge

## Description
Implementation of a pathfinding algorithm for Amazon’s self-driving delivery vehicles. The self-driving vehicle will need to create a path on a 2D-grid that contains a starting point (x,y), a delivery point (x,y) and a number of obstacles. The vehicle
through this pathfinder can navigate to any of the adjacent squares (even diagonally), as long as the squares are inbound and do not contain an obstacle.

Finder can process all the obstacles in the grid and create a path to the delivery point.
Computing adjacent and diagonal squares with ability to identify obstacles that can be removed to obtain the shortest path to the delivery point, while removing the least number of obstacles to be removed to attain this.

## To run:

```bash
python main.py
```

Pass the following where necessary

## *REQUIRED*

 --grid-width: The width of the grid. 
 
       e.g. --grid-width 3

 --grid-height: The height of the grid. 
 
       e.g. --grid-height 3

 --start: The starting point of the pathfinder. 
 
       e.g. --start (0,0)

 --end: The ending point of the pathfinder (delivery destination). 
 
       e.g --end (5,5)

## *OPTIONAL*

 --obstacle: Use this to place an obstacle on the grid (Can be used multiple times to place multiple obstacles).
 
        e.g. --obstacle (0,0)      ..................for a single obstacle
            --obstacle (0,0) --obstacle (1,1)......... for multiple obstacles

 --random-obstacles: Use this to add random obstacles on the grid. 
 
        e.g. --random-obstacles 10 where 10 is the number of obstacles to place


 --obstacle-unremoveable: Raise this flag to make obstacles unremoveable. Thus no paths can suggest an obstacle to be removed if it cannot find a clear path.

## Example usage:

```bash
python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (1,5) --obstacle (0,1) --obstacle (1,0) --random-obstacles 4 --obstacles-unremoveable

python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (1,5) --obstacle (0,1) --obstacle (1,0) --random-obstacles 2

python main.py --grid-width 6 --grid-height 6 --start (0,0) --end (3,5) --obstacle (2,1) --obstacle (1,2)

python main.py --grid-width 3 --grid-height 3 --start (0,0) --end (2,2) --obstacle (0,1) --obstacle (1,0) --obstacle (1,1) --obstacles-unremoveable

python main.py --grid-width 3 --grid-height 3 --start (0,0) --end (2,2) --obstacle (0,1) --obstacle (1,0) --obstacle (1,1)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Task Link
[PATH FINDING CHALLENGE](https://brightnetwork.egnyte.com/dl/JTioVLInlf)
