def selection_sort(list_name):
    for i in range(len(list_name) - 1):
        min_val = i
        for j in range(i + 1, len(list_name)):
            if list_name[j] < list_name[min_val]:
                min_val = j

        if min_val != i:  # Corrected the variable name from "min" to "min_val"
            temp = list_name[i]
            list_name[i] = list_name[min_val]
            list_name[min_val] = temp

    return list_name


l_1 = [2, 5, 1, 8, 3, 20, 6, 10, 23, 4, 14]
selection_sort(l_1)
print(l_1)


def binary_search(list_name, val):
    N = len(list_name)
    resultOk = False
    first = 0
    last = N - 1

    while first <= last:
        mid = (first + last) // 2

        if val == list_name[mid]:
            resultOk = True
            break
        elif val > list_name[mid]:
            first = mid + 1
        else:
            last = mid - 1

    if resultOk:
        print(f'\033[92m{val} was found!\033[0m')
    else:
        print(f'\033[91m{val} was not found!\033[0m')


for k in range(25):
    binary_search(l_1, k)
