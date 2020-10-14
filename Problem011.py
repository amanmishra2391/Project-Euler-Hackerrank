grid = []
for grid_i in range(20):
    grid_t = []
    for grid_temp in input().split(' '):
        grid_t.append(int(grid_temp))
    grid.append(grid_t)
if 1:
    GP=-1
    for i in range(20):    
        for j in range(17):
            P=grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if P>GP:
                GP=P
    for i in range(17):    
        for j in range(20):
            P=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if P>GP:
                GP=P
    for i in range(17):    
        for j in range(17):
            P=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if P>GP:
                GP=P
    for i in range(17):    
        for j in range(16,-1,-1):
            P=grid[i][j+3]*grid[i+1][j+2]*grid[i+2][j+1]*grid[i+3][j]
            if P>GP:
                GP=P
    print(GP)
