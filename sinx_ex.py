def fakt(x):
    start = 2
    result = 1
    for i in range(x-1):
        result = result * start
        start += 1
    return result

def sinx_dift(x,turn):
    
    ust = 3
    result = x

    for i in range(1,turn-1):
        print(f"üst {ust} , fakt : {fakt(ust)} , result : {result}")
        if i%2 == 0:
            result += x**ust / fakt(ust)

        else:
            result -= x**ust / fakt(ust)

        ust+=2
    print(f"üst {ust} , fakt : {fakt(ust)} , result : {result}")
        

    print(result)

def ex_dift(x,turn):
    
    ust = 2
    result = 1 + x
    if turn > 2 :
        for i in range(1,turn-1):
            print(f"üst {ust} , fakt : {fakt(ust)} , result : {result}")
            result += x**ust / fakt(ust)
            ust+=1
        
        

    print(result)

#ex_dift(2,5)
sinx_dift(30,5)