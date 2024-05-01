# Exercise 8
# Your solution comes here
num1 = int(input())
num2 = int(input())
num3 = int(input())


smallest = (num1 * (num1 < num2 and num1 < num3)) + (num2 * (num2 < num1 and num2 < num3)) +  (num3 * (num3 < num1 and num3 < num2))
biggest = (num1 * (num1 > num2 and num1 > num3)) + (num2 * (num2 > num1 and num2 > num3)) +  (num3 * (num3 > num1 and num3 > num2))
mid = (num1 + num2 + num3) - biggest - smallest

print(smallest)
print(mid)
print(biggest)
