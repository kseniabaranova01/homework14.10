count = int(input("введите количество элементов массива A: "))
firstArray = []
for i in range(count):
    element = float(input())
    firstArray.append(element)

count = int(input("введите количество элементов массива B: "))
secondArray = []
for i in range(count):
        element = float(input())
        secondArray.append(element)
        arrayCommon = []
for i in firstArray:
    if i in secondArray:
        arrayCommon.append(i)

    print("Для обоих массивов:")
    print(arrayCommon)


    arrayCommonForFirstArray = []
    arrayCommonForSecondArray = []
    for a in firstArray:
        if a in secondArray:
            arrayCommonForFirstArray.append(a)

    for b in secondArray:
        if b in firstArray:
            arrayCommonForSecondArray.append(b)

    print("Для массива А:")
    print(arrayCommonForFirstArray)
    print("Для массива B:")
    print(arrayCommonForSecondArray)
