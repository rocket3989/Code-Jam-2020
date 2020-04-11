T, N = [int(x) for x in input().split()]

for tc in range(T):
    pos = 1
    ans = [-1] * (N // 2)
    match = [False] * N
    
    matchTest = -1
    diffTest = -1
    
    print(1)
    ans[0] = int(input())
    print(N)
    val = int(input())
    
    if val == ans[0]:
        matchTest = 0
        match[0] = True
    else:
        diffTest = 0
    
    for i in range(3, 151):
    
        if pos == N // 2:
            break
            
        if i % 10 == 1:
            if matchTest == -1:
                print(1)
                input()
            
            else:
                print(matchTest + 1)
                val = int(input())
                if val != ans[matchTest]:
                    for b in range(pos + 1):
                        ans[b] ^= 1
                
        elif i % 10 == 2:
            if diffTest == -1:
                print(1)
                input()
            
            else:
                print(diffTest + 1)
                val = int(input())
                if val != ans[diffTest]:
                    for b in range(pos + 1):
                        if not match[b]:
                            ans[b] ^= 1
                            
        elif i % 2:
            print(pos + 1)
            ans[pos] = int(input())
            
        else:
            print(N - pos)
            val = int(input())
            
            if val == ans[pos]:
                matchTest = pos
                match[pos] = True
            else:
                diffTest = pos
            pos += 1
    
    
    out = ''.join([str(x) for x in ans])
    for i in range(N // 2 - 1, -1, -1):
        if match[i]:
            out += str(ans[i])
        else:
            out += str(ans[i] ^ 1)
    print(out)
    
    if input().strip() == "N": break 
            