#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import random
from statistics import mean
import matplotlib.pyplot as plt

map_ = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], np.uint8)

map_image = map_*255
map_image2 = map_*255
rows, cols = map_image.shape

def set_color(i):
    color = random.randint(10, 240)
    for j in range(0,rows):
        if map_image[j,i] == 0:
            map_image[j,i] = color
        else:
            color = random.randint(10, 240)
            
i = 0
while (i < cols):
    set_color(i)
    i += 1
    
def set_color2(j):
    for i in range(0,cols):
        if map_image[j,i] != 255:
            color = random.randint(10,240)
            map_image[j,i] = color
        else:
            color = random.randint(10,240)
            
j = 0
while (j < rows):
    set_color2(j)
    j += 1

def scale(frame, percent):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    return resized

sized = scale(map_image, 5000)   
sized2 = scale(map_image2, 5000)  
sized = cv2.cvtColor(sized, cv2.COLOR_GRAY2BGR)        

i = 1
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 0, 0)
fontScale = 0.5
thickness = 2
locations = {}
obstacles = []

for m in range(0,rows):
    for n in range(0,cols):
        k = (m*50)+40
        j = (n*50)+15
        if sized[k,j,2] != 255:
            org = (j,k)
            locations[k-15,j+10] = 0
            image = cv2.putText(sized, str(i), org, font, fontScale, color, thickness, cv2.LINE_AA)
            i += 1
        else:
            obstacles.append([k-15,j+10])
        
for m in range(0,rows):
    for n in range(0,cols):
        k = (m*50)+40
        j = (n*50)+15
        if sized[k,j,2] != 255 and ([k,j] != [540,465]) and ([k,j] != [590,465]) and ([k,j] != [590,415]) and ([k,j] != [590,515]) and ([k,j] != [90,65]) and ([k,j] != [390,65]) and ([k,j] != [390,15]) and ([k,j] != [690,65]) and ([k,j] != [690,15]) and ([k,j] != [390,865]) and ([k,j] != [390,915]) and ([k,j] != [690,865]) and ([k,j] != [690,915]):
            org2 = (j+10,k-15)
            locations[k-15,j+10] = 1
            image = cv2.circle(sized2, org2, 5, 150, -1)
        else:
            pass

def FindCosts():
    pacman_costs = {}
    for i in open_nodes.keys():
        pacman_costs[i] = (abs(current_pacman_location[0]-i[0]) + abs(current_pacman_location[1]-i[1])) * open_nodes[i]
    return pacman_costs  

def SetGoal(pacman_costs):
    min_val = None
    result = None
    for key, value in pacman_costs.items():
        if value and (min_val is None or value < min_val):
            min_val = value
            result = key
    return result

def MoveRight(x,y,cost,p):
    p = p + 'R'
    x += 1
    if [x,y] in open_check:
        cost += 1
    else:
        cost += 1000
    return x,y,cost,p

def MoveLeft(x,y,cost,p):
    p = p + 'L'
    x -= 1
    if [x,y] in open_check:
        cost += 1
    else:
        cost += 1000
    return x,y,cost,p

def MoveUp(x,y,cost,p):
    p = p + 'U'
    y -= 1
    if [x,y] in open_check:
        cost += 1
    else:
        cost += 1000
    return x,y,cost,p

def MoveDown(x,y,cost,p):
    p = p + 'D'
    y += 1
    if [x,y] in open_check:
        cost += 1
    else:
        cost += 1000
    return x,y,cost,p

def MoveAround(x,y,cost,p):
    x_r, y_r, cost_r, p_r = MoveRight(x,y,cost,p)
    x_l, y_l, cost_l, p_l = MoveLeft(x,y,cost,p)
    x_u, y_u, cost_u, p_u = MoveUp(x,y,cost,p)
    x_d, y_d, cost_d, p_d = MoveDown(x,y,cost,p)
    return x_r, y_r, cost_r, p_r, x_l, y_l, cost_l, p_l, x_u, y_u, cost_u, p_u, x_d, y_d, cost_d, p_d

