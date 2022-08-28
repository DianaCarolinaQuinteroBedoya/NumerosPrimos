def is_prime(x):
    return all(((x/i) - int(x/i)) !=0 for i in range (2,x))
    #for i in range(2, x):
    #    if x%1 == 0:
    #        return True
    #    else:
    return False

def get_primes(x,y):
    result = []
    for i in range(x,y):
        if is_prime(i):
            result.append(i)
    return result
