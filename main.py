# inputValue = input("Enter a string-")

# if (inputValue == inputValue[::-1]):
#     print("The string is a palindrome")
# else:
#     print("Not a palindrome")

inputValue = int(input('Enter your desired value to check for palindrome: '))
temp = inputValue
rev = 0

while(inputValue>0):
    dig = inputValue%10
    rev = rev*10+dig
    inputValue = inputValue//10

if (temp==rev):
    print('palindrome')
else:
    print('Not a palindrome')