def PacmanPath(current_pacman_location):
    pacman_costs = FindCosts()
    goal = SetGoal(pacman_costs)
    current_cost = 0
    current_path = ''
    pacman_path = {current_pacman_location : (current_cost,current_path)}
    pacman_start = current_pacman_location
    if (([pacman_start[0], pacman_start[1]]) in closed_nodes) or ((([pacman_start[0] + 1, pacman_start[1]]) in closed_nodes) and (([pacman_start[0] - 1, pacman_start[1]]) in closed_nodes) and (([pacman_start[0], pacman_start[1] - 1]) in closed_nodes) and (([pacman_start[0], pacman_start[1] + 1]) in closed_nodes)):
        return 'I', pacman_start
    while (current_pacman_location[1] != goal[1]) or (current_pacman_location[0] != goal[0]):
        x_r, y_r, cost_r, p_r, x_l, y_l, cost_l, p_l, x_u, y_u, cost_u, p_u, x_d, y_d, cost_d, p_d = MoveAround(current_pacman_location[0], current_pacman_location[1], current_cost, current_path)
        if ([x_r, y_r] not in closed_nodes):
            pacman_path[x_r,y_r] = cost_r,p_r
        else:
            pass
        if ([x_l, y_l] not in closed_nodes):
            pacman_path[x_l,y_l] = cost_l, p_l
        else:
            pass
        if ([x_u, y_u] not in closed_nodes):
            pacman_path[x_u,y_u] = cost_u, p_u
        else:
            pass
        if ([x_d, y_d] not in closed_nodes):
            pacman_path[x_d,y_d] = cost_d, p_d
        else:
            pass
        pacman_path.pop(current_pacman_location)
        pacman_path = {k: v for k, v in sorted(pacman_path.items(), key=lambda item: item[1])}  
        current_pacman_location = list(pacman_path.keys())[0]   
        current_cost = list(pacman_path.values())[0][0]
        current_path = list(pacman_path.values())[0][1]
        if len(current_path) > 20:
            if (([pacman_start[0] + 1, pacman_start[1]]) not in closed_nodes):
                pacman_start = (pacman_start[0] + 1, pacman_start[1])
                open_nodes[pacman_start] = 0
                return 'R', pacman_start
            elif (([pacman_start[0] - 1, pacman_start[1]]) not in closed_nodes):
                pacman_start = (pacman_start[0] - 1, pacman_start[1])
                open_nodes[pacman_start] = 0
                return 'L', pacman_start
            elif (([pacman_start[0], pacman_start[1] - 1]) not in closed_nodes):
                pacman_start = (pacman_start[0], pacman_start[1] - 1)
                open_nodes[pacman_start] = 0
                return 'U', pacman_start
            elif (([pacman_start[0], pacman_start[1] + 1]) not in closed_nodes):
                pacman_start = (pacman_start[0], pacman_start[1] + 1)
                open_nodes[pacman_start] = 0
                return 'D', pacman_start
    if current_path[0] == 'R':
        pacman_start = (pacman_start[0] + 1, pacman_start[1])
        open_nodes[pacman_start] = 0
        return current_path[0], pacman_start
    elif current_path[0] == 'L':
        pacman_start = (pacman_start[0] - 1, pacman_start[1])
        open_nodes[pacman_start] = 0
        return current_path[0], pacman_start
    elif current_path[0] == 'U':
        pacman_start = (pacman_start[0], pacman_start[1] - 1)
        open_nodes[pacman_start] = 0
        return current_path[0], pacman_start
    elif current_path[0] == 'D':
        pacman_start = (pacman_start[0], pacman_start[1] + 1)
        open_nodes[pacman_start] = 0
        return current_path[0], pacman_start
    
