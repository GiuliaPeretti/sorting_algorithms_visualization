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
    buttons.append({'name': 'Insertion sort', 'coordinates': (x,y,w,h)})
    x,y=x+w+10, 20
    buttons.append({'name': 'Selection sort', 'coordinates': (x,y,w,h)})
    y=y+h+10
    buttons.append({'name': 'Quicksort', 'coordinates': (x,y,w,h)})
    x,y=x+w+10, 20
    buttons.append({'name': 'Merge sort', 'coordinates': (x,y,w,h)})
    y=y+h+10
    buttons.append({'name': 'Patience sort' , 'coordinates': (x,y,w,h)})
    return(buttons)

def draw_buttons():   
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+5,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, LIGHT_PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+5,buttons[selected]['coordinates'][1]+3))  
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
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0,110,840,640))
    pygame.draw.line(screen, WHITE, (20,110),(20,620), 2)
    pygame.draw.line(screen, WHITE, (20,110),(820,110), 2)
    pygame.draw.line(screen, WHITE, (20,620),(820,620), 2)
    pygame.draw.line(screen, WHITE, (820,110),(820,620), 2)

def gen_list():
    l=np.random.randint(0,100, size=100)
    return(l)

def select_algo(n):
    match n:
        case 0:
            bubbleSort()
        case 1:
            insertionSort()
        case 2:
            selectionSort()
        case 3:
            quickSort(0,99)
        case 4:
            mergeSort(0,99)
        case 5:
            gnomeSort()

def visualize_list():
    draw_square()
    x,w=20,5
    for i in range(len(l)):
        x=x+2
        pygame.draw.rect(screen, PINK, (x,620-l[i]*5.1,w,l[i]*5.1))
        x=x+6
    pygame.display.flip()

def bubbleSort():
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if l[j] > l[j + 1]:
                swapped = True
                l[j], l[j + 1] = l[j + 1], l[j]
                visualize_list()
                pygame.time.delay(1)
        if not swapped:
            return

def insertionSort():
    n = len(l)
    if n <= 1:
        return  
    for i in range(1, n): 
        key = l[i] 
        j = i-1
        while j >= 0 and key < l[j]:  
            l[j+1] = l[j]  
            j -= 1
            visualize_list()
            pygame.time.delay(5)
        l[j+1] = key  
  
def selectionSort():
    n = len(l)
    for ind in range(n):
        min_index = ind
        for j in range(ind + 1, n):
            if l[j] < l[min_index]:
                min_index = j
        (l[ind], l[min_index]) = (l[min_index], l[ind])
        visualize_list()
        pygame.time.delay(10)

def partition(low, high):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= pivot:
            i = i + 1
            (l[i], l[j]) = (l[j], l[i])
            visualize_list()
            pygame.time.delay(5)
    (l[i + 1], l[high]) = (l[high], l[i + 1])
    visualize_list()
    pygame.time.delay(5)
    return i + 1

def quickSort(low, high):
    if low < high:
        pi = partition(low, high)
        quickSort(low, pi - 1)
        quickSort(pi + 1, high)

def merge(left, m, right):
    n1 = m - left + 1
    n2 = right - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = l[left + i]
    for j in range(0, n2):
        R[j] = l[m + 1 + j]
    i = 0  
    j = 0     
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        l[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        l[k] = R[j]
        j += 1
        k += 1
    visualize_list()
    pygame.time.delay(5)
 
def mergeSort(left, right):
    if left < right:
        m = left+(right-left)//2
        mergeSort(left, m)
        mergeSort(m+1, right)
        merge(left, m, right)

def gnomeSort():
    n=len(l)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if l[index] >= l[index - 1]:
            index = index + 1
        else:
            l[index], l[index - 1] = l[index - 1], l[index]
            index = index - 1
        visualize_list()
        pygame.time.delay(5)






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