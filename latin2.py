broken = [
        -1, -1, 
        {3},
        {4, 5, 7, 8}]

for i in range(4, 51):
        broken.append({i + 1, i * i - 1})
    


for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]
    if K in broken[N]:
        print("Case #{}: IMPOSSIBLE".format(tc + 1))
        continue
    print("Case #{}: POSSIBLE".format(tc + 1))
    
    row = [i for i in range(1, N + 1)]
    
    vals = []
    mat = [row]
    for i in range(N - 1):
        mat.append([mat[-1][-1]] + mat[-1][:-1])
    
    mat = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3],[3, 4, 1, 2]]
    def search(arr, score, lastDiff):
        if score == K:
            return arr
        best = (100, 0, 0, 'r')
        for r1 in range(N):
            for r2 in range(r1 + 1, N):
                diff = arr[r1][r2] + arr[r2][r1] - arr[r1][r1] - arr[r2][r2]
                test = abs(score + diff - K)
                if test <= best[0]:
                    best = (test, diff, r1, r2)
        print(score, best)
        test, diff, r1, r2 = best
        if diff == -lastDiff: return False
        
        new = [1] * N
        for r in range(N):
            if r == r1:
                new[r] = arr[r2][:]
            elif r == r2:
                new[r] = arr[r1][:]
            else:
                new[r] = arr[r][:]
        
        res = search(new, score + diff, diff)
        
        if res:
            return res
        
        for r in range(N):
            for c in range(N):
                if c == r1:
                    new[r][c] = arr[r][r2]
                elif c == r2:
                    new[r][c] = arr[r][r1]
                else:
                    new[r][c] = arr[r][c]
        
        return search(new, score + diff, diff)
        
        
    for row in search(mat, N, 100):
        print(*row)