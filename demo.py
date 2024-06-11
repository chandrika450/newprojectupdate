#def isPalindrome(s):
 #   return s == s[::-1]
#s = "malayalam"
#ans = isPalindrome(s)

#if ans:
   # print("Yes")
#else:
   # print("No")

    #a=input("enter a string:")
    #b=a[::-1]
    #if z==b:
     #   print(f"{a} is a palindrome")
    #else:
       # print(f"{a} is not a palindrome")
        #abs/fabs   round   floor   ceil

num = 407

# To take input from the user
# num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")