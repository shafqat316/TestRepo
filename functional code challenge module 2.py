

max_value = 50

for i in range(0,max_value+1):
    if i % 3 ==0 and i % 4 ==0: #the numbers must be divisible by both 3 and 4
        print(i)

#odd number challenge
        numbers = [3, 9, 1, 10, 5, 2, 8]

for number in numbers:
    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")    


#building a simple countdown timer

for i in range(10, -1, -1):
    print(i)
    if i == 5:
        print("Halfway point reached!")
    if i==0:     #additional stuff i added 
        print("HAPPY NEW YEAR!")    