import numpy as np

limit = 10
count = 0
vector = np.empty(limit, dtype=int)


def insertion_in_a_ordered_vector(value: int) -> None:
    global vector, limit, count
    count += 1
    value = value
    max = float('-inf')
    ind = 0
    for index, num in enumerate(vector):  # O(n)  -> Linear: best case
        if num > value:
            for i in range(index, len(vector) - 1):  # O(n2) -> Quadratic worth case
                aux = vector[i]  # 4
                vector[i] = value  # 3
                value = aux  # 4
                y = i
            limit += 1
            vector.resize(limit + 1, refcheck=False)
            print(f"Updated vector: {vector.tolist()[:count]}")
            return
        else:
            if num >= max:
                max = num
                ind = index
    limit += 1
    vector.resize(limit + 1, refcheck=False)
    vector[ind + 1] = value
    print(f"Updated vector: {vector.tolist()[:count]}")


insertion_in_a_ordered_vector(0)
insertion_in_a_ordered_vector(9)
insertion_in_a_ordered_vector(3)
insertion_in_a_ordered_vector(1)

