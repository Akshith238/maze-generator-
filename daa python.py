import pygame
import time
import random
import sys

WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
GREEN = (0,255,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

w = 20      
grid = []      
visited = []
stack = []

def draw_grid(x, y, w):
    for i in range(1, 19):
        x = 20      
        y += 20     
        for j in range(1, 19):
            pygame.draw.line(screen, WHITE, (x, y), (x+w, y))  
            pygame.draw.line(screen, WHITE, (x+w, y), (x+w, y+w))    
            pygame.draw.line(screen, WHITE, (x+w, y+w), (x, y+w))  
            pygame.draw.line(screen, WHITE, (x, y+w), (x, y))   
            grid.append((x, y))
            x += 20    
            pygame.display.update()

def move_up(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y-w+1, 19, 39), 0)
    pygame.display.update()

def move_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def move_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def move_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def carve_maze(x, y):
    single_cell(x, y)       
    stack.append((x, y))    
    visited.append((x, y))  
    while len(stack) > 0:
        time.sleep(0.09)
        cell = []
    
        if (x, y - w) not in visited and (x, y - w) in grid:    
            cell.append("top")

        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("right")

        if(x, y + w) not in visited and (x, y + w) in grid:
            cell.append("bottom")

        if(x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")
        
        if len(cell) > 0:
            next_cell = random.choice(cell)

            if next_cell == "top":
                move_up(x, y)
                y -= w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "right":
                move_right(x, y)
                x += w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "bottom":
                move_down(x, y)
                y += w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "left":
                move_left(x, y)
                x -= w
                visited.append((x, y))
                stack.append((x, y))
        
        else:
            x, y = stack.pop()     
            single_cell(x, y)       
            time.sleep(0.09)
            backtracking_cell(x, y)      
     
x,y=20,20

draw_grid(20, 0, 20)
carve_maze(x, y) 


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()