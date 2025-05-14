#Линейный поиск и сложности алгоритмов

def search(arr, n):
    ind = 0
    for i in arr:
        if i == n:
            return ind
        ind += 1
    return -1

print(search([1, 2, 3, 50, 70], 70))
