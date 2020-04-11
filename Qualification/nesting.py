for tc in range(int(input())):
    
    s = input().strip()
    
    count = 0
    
    output = []
    
    for char in s:
        if char == '(':
            count += 1
            output.append('(')
        elif char == ')':
            if count == 0:
                count += 1
                output.append('(')
            
            count -= 1
            output.append(')')
        else:
            d = int(char)
            while count > d:
                output.append(')')
                count -= 1
            while count < d:
                output.append('(')
                count += 1
            output.append(char)

    while count:
        output.append(')')
        count -= 1
    
    print("Case #{}: {}".format(tc + 1, ''.join(output)))