def RedGhost(current_red_location, current_pacman_location):
    goal = current_pacman_location
    current_cost = 0
    current_path = ''
    red_path = {current_red_location : (current_cost,current_path)}
    red_start = current_red_location
    while (current_red_location[1] != goal[1]) or (current_red_location[0] != goal[0]):
        x_r, y_r, cost_r, p_r, x_l, y_l, cost_l, p_l, x_u, y_u, cost_u, p_u, x_d, y_d, cost_d, p_d = MoveAround(current_red_location[0], current_red_location[1], current_cost, current_path)
        if ([x_r, y_r] in open_check):
            red_path[x_r,y_r] = cost_r,p_r
        else:
            pass
        if ([x_l, y_l]  in open_check):
            red_path[x_l,y_l] = cost_l, p_l
        else:
            pass
        if ([x_u, y_u] in open_check):
            red_path[x_u,y_u] = cost_u, p_u
        else:
            pass
        if ([x_d, y_d] in open_check):
            red_path[x_d,y_d] = cost_d, p_d
        else:
            pass
        red_path.pop(current_red_location)
        red_path = {k: v for k, v in sorted(red_path.items(), key=lambda item: item[1])}   
        current_red_location = list(red_path.keys())[0]   
        current_cost = list(red_path.values())[0][0]
        current_path = list(red_path.values())[0][1]
    closed_nodes.remove([red_start[0], red_start[1]])
    if current_path[0] == 'R':
        red_start = (red_start[0] + 1, red_start[1])
        closed_nodes.append([red_start[0], red_start[1]])
        return current_path[0], red_start
    elif current_path[0] == 'L':
        red_start = (red_start[0] - 1, red_start[1])
        closed_nodes.append([red_start[0], red_start[1]])
        return current_path[0], red_start
    elif current_path[0] == 'U':
        red_start = (red_start[0], red_start[1] - 1)
        closed_nodes.append([red_start[0], red_start[1]])
        return current_path[0], red_start
    elif current_path[0] == 'D':
        red_start = (red_start[0], red_start[1] + 1)
        closed_nodes.append([red_start[0], red_start[1]])
        return current_path[0], red_start
    
def CheckNodes(current_position):
    if (([current_position[0] + 1, current_position[1]]) in open_check and ([current_position[0] - 1, current_position[1]]) in open_check and ([current_position[0], current_position[1] - 1]) in open_check) or (([current_position[0] + 1, current_position[1]]) in open_check and ([current_position[0] - 1, current_position[1]]) in open_check and ([current_position[0], current_position[1] + 1]) in open_check) or (([current_position[0] + 1, current_position[1]]) in open_check and ([current_position[0], current_position[1] - 1]) in open_check and ([current_position[0], current_position[1] + 1]) in open_check) or (([current_position[0] - 1, current_position[1]]) in open_check and ([current_position[0], current_position[1] - 1]) in open_check and ([current_position[0], current_position[1] + 1]) in open_check) or (([current_position[0] + 1, current_position[1]]) in open_check and ([current_position[0] - 1, current_position[1]]) in open_check and ([current_position[0], current_position[1] - 1]) in open_check and ([current_position[0], current_position[1] + 1]) in open_check):
        return True
    else:
        return False
    
