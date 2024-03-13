import math





def MovePenVector(direction, distance):
    direction_rad = math.radians(direction)

    delta_x = distance * math.cos(direction_rad)
    delta_y = distance * math.sin(direction_rad)

    print(delta_x, delta_y)
    