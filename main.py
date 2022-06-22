

if __name__ == "__main__":

    from pathfinder import PathFinder
    import argparse

    parser = argparse.ArgumentParser(description="Amazon Path Finder")
    
    parser.add_argument("--grid-width", type=int, help="Grid width", default=5)
    parser.add_argument("--grid-height", type=int, help="Grid height", default=5)
    parser.add_argument("--start", nargs='+', type=int, help="Starting coordinates. eg. --start (0,0)", default=(0,0))
    parser.add_argument("--end", nargs='+', type=int, help="Delivery coordinates. eg. --end (1,2)", default=(0,0))
    parser.add_argument("--obstacle", nargs='+', type=int, action='append', help="Coordinate of an obstacle. eg. --obstacle (1,1)", default=[])
    parser.add_argument("--random-obstacles", type=int, help="Number of obstacles", default=0)
    parser.add_argument("--path-factor", type=str, help="Method to select the shortest path by: steps, distance", default="distance")
    parser.add_argument("--obstacles-unremovable", action='store_true', help="Include flag to restrict path without suggestions to remove obstacles", default=False)
    
    args = parser.parse_args()

    amazon_pathfinder = PathFinder([])
    amazon_pathfinder.create_grid(args.grid_width, args.grid_height)
    amazon_pathfinder.set_starting_point(tuple(args.start))
    amazon_pathfinder.set_delivery_point(tuple(args.end))
    
    try:
        amazon_pathfinder.add_obstacles([tuple(obstacle) for obstacle in args.obstacle])
        amazon_pathfinder.add_random_obstacles(args.random_obstacles)

        print(f"\nCreated grid of size {args.grid_height}x{args.grid_width}")
        print(f"Starting point: {tuple(args.start)}")
        print(f"Delivery point: {tuple(args.end)}")
        print(f"Obstacles are placed at: {amazon_pathfinder.obstacles}")
        print(f"Finding shortest path by: least {args.path_factor}")

        amazon_pathfinder.shortest_path(allow_obstacle_elimination=not(args.obstacles_unremovable), filter=args.path_factor)
    except AssertionError:
        pass