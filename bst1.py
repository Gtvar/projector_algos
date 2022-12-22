from avl import *
from random import seed
from random import randint
import time
import psutil
import os
import tracemalloc

def makeset(max):
    set = []
    for _ in range(max):
        set.append(randint(0, max))

    return set

def calcTimeExecution(action, startTime, print = 0):
    resultTime = (time.time() - startTime) * 1000
    if print:
        print("--- %s for %s miliseconds ---" % (action, resultTime))

    return resultTime

def calcMemory():
    return tracemalloc.get_traced_memory()

def measureComplexity(countDatasets = 1, maxNumber = 10000, print = 0):
    createTimeMs = 0
    findTime = 0
    deleteTime = 0
    insertTime = 0
    memoryForInsert = 0

    for _ in range(countDatasets):
        set = makeset(maxNumber)
        myTree = AVL_Tree()
        root = None

        start_time = time.time()
        tracemalloc.start()
        for key in set:
          root = myTree.insert(root, key)
        allMemory, peakMemory = calcMemory()
        memoryForInsert += peakMemory
        tracemalloc.stop()

        createTimeMs += calcTimeExecution('Create', start_time, print)

        start_time = time.time()
        find = myTree.find(root, 100)
        findTime += calcTimeExecution('Find', start_time, print)

        start_time = time.time()
        delete = myTree.delete(root, 100)
        deleteTime += calcTimeExecution('Delete', start_time, print)

        start_time = time.time()
        delete = myTree.insert(root, 100)
        insertTime += calcTimeExecution('Insert', start_time, print)

    return createTimeMs, findTime, deleteTime, insertTime, memoryForInsert

countDatasets = 10
maxNumber = 1000
createTimeMs, findTime, deleteTime, insertTime, memoryForInsert = measureComplexity(countDatasets, maxNumber)

print("--- Total result for %s datasets with %s max numbers ---" % (countDatasets, maxNumber))
print("--- Average Time ms ---")
print("--- Create %s Find %s Delete %s Insert %s ---" % (createTimeMs/countDatasets, findTime/countDatasets, deleteTime/countDatasets, insertTime/countDatasets))
print("--- Peak memory Average Mb ---")
print("--- Create %s ---" % (memoryForInsert/(1024*1024)/countDatasets))
