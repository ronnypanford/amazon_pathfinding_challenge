from pathfinder import PathFinder


def test_phase_one():
    """
    It creates a 10x10 grid, sets the starting point to (0,0),
    sets the delivery point to (9,9), adds obstacles at (9,7), (8,7),
    (6,7), (6,8) and then finds the shortest path by distance and by steps
    """
    amazon_pathfinder = PathFinder([])

    amazon_pathfinder.create_grid(10, 10)
    assert amazon_pathfinder.grid == [
        [0 for x in range(10)] for y in range(10)]

    amazon_pathfinder.set_starting_point((0, 0))
    assert amazon_pathfinder.starting_point == (0, 0)

    amazon_pathfinder.set_delivery_point((9, 9))
    assert amazon_pathfinder.delivery_point == (9, 9)

    amazon_pathfinder.add_obstacles([(9, 7), (8, 7), (6, 7), (6, 8)])
    assert amazon_pathfinder.obstacles == [(9, 7), (8, 7), (6, 7), (6, 8)]

    print("\nCreated grid of size 10x10")
    print("Starting point: (0,0)")
    print("Delivery point: (9,9)")
    print(f"Obstacles are placed at: {amazon_pathfinder.obstacles}")

    amazon_pathfinder.shortest_path(allow_obstacle_elimination=False)



def test_phase_two():
    """
    It creates a grid of size 10x10, sets the starting point to (0,0),
    sets the delivery point to (9,9), adds 4 obstacles, adds 20 random
    obstacles, finds the shortest path by least steps.
    """
    amazon_pathfinder = PathFinder([])

    amazon_pathfinder.create_grid(10, 10)
    assert amazon_pathfinder.grid == [
        [0 for x in range(10)] for y in range(10)]

    amazon_pathfinder.set_starting_point((0, 0))
    assert amazon_pathfinder.starting_point == (0, 0)

    amazon_pathfinder.set_delivery_point((9, 9))
    assert amazon_pathfinder.delivery_point == (9, 9)

    amazon_pathfinder.add_obstacles([(9, 7), (8, 7), (6, 7), (6, 8)])
    assert amazon_pathfinder.obstacles == [(9, 7), (8, 7), (6, 7), (6, 8)]

    amazon_pathfinder.add_random_obstacles(20)
    assert len(amazon_pathfinder.obstacles) == 24

    print("\nCreated grid of size 10x10")
    print("Starting point: (0,0)")
    print("Delivery point: (9,9)")
    print(f"Obstacles are placed at: {amazon_pathfinder.obstacles}")

    amazon_pathfinder.shortest_path(allow_obstacle_elimination=False)


def test_phase_bonus():
    """
    It creates a grid of size 10x10, sets the starting point to (0,0),
    sets the delivery point to (9,9), adds 4 obstacles, adds 20 random
    obstacles, finds the shortest path by least steps. If no path found 
    it allows for the shortest path through pbstacles and sggests 
    the shortest path with the least obstacles to be removed.
    """
    amazon_pathfinder = PathFinder([])

    amazon_pathfinder.create_grid(10, 10)
    assert amazon_pathfinder.grid == [
        [0 for x in range(10)] for y in range(10)]

    amazon_pathfinder.set_starting_point((0, 0))
    assert amazon_pathfinder.starting_point == (0, 0)

    amazon_pathfinder.set_delivery_point((9, 9))
    assert amazon_pathfinder.delivery_point == (9, 9)

    amazon_pathfinder.add_obstacles([(9, 7), (8, 7), (6, 7), (6, 8)])
    assert amazon_pathfinder.obstacles == [(9, 7), (8, 7), (6, 7), (6, 8)]

    amazon_pathfinder.add_random_obstacles(20)
    assert len(amazon_pathfinder.obstacles) == 24

    print("\nCreated grid of size 10x10")
    print("Starting point: (0,0)")
    print("Delivery point: (9,9)")
    print(f"Obstacles are placed at: {amazon_pathfinder.obstacles}")

    amazon_pathfinder.shortest_path(allow_obstacle_elimination=True)


# if __name__ == "__main__":
    # test_phase_one()
    # test_phase_two()
    # test_phase_bonus()
