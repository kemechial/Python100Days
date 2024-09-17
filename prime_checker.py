def is_prime(num):
    dividers=[2,3,5,7]
    
    result=[num%div==0 for div in dividers]
    print(result)
    if (num not in dividers and num!=1) and any(result):
        return False
    else:
        return True
    

print(is_prime(int(input("Input number for prime check: "))))