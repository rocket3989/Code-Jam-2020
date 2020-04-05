for tc in range(int(input())):
    N = int(input())
    
    events = []
    Jfree = -1
    Cfree = -1
    
    output = [''] * N
    for i in range(N):
        l, r = [int(x) for x in input().split()]
        events.append((l, r, i))
      
    for event in sorted(events):
        
        if Jfree <= event[0]:
            Jfree = event[1]
            output[event[2]] = "J"
        
        elif Cfree <= event[0]:
            Cfree = event[1]
            output[event[2]] = "C"
            
        else:
            output = ["IMPOSSIBLE"]
            break
    
    print("Case #{}: {}".format(tc + 1, ''.join(output)))
    