def print_arr(arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            print(arr[x][y], end=' ')
        print()
    print('------------')
    
def cacti_number(plot):
    def wrapper(arr): 
        count = 0
        rows = len(arr)
        cols = len(arr[0])
        
        if any(len(row) != cols for row in arr):
            return 0
        FIRST_ROW = 0
        FIRST_COL = 0
        LAST_ROW = rows - 1
        LAST_COL = cols - 1
         
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 1:
                    continue
                else:
                    has_neighbor = False  
                    if i > FIRST_ROW and arr[i-1][j] == 1:
                        has_neighbor = True
                    if j > FIRST_COL and arr[i][j-1] == 1:
                        has_neighbor = True
                    if i < LAST_ROW and arr[i+1][j] == 1:
                        has_neighbor = True
                    if j < LAST_COL and arr[i][j+1] == 1:
                        has_neighbor = True
                    
                    if not has_neighbor:
                        count += 1
                        arr[i][j] = 1
                
        return count

    return wrapper(plot)
'''
def main():
    # plot = [ [1, 0, 1, 0, 1],
            #  [0, 0, 0, 0, 0],
            #  [1, 0, 0, 0, 0] ]

    plot = [ [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 1] ]
    print(f"count = {cacti_number(plot)}")

display = False
main()
'''