def OrangeGhost(current_orange_location, current_pacman_location, current_orange_path):
    current_cost = 0
    current_path = ''
    orange_path = {current_orange_location : (current_cost,current_path)}
    orange_start = current_orange_location
    if CheckNodes(current_orange_location) == False:
        closed_nodes.remove([orange_start[0], orange_start[1]])
        if current_orange_path == 'R':
            if ([orange_start[0] + 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] + 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'R', orange_start
            elif ([orange_start[0], orange_start[1] - 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] - 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'U', orange_start
            elif ([orange_start[0], orange_start[1] + 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] + 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'D', orange_start     
        elif current_orange_path == 'L':
            if ([orange_start[0] - 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] - 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'L', orange_start
            elif ([orange_start[0], orange_start[1] - 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] - 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'U', orange_start
            elif ([orange_start[0], orange_start[1] + 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] + 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'D', orange_start  
        elif current_orange_path == 'U':
            if ([orange_start[0] - 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] - 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'L', orange_start
            elif ([orange_start[0], orange_start[1] - 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] - 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'U', orange_start
            elif ([orange_start[0] + 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] + 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'R', orange_start  
        elif current_orange_path == 'D':
            if ([orange_start[0] - 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] - 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'L', orange_start
            elif ([orange_start[0] + 1, orange_start[1]]) in open_check:
                orange_start = (orange_start[0] + 1, orange_start[1])
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'R', orange_start
            elif ([orange_start[0], orange_start[1] + 1]) in open_check:
                orange_start = (orange_start[0], orange_start[1] + 1)
                closed_nodes.append([orange_start[0], orange_start[1]])
                return 'D', orange_start  
    else:
        if ((abs(current_orange_location[0] - current_pacman_location[0]) + abs(current_orange_location[1] - current_pacman_location[1])) > 16):
            goal = current_pacman_location
        elif (current_pacman_location[1] <= 11):
            goal = (1,21)
        else:
            goal = (17,1)
        while (current_orange_location[1] != goal[1]) or (current_orange_location[0] != goal[0]):
            x_r, y_r, cost_r, p_r, x_l, y_l, cost_l, p_l, x_u, y_u, cost_u, p_u, x_d, y_d, cost_d, p_d = MoveAround(current_orange_location[0], current_orange_location[1], current_cost, current_path)
            if ([x_r, y_r] in open_check):
                orange_path[x_r,y_r] = cost_r,p_r
            else:
                pass
            if ([x_l, y_l] in open_check):
                orange_path[x_l,y_l] = cost_l, p_l
            else:
                pass
            if ([x_u, y_u] in open_check):
                orange_path[x_u,y_u] = cost_u, p_u
            else:
                pass
            if ([x_d, y_d] in open_check):
                orange_path[x_d,y_d] = cost_d, p_d
            else:
                pass
            orange_path.pop(current_orange_location)
            orange_path = {k: v for k, v in sorted(orange_path.items(), key=lambda item: item[1])}   
            current_orange_location = list(orange_path.keys())[0]   
            current_cost = list(orange_path.values())[0][0]
            current_path = list(orange_path.values())[0][1]
        closed_nodes.remove([orange_start[0], orange_start[1]])
        if current_path[0] == 'R':
            orange_start = (orange_start[0] + 1, orange_start[1])
            closed_nodes.append([orange_start[0], orange_start[1]])
            return current_path[0], orange_start
        elif current_path[0] == 'L':
            orange_start = (orange_start[0] - 1, orange_start[1])
            closed_nodes.append([orange_start[0], orange_start[1]])
            return current_path[0], orange_start
        elif current_path[0] == 'U':
            orange_start = (orange_start[0], orange_start[1] - 1)
            closed_nodes.append([orange_start[0], orange_start[1]])
            return current_path[0], orange_start
        elif current_path[0] == 'D':
            orange_start = (orange_start[0], orange_start[1] + 1)
            closed_nodes.append([orange_start[0], orange_start[1]])
            return current_path[0], orange_start

def BlueGhost(current_blue_location, current_pacman_location, current_blue_path):
    current_cost = 0
    current_path = ''
    blue_path = {current_blue_location : (current_cost,current_path)}
    blue_start = current_blue_location
    if CheckNodes(current_blue_location) == False:
        closed_nodes.remove([blue_start[0], blue_start[1]])
        if current_blue_path == 'R':
            if ([blue_start[0] + 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] + 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'R', blue_start
            elif ([blue_start[0], blue_start[1] - 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] - 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'U', blue_start
            elif ([blue_start[0], blue_start[1] + 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] + 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'D', blue_start     
        elif current_blue_path == 'L':
            if ([blue_start[0] - 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] - 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'L', blue_start
            elif ([blue_start[0], blue_start[1] - 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] - 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'U', blue_start
            elif ([blue_start[0], blue_start[1] + 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] + 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'D', blue_start  
        elif current_blue_path == 'U':
            if ([blue_start[0] - 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] - 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'L', blue_start
            elif ([blue_start[0], blue_start[1] - 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] - 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'U', blue_start
            elif ([blue_start[0] + 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] + 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'R', blue_start  
        elif current_blue_path == 'D':
            if ([blue_start[0] - 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] - 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'L', blue_start
            elif ([blue_start[0] + 1, blue_start[1]]) in open_check:
                blue_start = (blue_start[0] + 1, blue_start[1])
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'R', blue_start
            elif ([blue_start[0], blue_start[1] + 1]) in open_check:
                blue_start = (blue_start[0], blue_start[1] + 1)
                closed_nodes.append([blue_start[0], blue_start[1]])
                return 'D', blue_start  
    else:
        open_check.remove([blue_start[0], blue_start[1]])
        goal = random.choice(open_check)
        open_check.append([blue_start[0], blue_start[1]])
        while (current_blue_location[1] != goal[1]) or (current_blue_location[0] != goal[0]):
            x_r, y_r, cost_r, p_r, x_l, y_l, cost_l, p_l, x_u, y_u, cost_u, p_u, x_d, y_d, cost_d, p_d = MoveAround(current_blue_location[0], current_blue_location[1], current_cost, current_path)
            if ([x_r, y_r] in open_check):
                blue_path[x_r,y_r] = cost_r,p_r
            else:
                pass
            if ([x_l, y_l] in open_check):
                blue_path[x_l,y_l] = cost_l, p_l
            else:
                pass
            if ([x_u, y_u] in open_check):
                blue_path[x_u,y_u] = cost_u, p_u
            else:
                pass
            if ([x_d, y_d] in open_check):
                blue_path[x_d,y_d] = cost_d, p_d
            else:
                pass
            blue_path.pop(current_blue_location)
            blue_path = {k: v for k, v in sorted(blue_path.items(), key=lambda item: item[1])}   
            current_blue_location = list(blue_path.keys())[0]   
            current_cost = list(blue_path.values())[0][0]
            current_path = list(blue_path.values())[0][1]
        closed_nodes.remove([blue_start[0], blue_start[1]])
        if current_path[0] == 'R':
            blue_start = (blue_start[0] + 1, blue_start[1])
            closed_nodes.append([blue_start[0], blue_start[1]])
            return current_path[0], blue_start
        elif current_path[0] == 'L':
            blue_start = (blue_start[0] - 1, blue_start[1])
            closed_nodes.append([blue_start[0], blue_start[1]])
            return current_path[0], blue_start
        elif current_path[0] == 'U':
            blue_start = (blue_start[0], blue_start[1] - 1)
            closed_nodes.append([blue_start[0], blue_start[1]])
            return current_path[0], blue_start
        elif current_path[0] == 'D':
            blue_start = (blue_start[0], blue_start[1] + 1)
            closed_nodes.append([blue_start[0], blue_start[1]])
            return current_path[0], blue_start


simulations = 0
win = 0
lose = 0
win_scores = []
lose_scores = []
while simulations < 100:
    print("Simulation #", simulations+1)
    open_nodes = {}
    open_check = []
    closed_nodes = []
    i = 1
    for m in range(0,rows):
        for n in range(0,cols):
            if map_image[m,n] != 255:
                open_nodes[n,m] = 1
                open_check.append([n,m])
            else:
                closed_nodes.append([n,m])           
    open_nodes[9,10] = 0
    open_nodes[8,11] = 0
    open_nodes[7,11] = 0
    open_nodes[11,11] = 0
    open_nodes[9,11] = 0
    open_nodes[9,12] = 0
    open_nodes[10,11] = 0
    open_nodes[1,1] = 0
    open_nodes[9,9] = 0
    start_x = 1
    start_y = 1
    current_pacman_location = (start_x, start_y) # CHANGE START POSITION
    current_red_location = (9,9)
    current_orange_location = (9,11)
    current_blue_location = (9,11)
    closed_nodes.append([current_red_location[0], current_red_location[1]])
    closed_nodes.append([current_orange_location[0], current_orange_location[1]])
    closed_nodes.append([current_blue_location[0], current_blue_location[1]])
    overall_red_path = ''
    overall_orange_path = ''
    overall_blue_path = ''
    overall_path = ''
    orange_path = ''
    blue_path = ''
    total_moves = 0
    while any(value == 1 for value in open_nodes.values()):
        red_path, current_red_location = RedGhost(current_red_location,current_pacman_location)
        overall_red_path += red_path
        # print('red',red_path,current_red_location)
        orange_path, current_orange_location = OrangeGhost(current_orange_location,current_pacman_location,orange_path)
        overall_orange_path += orange_path
        # print('orange',orange_path, current_orange_location)
        blue_path, current_blue_location = BlueGhost(current_blue_location,current_pacman_location,blue_path)
        overall_blue_path += blue_path
        # print('blue',blue_path,current_blue_location)
        pacman_path, current_pacman_location = PacmanPath(current_pacman_location)
        overall_path += pacman_path
        total_moves += 1
        # print('pacman',pacman_path,current_pacman_location)  
        
        if (current_red_location == current_pacman_location) or (current_orange_location == current_pacman_location) or (current_blue_location == current_pacman_location):
            print('Game over. You lose.')
            print('Total moves before failure: ', total_moves)
            lose_scores.append(total_moves)
            lose += 1
            break  
       
        if all(value == 0 for value in open_nodes.values()):
            print("Game over. You win!")
            print('Total moves before victory: ', total_moves)
            win_scores.append(total_moves)
            win += 1
            break
    simulations += 1

win_average = mean(win_scores)
lose_average = mean(lose_scores)
print("After 100 simulations, Pacman won ", win, " times and lost ", lose, " times.")
print("The average winning score was ", win_average)
print("The average losing score was ", lose_average)

labels = 'Wins', 'Losses'
sizes = [win, lose]
fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()