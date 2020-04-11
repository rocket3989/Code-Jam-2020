for tc in range(int(input())):
    print("Case #{}:".format(tc + 1))
    N = int(input())
    print("1 1")
    N -= 1
    if N == 0: continue
    row = 2
    
    for i in range(1, 500):
        if N >= i:
            N -= i
            print(row, row - 1)
            row += 1
        
        else:
            row -= 1
            break
    
    while N:
        print(row, row)
        N -= 1
        row += 1
        
    
    
    
        