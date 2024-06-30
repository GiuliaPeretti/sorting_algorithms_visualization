import pygame
from settings import *
import numpy as np


def draw_background():
    screen.fill(BACKGROUND_COLOR)

def gen_buttons():
    x,y,w,h=20,20,150,30
    buttons=[]
    buttons.append({'name': 'Bubble sort', 'coordinates': (x,y,w,h)})
    y=y+h+10
    buttons.append({'name': 'Quicksort', 'coordinates': (x,y,w,h)})
    return(buttons)

def draw_buttons():   
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+17,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+17,buttons[selected]['coordinates'][1]+3))  
    pygame.display.flip()
    
def init_cell(size):
    cells=[]
    for i in range (size):
        t=[]
        for j in range(size):
            t.append(0)
        cells.append(t)
    return(cells)

def draw_square():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (20,110,600,600))
    pygame.draw.line(screen, WHITE, (20,110),(20,620), 2)
    pygame.draw.line(screen, WHITE, (20,110),(820,110), 2)
    pygame.draw.line(screen, WHITE, (20,620),(820,620), 2)
    pygame.draw.line(screen, WHITE, (820,110),(820,620), 2)

def gen_list():
    l=np.random.randint(0,100, size=100)
    return(l)

def select_algo(n):
    if n==0:
        bubble()
    pass

def bubble():
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if l[j] > l[j + 1]:
                swapped = True
                l[j], l[j + 1] = l[j + 1], l[j]
        if not swapped:
            return


def visualize_list():
    x,y,w=20,22,5
    print(l)
    for i in range(len(l)):
        x=x+2
        pygame.draw.rect(screen, PINK, (x,620-l[i]*5.1,w,l[i]*5.1))
        x=x+6

if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Sorting visualizer♥')
    font = pygame.font.SysFont('arial', 20)

    selected=-1
    buttons=gen_buttons()
    draw_background()
    draw_buttons()
    draw_square()
    l=gen_list()
    visualize_list()

    run  = True

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                for i in range (len(buttons)):
                    if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                        if(i<len(buttons)):
                            selected=i
                            draw_buttons()
                            select_algo(selected)
                            break
                else:
                    selected=-1
                    draw_buttons()








        pygame.display.flip()
        clock.tick(30)
    pygame.quit()