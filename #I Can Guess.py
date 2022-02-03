#I Can Guess

from sys import stdin, stdout
from queue import PriorityQueue

while True:
    try:
        entradas = int(input()) 

        stack = []
        queue = []
        priority = PriorityQueue()

        esQueue = True
        esStack = True
        esPriority = True
        tamaño = 0
        for i in range(entradas):
            linea = list(map(int, input().split()))
            if linea[0] == 1:
                if esStack:
                    stack.append(linea[1])
                if esQueue:
                    queue.append(linea[1])
                if esPriority:
                    priority.put((linea[1]*-1))   
                tamaño = tamaño + 1
            elif linea[0] == 2:
                if tamaño == 0:
                    esPriority = esQueue = esStack = False
                else:
                    if esPriority and (priority.get()*-1) != linea[1]:
                        esPriority = False
                    if esQueue and queue.pop(0) != linea[1]:
                        esQueue = False
                    if esStack and stack.pop() != linea[1]:
                        esStack = False
                tamaño = tamaño - 1
        
        if ((not esStack) and (not esQueue) and (not esPriority)):
            print ("impossible")
        elif ((esStack) and (not esQueue) and (not esPriority)):
            print ("stack")
        elif ((not esStack) and (not esQueue) and (esPriority)):
            print ("priority queue")
        elif ((not esStack) and (esQueue) and (not esPriority)):
            print ("queue")
        else:
            print("not sure")

    except(EOFError):
        break