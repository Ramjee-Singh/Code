def check(pos, size):
    for i in range(size + 1):
        for j in range(i+1, size + 1):
            if pos[i] == pos[j]:
                return False
            if pos[j] == pos[i] + (j-i):
                return False     
    return True        
            

def nQueen(pos, size, curr_row):
    if size  == curr_row:
        return True
    for i in range(size):
        pos[curr_row] = i
        if check(pos, curr_row) == False:
            pos[curr_row] = -1
        else:
            if nQueen(pos, size, curr_row + 1) == False:
                pos[curr_row] = -1
            else:
                return True  
    return False



size = int(input("Enter board size "))
pos = [-1] * size
nQueen(pos, size, 0)
print(pos)