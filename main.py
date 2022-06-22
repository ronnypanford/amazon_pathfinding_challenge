from pathfinder import PathFinder
import argparse


amazon_pathfinder = PathFinder([])

amazon_pathfinder.create_grid(2, 2)
amazon_pathfinder.set_starting_point((0, 0))
amazon_pathfinder.set_delivery_point((1, 1))
amazon_pathfinder.add_random_obstacles(1)

amazon_pathfinder.find_all_paths()
print(amazon_pathfinder.all_paths)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Amazon Path Finder")
    parser.add_argument("--grid-width", type=int, help="Grid width", default=10)
    parser.add_argument("--grid-height", type=int, help="Grid height", default=10)
    parser.add_argument("--start-x", type=int, help="Starting x coordinate", default=0)
    parser.add_argument("--start-y", type=int, help="Starting y coordinate", default=0)
    parser.add_argument("--end-x", type=int, help="Ending x coordinate", default=9)
    parser.add_argument("--end-y", type=int, help="Ending y coordinate", default=9)
    parser.add_argument("--obstacles", type=int, help="Number of obstacles", default=0)
    args = parser.parse_args()

    amazon_pathfinder = PathFinder([])
    amazon_pathfinder.create_grid(args.grid_width, args.grid_height)
    amazon_pathfinder.set_starting_point((args.start_x, args.start_y))
    amazon_pathfinder.set_delivery_point((args.end_x, args.end_y))
    amazon_pathfinder.add_random_obstacles(args.obstacles)

    amazon_pathfinder.find_all_paths()