import random
import time
#Solution for N > 3
#1) Create a starting population (size = ?)
#2) Rank them (# of queens that attack each other? --> how to rank?)
#3) Randomly mate pairs --> (crossover, mutations (swapping, rates = ?))
#4) Kill some (keep the population size p. constant) --> which to kill off

#How can detect population not being very diverse
#Use permutations: set (2,1,0,3) <--- (ex) each index is a col, each value is a row
#Only 1 queen per row/col ^^^

#Need to iterate until find a soln+

def nextGen (popSort,N):
    x = 5*(N//5)
    for r in range (0, 5+x):
        eNum1 = random.randint(0, len(popSort) - 1)
        eNum2 = random.randint(0, len(popSort) - 1)
        popSort = crossover(popSort, N, eNum1, eNum2)

    for r in range (0, 5+x): # mutations
        eNum = random.randint(0, len(popSort) - 1)
        popSort = mutation(popSort, N, eNum)

    pSortN = sort (popSort, N)

    brk = int(len(pSortN)-len(pSortN)/3)

    pSortN = pSortN[0:brk]

    return pSortN




def crossover (popSort, N, eNum1, eNum2):
    pos = random.randint(0, N-1)
    e1 = popSort[eNum1][0]
    e2 = popSort[eNum2][0]

    newE1 = []
    newE2 = []

    for i in range(0, pos):
        newE1.append(e1[i])
        newE2.append(e2[i])

    for n in range (0, N):
        x = e2[n]
        if e2[n] not in newE1:
            newE1.append(e2[n])
        y = e1[n]
        if e1[n] not in newE2:
            newE2.append(e1[n])

    r1 = rank(newE1, N)
    r2 = rank(newE2, N)

    newElem1 = []
    newElem2 = []

    newElem1.append(newE1)
    newElem1.append(r1)
    newElem2.append(newE2)
    newElem2.append(r2)

    popSort.append(newElem1)
    popSort.append(newElem2)

    return popSort

def mutation (popSort, N, eNum):
    elem = popSort[eNum][0]
    tempSet = []
    newE = []
    for n in range(0, N):
        tempSet.append(n + 1)
        newE.append(elem[n])

    num1 = random.randint(0, N - 1)
    del tempSet[num1]
    num2 = random.randint(0, N - 2)
    del tempSet[num2]

    t = newE[num1]
    newE[num1] = newE[num2]
    newE[num2] = t

    r = rank(newE, N)
    newElem = []
    newElem.append(newE)
    newElem.append(r)

    popSort.append(newElem)
    return popSort

def sort(popRaw, N): #sorts & removes duplicates
    popSort = []

    popSort.append(popRaw[0])

    for i in range (1, len(popRaw)):
        val = popRaw[i][1]
        elem = popRaw[i][0]

        ins = False

        for x in range(0, len(popSort)):
            if popRaw[i] in popSort:
                ins = True
            elif val < popSort[x][1]:
                popSort.insert(x, popRaw[i])
                ins = True
                break
        if not ins:
            popSort.append(popRaw[i])

    return popSort

def rank (indv, N):

    numQAttack = 0

    for n in range (0, N):
        row = indv.index(n+1)
        col = n

        tempC = 0
        for i in  range (0, N):
            if i != n:
                nextR = indv.index(i+1)
                nextC = i
                if abs(nextR-row) == abs(nextC-col):
                    tempC+=1
        if tempC > 0:
            numQAttack += 1

    return numQAttack


def populate(N):
    popRaw = []

    # Creates random board
    for z in range(0, 30+N):
        tempSet = []
        for n in range(0, N):
            tempSet.append(n + 1)
        tempSoln = []
        for i in range(0, N):
            num = random.randint(0, N - 1 - i)
            tempSoln.append(tempSet[num])
            del tempSet[num]
        tempArr = []
        tempArr.append(tempSoln)
        tempArr.append(rank(tempSoln, N))
        popRaw.append(tempArr)

    return popRaw

def main():
    for iterT in range(0, 10):
        t1 = time.time()

        N = 4+iterT

        popRaw = populate(N)
        sortRaw = sort(popRaw, N)

        x = sortRaw[0][1]

        while x!=0 and sortRaw:
            sortRaw = nextGen(sortRaw, N)
            x = sortRaw[0][1]

        if sortRaw[0][1] == 0:
            print (N, '\t',(time.time() - t1))
        else:
            print (N, '\t',"Could not solve")






if __name__ =='__main__':
    main()
