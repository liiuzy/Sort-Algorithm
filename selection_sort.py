import random

# initialize list to be sorted
listLength = 100

sortingList = []
originalList = []

i = 0
while(i < listLength):
    temp = random.randint(0, 100)

    sortingList.append(temp)
    originalList.append(temp)

    i = i+1


# sorting
minIndex = 0
i = 0
j = 0

while(i < listLength):
    minIndex = i

    j = i + 1
    while(j < listLength):
        if(sortingList[j] < sortingList[minIndex]):
            minIndex = j

        j = j + 1

    temp = sortingList[i]
    sortingList[i] = sortingList[minIndex]
    sortingList[minIndex] = temp

    i = i + 1


# print the sorted list
print('Original\tSorted')

i = 0
while (i < listLength):
    print('%d\t%d' % (originalList[i], sortingList[i]))

    i = i + 1
