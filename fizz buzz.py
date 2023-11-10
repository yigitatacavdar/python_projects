
#prints fizz if it is divisible by 3 and 4, prints buzz if divisible by 5
#prints fizzbuzz if divisible by 3 and 5, or 4 and 5


for n in range(201):

 output = ""

 if (n % 3 and n % 4) == 0:
  output += "Fizz"

 if (n % 5) == 0:
  output += "Buzz"

 elif output == "":
  output = n

 print(output)











     
 
    
