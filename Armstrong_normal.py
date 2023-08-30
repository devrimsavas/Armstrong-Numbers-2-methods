

#Armstrong Numbers Method 1

def checkNumber(number):
    convert=str(number) # we need to convert number to string first 
    len_number=len(convert) # we get lenght of string of number 
    sum_numbers=0 #collector 
    
    for i in range(len_number):
        
        sum_numbers+=int(convert[i])**len(convert) we collect the power of number which was determined by length 
 
    return sum_numbers


# test from 0 to 14000000
for i in range(0,14000000):
    if i==checkNumber(i):
        print(f"{i}={checkNumber(i)}")
        
        

    
        
