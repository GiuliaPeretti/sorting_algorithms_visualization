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
    buttons.append({'name': 'Gnome sort' , 'coordinates': (x,y,w,h)})
    x,y=x+w+10, 20
    buttons.append({'name': 'Smooth sort', 'coordinates': (x,y,w,h)})
    y=y+h+10
    buttons.append({'name': 'Strand sort' , 'coordinates': (x,y,w,h)})
    x,y=x+w+10, 20
    buttons.append({'name': '', 'coordinates': (x,y,w,h)})
    y=y+h+10
    # buttons.append({'name': 'Set Delay' , 'coordinates': (x,y,w,h)})
    return(buttons)

def draw_buttons():   
    for b in buttons[:len(buttons)-1]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+5,b['coordinates'][1]+3))
    
    b=buttons[-1]
    pygame.draw.rect(screen, WHITE, b['coordinates'])
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

def select_algo(n, d):
    match n:
        case 0:
            bubbleSort(d)
        case 1:
            insertionSort(d)
        case 2:
            selectionSort(d)
        case 3:
            quickSort(0,99, d)
        case 4:
            mergeSort(0,99, d)
        case 5:
            gnomeSort(d)
        case 6:
            smooth_sort(d)
        case 7:
            pancakeSort(d)

def visualize_list():
    draw_square()
    x,w=20,5
    for i in range(len(l)):
        x=x+2
        pygame.draw.rect(screen, PINK, (x,620-l[i]*5.1,w,l[i]*5.1))
        x=x+6
    pygame.display.flip()

def bubbleSort(d):
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if l[j] > l[j + 1]:
                swapped = True
                l[j], l[j + 1] = l[j + 1], l[j]
                visualize_list()
                pygame.time.delay(d)
        if not swapped:
            return

def insertionSort(d):
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
            pygame.time.delay(d)
        l[j+1] = key  
  
def selectionSort(d):
    n = len(l)
    for ind in range(n):
        min_index = ind
        for j in range(ind + 1, n):
            if l[j] < l[min_index]:
                min_index = j
        (l[ind], l[min_index]) = (l[min_index], l[ind])
        visualize_list()
        pygame.time.delay(d)

def partition(low, high, d):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= pivot:
            i = i + 1
            (l[i], l[j]) = (l[j], l[i])
            visualize_list()
            pygame.time.delay(d)
    (l[i + 1], l[high]) = (l[high], l[i + 1])
    visualize_list()
    pygame.time.delay(d)
    return i + 1

def quickSort(low, high, d):
    if low < high:
        pi = partition(low, high, d)
        quickSort(low, pi - 1, d)
        quickSort(pi + 1, high, d)

def merge1(left, m, right,d):
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
    pygame.time.delay(d)
 
def mergeSort(left, right,d):
    if left < right:
        m = left+(right-left)//2
        mergeSort(left, m,d)
        mergeSort(m+1, right,d)
        merge1(left, m, right,d)

def gnomeSort(d):
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
        pygame.time.delay(d)

def smooth_sort(d):
    n = len(l)

    def leonardo(k):
        if k < 2:
            return 1
        return leonardo(k - 1) + leonardo(k - 2) + 1
 
    def heapify(start, end):
        i = start
        j = 0
        k = 0
        while k < end - start + 1:
            if k & 0xAAAAAAAA:
                j = j + i
                i = i >> 1
            else:
                i = i + j
                j = j >> 1
            k = k + 1
        while i > 0:
            j = j >> 1
            k = i + j
            while k < end:
                if l[k] > l[k - i]:
                    break
                l[k], l[k - i] = l[k - i], l[k]
                k = k + i
            i = j
    p = n - 1
    q = p
    r = 0
    while p > 0:
        if (r & 0x03) == 0:
            heapify(r, q)
        if leonardo(r) == p:
            r = r + 1
        else:
            r = r - 1
            q = q - leonardo(r)
            heapify(r, q)
            q = r - 1
            r = r + 1
        l[0], l[p] = l[p], l[0]
        visualize_list()
        pygame.time.delay(d)
        p = p - 1
    for i in range(n - 1):
        j = i + 1
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
            visualize_list()
            pygame.time.delay(5)

def flip(arr, i, d):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
        visualize_list()
        pygame.time.delay(d)

def findMax(arr, n, d):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
            visualize_list()
            pygame.time.delay(d)
    return mi

def pancakeSort(d):
    curr_size = len(l)
    while curr_size > 1:
        mi = findMax(l, curr_size)
        if mi != curr_size-1:
            flip(l, mi)
            flip(l, curr_size-1)
            visualize_list()
            pygame.time.delay(d)
        curr_size -= 1



if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Sorting visualizer♥')
    font = pygame.font.SysFont('arial', 20)

    current_delay=1
    delay=''
    selected=-1
    buttons=gen_buttons()
    draw_background()
    draw_buttons()
    draw_square()



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
                            l=gen_list()
                            visualize_list()
                            draw_buttons()
                            select_algo(selected, current_delay)
                            break
                else:
                    selected=-1
                    draw_buttons()

            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_BACKSPACE and buttons[-1]['name']!='' and selected==8:
                    buttons[-1]['name'] = buttons[-1]['name'][:-1]
                    draw_buttons()
                elif(event.key == pygame.K_RETURN) and buttons[-1]['name']!=''  and selected==8:
                    current_delay=int(buttons[-1]['name'])
                    buttons[-1]['name']=''
                    selected=-1
                    draw_buttons()
                elif(selected==8):
                    for i in range(len(INPUTS)):
                        if (event.key==INPUTS[i]):
                            buttons[-1]['name']=buttons[-1]['name']+str(i+1)
                            draw_buttons()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()