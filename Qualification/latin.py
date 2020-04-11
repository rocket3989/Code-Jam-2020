for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    broken = [
        -1, -1, 
        {3},
        {4, 5, 7, 8},
        {5, 15},
        {6, 24}
    ]
    for i in range(6, 51):
        broken.append({i + 1, i * i - 1})
    
    if K in broken[N]:
        print("Case #{}: IMPOSSIBLE".format(tc + 1))
        continue
    
    print("Case #{}: POSSIBLE".format(tc + 1))
    vals = []
      
    if K > (N * N) // 2:
        vals = [N] * N
        
        diff = N * N - K
        pos = 0
        if diff != 0:
            vals[pos] = N - 1
            diff -= 1
            pos += 1
            
            while diff:
                if diff < N:
                    vals[pos] -= diff
                    diff = 0
                else:
                    vals[pos] = 1
                    diff -= N - 1
                    pos += 1
                    
    else:
        vals = [1] * N
        
        diff = K - N
        pos = 0
        if diff != 0:
            vals[pos] = 2
            diff -= 1
            pos += 1
            
            while diff:
                if diff < N:
                    vals[pos] += diff
                    diff = 0
                else:
                    vals[pos] = N
                    diff -= N - 1
                    pos += 1
        

    grid = [[0 for i in range(N)] for i in range(N)]

    for i, val in enumerate(vals):
        grid[i][i] = val


    def nextEl(x, y):
        if x == N - 1:
            return (0, y + 1)
        return (x + 1, y)
        

    def printGrid():
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                print(el if el != 0 else ' ', end = ' ')
            print('')

    rowSets, colSets = [], []

    for i, row in enumerate(grid):
        colSets.append(set([grid[j][i] for j in range(N)]))
        rowSets.append(set(row))

    def solve(pair):
        x, y = pair
        if y > N - 1: return True

        if grid[y][x] != 0:
            return solve(nextEl(x, y))

        for val in range(1, N + 1):
            if val in rowSets[y] or val in colSets[x]:
                continue

            grid[y][x] = val
            rowSets[y].add(val)
            colSets[x].add(val)
            
            # printGrid()
            if solve(nextEl(x, y)): return True

            grid[y][x] = 0
            rowSets[y].remove(val)
            colSets[x].remove(val)
            
        return False
        
    solve((0, 0))
    printGrid()