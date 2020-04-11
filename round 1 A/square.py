for tc in range(int(input())):
    R, C = [int(x) for x in input().split()]
    
    
    floor = []
    for r in range(R):
        floor.append([int(x) for x in input().split()])
        
    score = 0
    
    
    while True:
        neighborSum = [[0 for i in range(C)] for j in range(R)]
        count = [[0 for i in range(C)] for j in range(R)]
        score += sum(sum(row) for row in floor)
        
        for r in range(R):
            lastSeen = -1
            for c in range(C):
                if lastSeen != -1:
                    neighborSum[r][c] += lastSeen
                    count[r][c] += 1
                if floor[r][c] != 0:
                    lastSeen = floor[r][c]
        
        for c in range(C):
            lastSeen = -1
            for r in range(R):
                if lastSeen != -1:
                    neighborSum[r][c] += lastSeen
                    count[r][c] += 1
                if floor[r][c] != 0:
                    lastSeen = floor[r][c]
        
        for r in range(R):
            lastSeen = -1
            for c in range(C - 1, - 1, -1):
                if lastSeen != -1:
                    neighborSum[r][c] += lastSeen
                    count[r][c] += 1
                if floor[r][c] != 0:
                    lastSeen = floor[r][c]
                    
        for c in range(C):
            lastSeen = -1
            for r in range(R - 1, -1, -1):
                if lastSeen != -1:
                    neighborSum[r][c] += lastSeen
                    count[r][c] += 1
                if floor[r][c] != 0:
                    lastSeen = floor[r][c]
        elim = 0
        for r in range(R):
            for c in range(C):
                if floor[r][c] == 0: continue
                if count[r][c] != 0:
                    if floor[r][c] < neighborSum[r][c] / count[r][c]:
                        floor[r][c] = 0
                        elim += 1
        if elim == 0:
            break
        
        
    print("Case #{}: {}".format(tc + 1, score))