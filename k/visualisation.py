import math
import turtle
blocked = []

class Navigation():
    def GetNumberInCordinates(centimeters):
        cordinates = centimeters / 0.0508
        return cordinates

    def jump_point_search(start=None, end=[]):
        def is_blocked(point, blocked):
            return point in blocked
        def get_next_point(point, angle, distance=1):
            return [point[0] + distance * math.cos(angle), point[1] + distance * math.sin(angle)]
        if start == None:
            start = [x, y]
        current = start
        delta_x = end[0] - start[0]
        delta_y = end[1] - start[1]
        
        distance = math.dist(start, end)
        angle_radians = math.atan2(delta_y, delta_x)
        angle_degrees = math.degrees(angle_radians)
        
        jump_start_list = []
        jump_finish_list = []
        
        if angle_degrees > -45 or angle_degrees < 45:
            direction = "right"
        elif angle_degrees > 45 or angle_degrees < 135:
            direction = "up"
        elif angle_degrees > 135 or angle_degrees < -135:
            direction = "left"
        elif angle_degrees > -135 or angle_degrees < -45:
            direction = "down"
        
        while current != end:
            if direction == "right":
                jump_start_list.append(current)
                cost_efficient = True
                while cost_efficient == True or current[0]+1 in blocked:
                    dist1 = math.dist(current, end)
                    current[0] += 1
                    dist2 = math.dist(current, end)
                    if dist2 > dist1:
                        cost_efficient = False
                if angle_degrees > 0:
                    secondary_direction = "up"
                elif angle_degrees < 0:
                    secondary_direction = "down"
                cost_efficient = True
                if secondary_direction == "up":
                    while cost_efficient == True or current[1]+1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[1] += 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                elif secondary_direction == "down":
                    while cost_efficient == True or current[1]-1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[1] -= 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                
                pointdistance = math.dist(start, end)
                sec_angle_radians = math.atan2(change_y, change_x)
                sec_angle_degrees = math.degrees(angle_radians)
                
                checkstart = jump_start_list[-1]
                checkprogress = checkstart
                checkfinish = jump_finish_list[-1]
                blockonpath = False
                while checkprogress != checkfinish:
                    get_next_point(current, sec_angle_degrees)
                    if is_blocked(current, blocked):
                        blockonpath = True
                if blockonpath == True:
                    if secondary_direction == "up":
                        while still_blocked == True:
                            jump_finish_list.pop()
                            current[1]-20
                            jump_finish_list.append(current)
                            change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                            change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                            
                            pointdistance = math.dist(start, end)
                            sec_angle_radians = math.atan2(change_y, change_x)
                            sec_angle_degrees = math.degrees(angle_radians)
                            
                            checkstart = jump_start_list[-1]
                            checkprogress = checkstart
                            checkfinish = jump_finish_list[-1]
                            blockonpath = False
                            still_blocked = False
                            while checkprogress != checkfinish:
                                get_next_point(current, sec_angle_degrees)
                                if is_blocked(current, blocked):
                                    still_blocked = True
                                    blockonpath = True
                            if still_blocked == False:
                                blockonpath = False
                            Navigation.jump_point_search(current, end)
                    if secondary_direction == "down":
                        while still_blocked == True:
                                jump_finish_list.pop()
                                current[1]+20
                                jump_finish_list.append(current)
                                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                                
                                pointdistance = math.dist(start, end)
                                sec_angle_radians = math.atan2(change_y, change_x)
                                sec_angle_degrees = math.degrees(angle_radians)
                                
                                checkstart = jump_start_list[-1]
                                checkprogress = checkstart
                                checkfinish = jump_finish_list[-1]
                                blockonpath = False
                                still_blocked = False
                                while checkprogress != checkfinish:
                                    get_next_point(current, sec_angle_degrees)
                                    if is_blocked(current, blocked):
                                        still_blocked = True
                                        blockonpath = True
                                if still_blocked == False:
                                    blockonpath = False
                                Navigation.jump_point_search(current, end)
            elif direction == "up":
                jump_start_list.append(current)
                cost_efficient = True
                while cost_efficient == True or current[1]+1 in blocked:
                    dist1 = math.dist(current, end)
                    current[1] += 1
                    dist2 = math.dist(current, end)
                    if dist2 > dist1:
                        cost_efficient = False
                if angle_degrees > -90 and angle_degrees < 90:
                    secondary_direction = "right"
                elif angle_degrees < -90 or angle_degrees > 90:
                    secondary_direction = "left"
                cost_efficient = True
                if secondary_direction == "right":
                    while cost_efficient == True or current[0]+1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[0] += 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                elif secondary_direction == "left":
                    while cost_efficient == True or current[0]-1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[0] -= 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                
                pointdistance = math.dist(start, end)
                sec_angle_radians = math.atan2(change_y, change_x)
                sec_angle_degrees = math.degrees(angle_radians)
                
                checkstart = jump_start_list[-1]
                checkprogress = checkstart
                checkfinish = jump_finish_list[-1]
                blockonpath = False
                while checkprogress != checkfinish:
                    get_next_point(current, sec_angle_degrees)
                    if is_blocked(current, blocked):
                        blockonpath = True
                if blockonpath == True:
                    if secondary_direction == "right":
                        while still_blocked == True:
                            jump_finish_list.pop()
                            current[0]-20
                            jump_finish_list.append(current)
                            change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                            change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                            
                            pointdistance = math.dist(start, end)
                            sec_angle_radians = math.atan2(change_y, change_x)
                            sec_angle_degrees = math.degrees(angle_radians)
                            
                            checkstart = jump_start_list[-1]
                            checkprogress = checkstart
                            checkfinish = jump_finish_list[-1]
                            blockonpath = False
                            still_blocked = False
                            while checkprogress != checkfinish:
                                get_next_point(current, sec_angle_degrees)
                                if is_blocked(current, blocked):
                                    still_blocked = True
                                    blockonpath = True
                            if still_blocked == False:
                                blockonpath = False
                            Navigation.jump_point_search(current, end)
                    if secondary_direction == "left":
                        while still_blocked == True:
                                jump_finish_list.pop()
                                current[0]+20
                                jump_finish_list.append(current)
                                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                                
                                pointdistance = math.dist(start, end)
                                sec_angle_radians = math.atan2(change_y, change_x)
                                sec_angle_degrees = math.degrees(angle_radians)
                                
                                checkstart = jump_start_list[-1]
                                checkprogress = checkstart
                                checkfinish = jump_finish_list[-1]
                                blockonpath = False
                                still_blocked = False
                                while checkprogress != checkfinish:
                                    get_next_point(current, sec_angle_degrees)
                                    if is_blocked(current, blocked):
                                        still_blocked = True
                                        blockonpath = True
                                if still_blocked == False:
                                    blockonpath = False
                                Navigation.jump_point_search(current, end)
            elif direction == "left":
                jump_start_list.append(current)
                cost_efficient = True
                while cost_efficient == True or current[0]-1 in blocked:
                    dist1 = math.dist(current, end)
                    current[0] -= 1
                    dist2 = math.dist(current, end)
                    if dist2 > dist1:
                        cost_efficient = False
                if angle_degrees > 0:
                    secondary_direction = "up"
                elif angle_degrees < 0:
                    secondary_direction = "down"
                cost_efficient = True
                if secondary_direction == "up":
                    while cost_efficient == True or current[1]+1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[1] += 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                elif secondary_direction == "down":
                    while cost_efficient == True or current[1]-1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[1] -= 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                
                pointdistance = math.dist(start, end)
                sec_angle_radians = math.atan2(change_y, change_x)
                sec_angle_degrees = math.degrees(angle_radians)
                
                checkstart = jump_start_list[-1]
                checkprogress = checkstart
                checkfinish = jump_finish_list[-1]
                blockonpath = False
                while checkprogress != checkfinish:
                    get_next_point(current, sec_angle_degrees)
                    if is_blocked(current, blocked):
                        blockonpath = True
                if blockonpath == True:
                    if secondary_direction == "up":
                        while still_blocked == True:
                            jump_finish_list.pop()
                            current[1]-20
                            jump_finish_list.append(current)
                            change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                            change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                            
                            pointdistance = math.dist(start, end)
                            sec_angle_radians = math.atan2(change_y, change_x)
                            sec_angle_degrees = math.degrees(angle_radians)
                            
                            checkstart = jump_start_list[-1]
                            checkprogress = checkstart
                            checkfinish = jump_finish_list[-1]
                            blockonpath = False
                            still_blocked = False
                            while checkprogress != checkfinish:
                                get_next_point(current, sec_angle_degrees)
                                if is_blocked(current, blocked):
                                    still_blocked = True
                                    blockonpath = True
                            if still_blocked == False:
                                blockonpath = False
                            Navigation.jump_point_search(current, end)
                    if secondary_direction == "down":
                        while still_blocked == True:
                                jump_finish_list.pop()
                                current[1]+20
                                jump_finish_list.append(current)
                                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                                
                                pointdistance = math.dist(start, end)
                                sec_angle_radians = math.atan2(change_y, change_x)
                                sec_angle_degrees = math.degrees(angle_radians)
                                
                                checkstart = jump_start_list[-1]
                                checkprogress = checkstart
                                checkfinish = jump_finish_list[-1]
                                blockonpath = False
                                still_blocked = False
                                while checkprogress != checkfinish:
                                    get_next_point(current, sec_angle_degrees)
                                    if is_blocked(current, blocked):
                                        still_blocked = True
                                        blockonpath = True
                                if still_blocked == False:
                                    blockonpath = False
                                Navigation.jump_point_search(current, end)
            elif direction == "down":
                jump_start_list.append(current)
                cost_efficient = True
                while cost_efficient == True or current[1]-1 in blocked:
                    dist1 = math.dist(current, end)
                    current[1] -= 1
                    dist2 = math.dist(current, end)
                    if dist2 > dist1:
                        cost_efficient = False
                if angle_degrees > -90 and angle_degrees < 90:
                    secondary_direction = "right"
                elif angle_degrees < -90 or angle_degrees > 90:
                    secondary_direction = "left"
                cost_efficient = True
                if secondary_direction == "right":
                    while cost_efficient == True or current[0]+1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[0] += 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                elif secondary_direction == "left":
                    while cost_efficient == True or current[0]-1 in blocked or current == end:
                        dist1 = math.dist(current, end)
                        current[0] -= 1
                        dist2 = math.dist(current, end)
                        if dist2 > dist1:
                            cost_efficient = False
                    jump_finish_list.append(current)
                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                
                pointdistance = math.dist(start, end)
                sec_angle_radians = math.atan2(change_y, change_x)
                sec_angle_degrees = math.degrees(angle_radians)
                
                checkstart = jump_start_list[-1]
                checkprogress = checkstart
                checkfinish = jump_finish_list[-1]
                blockonpath = False
                while checkprogress != checkfinish:
                    get_next_point(current, sec_angle_degrees)
                    if is_blocked(current, blocked):
                        blockonpath = True
                if blockonpath == True:
                    if secondary_direction == "right":
                        while still_blocked == True:
                            jump_finish_list.pop()
                            current[0]-20
                            jump_finish_list.append(current)
                            change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                            change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                            
                            pointdistance = math.dist(start, end)
                            sec_angle_radians = math.atan2(change_y, change_x)
                            sec_angle_degrees = math.degrees(angle_radians)
                            
                            checkstart = jump_start_list[-1]
                            checkprogress = checkstart
                            checkfinish = jump_finish_list[-1]
                            blockonpath = False
                            still_blocked = False
                            while checkprogress != checkfinish:
                                get_next_point(current, sec_angle_degrees)
                                if is_blocked(current, blocked):
                                    still_blocked = True
                                    blockonpath = True
                            if still_blocked == False:
                                blockonpath = False
                            Navigation.jump_point_search(current, end)
                    if secondary_direction == "left":
                        while still_blocked == True:
                                jump_finish_list.pop()
                                current[0]+20
                                jump_finish_list.append(current)
                                change_x = jump_finish_list[-1][0] - jump_start_list[-1][0]
                                change_y = jump_finish_list[-1][1] - jump_start_list[-1][1]
                                
                                pointdistance = math.dist(start, end)
                                sec_angle_radians = math.atan2(change_y, change_x)
                                sec_angle_degrees = math.degrees(angle_radians)
                                
                                checkstart = jump_start_list[-1]
                                checkprogress = checkstart
                                checkfinish = jump_finish_list[-1]
                                blockonpath = False
                                still_blocked = False
                                while checkprogress != checkfinish:
                                    get_next_point(current, sec_angle_degrees)
                                    if is_blocked(current, blocked):
                                        still_blocked = True
                                        blockonpath = True
                                if still_blocked == False:
                                    blockonpath = False
                                Navigation.jump_point_search(current, end)
        print("a")
        grid_turtle.penup()
        grid_turtle.goto(-500, -500)
        grid_turtle.pencolor("red")
        grid_turtle.penup()
        for i in range("jump_start_list"):
            grid_turtle.goto(jump_start_list[i])
            grid_turtle.pendown()
            grid_turtle.goto(jump_finish_list[i])
            grid_turtle.penup()

window = turtle.Screen()
grid_turtle = turtle.Turtle()
Navigation.jump_point_search([0, 0], [300, 100])
turtle.done()
        
x = 0
y = 0 