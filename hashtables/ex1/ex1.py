def get_indices_of_item_weights(weights, length, limit):
    wt = {}
    for i in range(len(weights)):
        if limit - weights[i] >= 0:
            wt[i] = limit - weights[i]
    print(wt)
    return None


get_indices_of_item_weights([9], 1, 9)
get_indices_of_item_weights([4,4], 2, 8)
get_indices_of_item_weights([4,6,10,15,16], 5, 21)
get_indices_of_item_weights([12,6,7,14,19,3,0,25,40], 9, 7)