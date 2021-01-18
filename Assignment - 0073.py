# C7212- Murat

number = input("Please enter a positive integer: ")
while not number.isdigit():
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a positive integer: ")

sum = 0
len = len(number)
for i in range(0,len):
    sum += int(number[i])**len

if sum == int(number):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")
    
    
