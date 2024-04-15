import math
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal)
        self.f = 0  # Total estimated cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    # Euclidean distance heuristic
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

def astar(start, goal, blocked):
    open_set = []
    closed_set = set()

    start_node = Node(start)
    start_node.g = 0
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g + start_node.h
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node.position)

        for neighbor in neighbors(current_node.position, blocked):
            if neighbor in closed_set:
                continue

            g = current_node.g + 1  # Assuming each step costs 1
            h = heuristic(neighbor, goal)
            f = g + h
            neighbor_node = Node(neighbor, parent=current_node)
            neighbor_node.g = g
            neighbor_node.h = h
            neighbor_node.f = f

            heapq.heappush(open_set, neighbor_node)

    return None  # No path found

def neighbors(position, blocked):
    x, y = position
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Assuming 4-connected grid
    return [(nx, ny) for nx, ny in neighbors if (nx, ny) not in blocked]


start = (0, 0)
goal = (300, 900)
blocked = {(100, 100), (100, 200), (100, 300), (200, 300), (300, 300), (300, 200), (300, 100), (1, 1), (1, 0)}

path = astar(start, goal, blocked)
print(path)