def rabbit_pairs(n, k):
    array = [1,1]
    start = 0
    end = 1

    
    for i in range(n-2):
        next_num = array[end] + (k * array[start])
        array.append(next_num)
        start += 1
        end += 1
        

    print(array[-1])
    return array[-1]


rabbit_pairs(28,5)
