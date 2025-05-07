def Fizz_Buzz(number_to_test): 
  result = ""
  if(number_to_test % 2 == 0): 
    result += "Fizz"
    
  if(number_to_test % 3 == 0): 
    result += "Buzz"
  return(result) 
  
test_val = 4

test_result = Fizz_Buzz(test_val) 

print("Results: " + test_result)
