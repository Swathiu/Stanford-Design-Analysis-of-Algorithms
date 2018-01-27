import math


def split(number,size):
    factor = math.pow(10,size)
    low = int(number % factor)
    high = int(number / factor)
    return high,low

def Karatsuba_multplication(num1,num2):
    if int(num1 < 10) or (num2 < 10):
        return num1 * num2

    else:       
        no_of_digits_num1 = int(math.log10(num1))+1
        no_of_digits_num2 = int(math.log10(num2))+1

        max_size = max(no_of_digits_num1,no_of_digits_num2)
        n = math.floor(max_size/2)
        
        
        high1,low1 = split(num1,n)
        high2,low2 = split(num2,n)
        
        ac = Karatsuba_multplication(high1,high2)
        bd = Karatsuba_multplication(low1,low2)
        acbd = Karatsuba_multplication(high1+low1,high2+low2)

        result = (pow(10,n*2) * ac) + (pow(10,n) * (acbd - ac - bd)) + bd

        return result


num1 = 12345
num2 = 5678

answer = Karatsuba_multplication(num1,num2)
print ("The product of %d and %d is %d." %(num1,num2,answer))

