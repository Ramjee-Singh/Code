def subset(array, curr_index, result):

    if curr_index  == len(array):
        print("Result 2", result)
        return  
    result.append(array[curr_index])
    subset(array, curr_index + 1, result)
    result.pop()
    subset(array, curr_index + 1, result)



set = [int(item) for item in input("Enter the items separated by space : ").split()]
result=[]
subset(set, 0, result)    




