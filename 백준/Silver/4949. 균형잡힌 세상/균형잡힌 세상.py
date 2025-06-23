while True:
    str = input()
    if str == '.':
        break
    
    bracket = []
    balance = True
    for s in str:
        if s == '(' or s == '[':
            bracket.append(s)
        elif s == ')':
            if not bracket or bracket[-1] == '[':
                balance = False
                break
            bracket.pop()
        elif s == ']':
            if not bracket or bracket[-1] == '(':
                balance = False
                break
            bracket.pop()
            
    if balance and not bracket:
        print('yes')
    else:
        print('no')