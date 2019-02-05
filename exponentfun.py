
def find_power(num, pow_num):
    
    result = 1
    
    for index in range(pow_num):
        
        result = result * num
     
    return result


print(find_power(2, 9))



