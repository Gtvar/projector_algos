from avl import *
from random import seed
from random import randint
import time

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

def measureComplexity(countDatasets = 1, maxNumber = 10000, print = 0):
    createTimeMs = 0
    findTime = 0
    deleteTime = 0
    insertTime = 0

    for _ in range(countDatasets):
        set = makeset(maxNumber)
        myTree = AVL_Tree()
        root = None

        start_time = time.time()
        for key in set:
          root = myTree.insert(root, key)
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

    return createTimeMs, findTime, deleteTime, insertTime

countDatasets = 100
maxNumber = 10000
createTimeMs, findTime, deleteTime, insertTime = measureComplexity(countDatasets, maxNumber)

print("--- Total result for %s datasets with %s max numbers ---" % (countDatasets, maxNumber))
print("--- Average Time ms ---")
print("--- Create %s Find %s Delete %s Insert %s ---" % (createTimeMs/countDatasets, findTime/countDatasets, deleteTime/countDatasets, insertTime/countDatasets))
