#program to find whether a given number is prime number or not
num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("This number is not prime number")
        break
    else:
        print("This number is prime number")
        break
