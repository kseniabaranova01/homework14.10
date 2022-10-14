def creatingArray():
    count = int(input("введите количество элементов массива: "))
    array = []
    for i in range(count):
        element = float(input())
        array.append(element)
    return array


def getArrayCommon():
    firstArray = creatingArray()
    secondArray = creatingArray()
    arrayCommon = []
    for i in firstArray:
        if i in secondArray:
            arrayCommon.append(i)
    return arrayCommon


def getArrayCommonIfForDifferent():
    firstArray = creatingArray()
    secondArray = creatingArray()
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
    return ""


print(getArrayCommon())
getArrayCommonIfForDifferent()
