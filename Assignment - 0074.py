# C7212- Murat

number = input("Please enter a positive integer: ")
while not number.isdigit():
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a positive integer: ")


num = int(number)
prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        break

if prime:
    print (num,"is a prime number")
else:
    print (num,"is not a prime number")


    
