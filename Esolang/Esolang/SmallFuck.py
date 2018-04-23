def interpreter(code, tape):
    # Implement your interpreter here
    cells = []
    for n in tape:
        cells.append(int(n))
    i = 0
    j = 0
    permit = 0
    status = 0
    stack = []
    while j<len(code):
        c = code[j]
        if i<0 or i>=len(tape):
            break
        if permit==0:
            if c=='<':
                i-=1
            elif c=='>':
                i+=1
            elif c=='*':
                cells[i] = 1 - cells[i]
        if c=='[': #and (permit==0 or (len(stack)!=0 and stack[-1]==']')):
            if len(stack)!=0 and stack[-1]==']':
                stack.pop()
            stack.append(c)
            if cells[i]==0:
                permit+=1
            else:
                permit = 0
        elif c==']':# and (permit==0 or (len(stack)!=0 and stack[-1]=='[')):
            if stack[-1]=='[':
                stack.pop()
            if cells[i]==1:
                stack.append(c)
                if permit>0:
                    permit-=1
            else:
                # stack.append(c)
                permit+=1
        else:
            pass
        if len(stack)!=0 and stack[-1]==']':
            j-=1
        else:
            j+=1
    sr = ''
    for n in cells:
        sr+=str(n)
    return sr

print(interpreter('[*>[>*>]>]', '11001'))