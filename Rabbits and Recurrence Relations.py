def rabbit_pairs(n, k):
    # n = number of times sliding window will be repeated 
    # k = litter of each rabbit pair
    
    # Sliding window approch to run the fibbanachi sequence 
    array = [1,1]

    # Sliding window start and end positions
    start = 0
    end = 1

    # indexing n - 2 range as first two elements in array are always [1, 1]
    for i in range(n-2):
        # Recursion formula Fn = fn-1 + (k *fn-2 )
        next_num = array[end] + (k * array[start])
        array.append(next_num)
        # Slides window across 1
        start += 1
        end += 1
        

    print(array[-1])
    return array[-1]


rabbit_pairs(28,5)
