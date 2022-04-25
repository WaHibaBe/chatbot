# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.

print('Hello! My name is robotchat')
print('I was created in 2 april 2022.')


print('Please, remind me your name.')
name = input()
print('What a great name you have, ' + name + '!')


print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")


print('Now I will prove to you that I can count to any number you want.')

num = int(input())
curr = 0
while curr <= num:
 print(curr, '!')
 curr = curr + 1


print("Let's test your programming knowledge.")

print("Why do we use methods?")
print(1., "To repeat a statement multiple times.")
print(2., "To decompose a program into several small subroutines.")
print(3., "To determine the execution time of a program.")
print(4., "To interrupt the execution of a program.")

answer = int(input())
while answer != 2:
 print('try again')
 answer = int(input())


print('Completed, have a nice day!')


print('Congratulations, have a nice day!')