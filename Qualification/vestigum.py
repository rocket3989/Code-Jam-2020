for tc in range(int(input())):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append([int(x) for x in input().split()])
        
    colCount = 0
    rowCount = 0
    
    for r in range(N):
        curr = set()
        for c in range(N):
            curr.add(mat[r][c])
        if len(curr) != N:
            rowCount += 1
    
    for c in range(N):
        curr = set()
        for r in range(N):
            curr.add(mat[r][c])
        if len(curr) != N:
            colCount += 1
    trace = 0
    for i in range(N):
        trace += mat[i][i]
        
    print("Case #{}: {} {} {}".format(tc + 1, trace, rowCount, colCount))
    