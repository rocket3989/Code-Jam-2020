for tc in range(int(input())):
    print("Case #{}:".format(tc + 1))
    N = int(input())
    if N == 1:
        print("1 1")
        continue
    N -= 1
        
    pascal = [[1]]
    for i in range(500):
        row = [1]
        for a, b in zip(pascal[-1], pascal[-1][1:]):
            row.append(a + b)
        pascal.append(row + [1])
    
    from collections import defaultdict
    
    def neighbors(r, k):
        ret = []
        
        for dr, dk in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
            R, K = r + dr, k + dk
            if R >= 0 and K >= 0 and R >= K:
                yield (R, K)
    
    
    visited = defaultdict(bool)
    
    def solve(n, r, k):
        visited[(r, k)] = True
        
        pos = []
        
        for nr, nk in neighbors(r, k):
            if pascal[nr][nk] <= n and not visited[(nr, nk)]:
                pos.append((pascal[nr][nk], nr, nk))
                
        pos.sort()
        pos.reverse()
        for score, nr, nk in pos:
            if score == n:
                return [(nr + 1, nk + 1), (r + 1, k + 1)]
            
            ret = solve(n - score, nr, nk)
            if ret:
                ret.append((r + 1, k + 1))
                return ret
                
        visited[(r, k)] = False
        
        return False        
    
    
    ans = solve(N, 0, 0)
    
    ans.reverse()
    
    score = 0
    for part in ans:
        print(*part)