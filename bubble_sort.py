import random

# initialize list to be sorted
listLength = 10

sortingList = []
originalList = []

i = 0
while(i < listLength):
    tempRandom = random.randint(0, 100)

    sortingList.append(tempRandom)
    originalList.append(tempRandom)

    i = i + 1


# sorting
i = 0
while(i < listLength - 1):
    j = 0
    while(j < listLength - 1 - i):
        if(sortingList[j] > sortingList[j+1]):
            tempInt = sortingList[j+1]
            sortingList[j+1] = sortingList[j]
            sortingList[j] = tempInt

        j = j + 1
    i = i + 1


# print the sorted list
print('Original\tSorted')

i = 0
while (i < listLength):
    print('%d\t%d' % (originalList[i], sortingList[i]))

    i = i + 1
