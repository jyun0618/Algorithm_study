A = input()
B = input()
C = input()

if A == 'FizzBuzz':
    print('Fizz')
        
elif A == 'Fizz':
    if C == 'Buzz':
        print('Fizz')
    else:
        if (int(C)+1)%5==0:
            print('FizzBuzz')
        else:
            print('Fizz')

elif A == 'Buzz':
    if C == 'Fizz':
        print(int(B)+2)
    else:
        if (int(C)+1)%3==0:
            print('Fizz')
        else:
            print(int(C)+1)
else:
    if (int(A)+3) % 5 == 0 and (int(A)+3) % 3 == 0:
        print('FizzBuzz')
    elif (int(A)+3) % 5 == 0 and (int(A)+3) % 3 != 0:
        print('Buzz')
    elif (int(A)+3) % 5 != 0 and (int(A)+3) % 3 == 0:
        print('Fizz')
    else:
        print(int(A)+3)
        
        