for tc in range(int(input())):
    N = int(input())

    prefixes = []
    suffixes = []

    maxLen = 0
    middle = []
    
    for i in range(N):
        arr = input().split('*')
        
        pre = arr[0]
        suff = arr[-1]
        
        if pre != '':
            prefixes.append(pre)
        if suff != '':
            suffixes.append(suff)
        for seg in arr[1:-1]:
            middle.append(seg)
        
            
    prefix = ''
    
    fail = True
    
    for add in prefixes:
        if len(add) > len(prefix):
            if add[:len(prefix)] != prefix:
                break
            prefix = add
            
        elif len(add) < len(prefix):
            if prefix[:len(add)] != add:
                break
                
        else:
            if add != prefix:
                break
    else:
        fail = False
        
    if fail:        
        print("Case #{}: *".format(tc + 1))
        continue    
            
    suffix = ''     
            
    for add in suffixes:
        if len(add) > len(suffix):
            if add[len(add) - len(suffix):] != suffix:
                break
            suffix = add
            
        elif len(add) < len(suffix):
            if suffix[len(suffix) - len(add):] != add:
                break
                
        else:
            if add != suffix:
                break
    else:
        print("Case #{}: {}".format(tc + 1, prefix + ''.join(middle) + suffix))
        continue
    
    
    print("Case #{}: *".format(tc + 1))