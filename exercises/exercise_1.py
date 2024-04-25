# Exercise 1
# Your solution comes here

number = int(input("Enter 5 digit number: "))
nums = [] 

while number > 0:
        nums.append(number % 10)
        number = number // 10

nums.reverse()

first = nums[0] + nums[2] + nums[4]
firstArr = []
while first > 0:
        firstArr.append(first % 10)
        first = first // 10
firstArr.reverse()


second = nums[1] + nums[3]
secondArr = []
while second > 0:
        secondArr.append(second % 10)
        second = second // 10
secondArr.reverse()

ans = 0
for i in range(0, len(firstArr)):
        ans = ans + firstArr[i]
        ans = ans * 10
for i in range(0, len(secondArr)):
        ans = ans + secondArr[i]
        ans = ans * 10
print(ans//10)

