from ht import HashTable

ht = HashTable(8)

def intersection(arrays):
    cache = {}
    matches = []
    arr_iter = iter(arrays[0])
    for item in arr_iter:
        ht.put(str(item), item)
    for i in range(1,len(arrays)):
        arr_iter = iter(arrays[i])
        for item in arr_iter:
            if ht.get(str(item)):
                cache[item] = cache.get(item,0) + 1
    for i in cache:
        if cache[i] == len(arrays)-1:
            matches.append(i)
    return matches


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
