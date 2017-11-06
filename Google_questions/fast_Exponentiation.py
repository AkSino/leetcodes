base=2
exponent=8

def fast_exponentiation(base,exponent):
    if exponent==1:
        return base
    result=fast_exponentiation(base,exponent/2)
    return result*result
print(fast_exponentiation(base,exponent))