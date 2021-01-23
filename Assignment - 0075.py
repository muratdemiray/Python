# C7212- Murat

fibonacci = [0,1]
length=len(fibonacci)

while fibonacci[length-1] != 55 :
    fibonacci.append(fibonacci[length-2] + fibonacci[length-1])
    length = len(fibonacci) 
   
print("fibonacci →",fibonacci[1:])


    
