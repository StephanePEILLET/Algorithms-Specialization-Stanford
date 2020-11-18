def karatsuba_multiplication(x:int, y:int, verbose:bool=False) -> int:
    '''
        Karatsuba Multiplication on two integers.
    '''
    x, y = str(x), str(y)
    n = max(len(x),len(y))
    
    # If inputs' lengths are different we pad with zeros the input with the smaller length
    if len(x) > len(y):
        y = '0'*(len(x)-len(y))+y
    else:
        x = '0'*(len(y)-len(x))+x
    
    # Slice the inputs in two with a length of n/2.
    a, b = x[:(n//2)], x[(n//2):]
    c, d = y[:(n//2)], y[(n//2):]
    
    # If splits' lengths is small enough with use the basic case.
    if n//2 <= 2:          
        e1 = int(a) * int(c)
        e2 = int(b) * int(d)
        e3 = (int(a) + int(b)) * (int(c) + int(d))
        
    # Else if splits' lengths is too large we use the method recursively. 
    else:
        e1 = karatsuba_multiplication(int(a), int(c))
        e2 = karatsuba_multiplication(int(b), int(d))
        e3 = karatsuba_multiplication(int(a) + int(b), int(c) + int(d))
        
    if n%2 == 0: # n even
        result = e1 * 10**n + e2 + (e3 - e2 - e1) * 10**(n//2)
    else:        # n odd
        result = e1 * 10**(n+1) + e2 + (e3 - e2 - e1) * 10**((n//2)+1)
        
    # Print several steps of computation of the Karatsuba multiplication.
    if verbose:
        print(f'x : {x} and y:{y}')
        print(f'n : {n}')
        print('e1:', e1)
        print('e2:', e2)
        print('e3:', e3)
        print('result:', result)
        print(f'attendu:{int(x) * int(y)}')
        
    return result 

def verification_karatsuba(x:int, y:int, verbose:bool=False)->None:
    '''
        Comparison of my Karatsuba's method and the native python multiplication. 
    '''
    print(f'Multiplication of x: {x} and y: {y}.')
    print('- Karatsuba:', karatsuba_multiplication(x, y, verbose=verbose))
    print('- Native   :', x * y)
    
    if karatsuba_multiplication(x, y, verbose=False) == x * y:
        print('Same result !')
    else:
        print('Errors ...')
