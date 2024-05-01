# Exercise 7
# Your solution comes here

val = int(input("Enter value: "))
div = 1000
total = 0
for i in range(0, 4):
        total = total + val // div
        val = val % div
        div = div / 10
print(total)