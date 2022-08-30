
def bubble_sort(list1):

    for i in range(0, len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return print(list1)


def binary_search(data, elem):
    bubble_sort(data)
    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high) // 2

        if data[middle] == elem:
            return print(f"Элемент  найден {data[middle]}" )
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return print("Элемент не найден")

binary_search(data=[1,22,54,43,23,15,41,80],elem= 54 )