
def find_power(num, pow_num):
    
    result = 1
    
    for index in range(pow_num):
        
        result = result * num
     
    return result

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
print( "SOLUTION:",find_power(number, exponent))



