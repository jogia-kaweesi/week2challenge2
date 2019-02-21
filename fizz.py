#python function to return fizz if combined length of strings is divisible by 3, 
  
def Fizzbuzz(list1, list2):

    a = len(list1) 
    b = len(list2) 
 
    z = a+b

    if z%3 == 0:
         
        return "Fizz" 

    elif z%5 == 0: 
         return "Buzz"
        
    else:
    
       if z%5 == 0 and z%3 == 0: 
            return "Fizzbuzz"
        
    print(Fizzbuzz([1, 2, 3], [1, 2])) 
