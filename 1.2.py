count = int(input("введите количество элементов массива: "))
array = []
for i in range(count):
    element = float(input())
    array.append(element)

maxElement = max(array)
indexMaxElement = array.index(maxElement)
countElementsSlice = len(array[indexMaxElement+1:len(array)])
array[indexMaxElement+1:len(array)] = [0] * countElementsSlice


print(array)