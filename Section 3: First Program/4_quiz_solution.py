# 1. How many seconds are there in 24 minutes and 36 seconds?
import math

total_seconds = 24 * 60 + 36
print('24 minutes and 36 seconds', total_seconds)

# 2. The Batmobile, having average speed of 80 km/hour will travel from Gotham to Arkham.
# We know the distance between Gotham and Arkham,
# which is 450 km's. How many minutes will it take for Batmobile to travel from Gotham to Arkham?

total_time_taken_in_minutes = (450 / 80) * 60
print(total_time_taken_in_minutes)

# 3.What is 14'th power of 2?

print(2 ** 14)

# 4.Can you print "Python, I love you :)" on the screen?

print("Python, I love you :)")

# 5.Can you print the type of number 15?

print(type(15))

# 6. Can you print the type of "Hi Python" expression?

print(type('hi python'))

# 7. Can you print the type of text "15"?

print(type('15'))

# 8. What is the remainder when we divide 49 by 5?

print(49 % 5)

# 9. What is the floor division (integer division) result of dividing 49 by 5?

print(49 // 5)

# 10. What is the average of sum of squares of integers from 1 to 5?
asum = 0
for i in range(6):
    asum += i ** 2

average = asum/5
print(average)

# 11. Solve this equation with Python:

print(math.sqrt(4**3+17))
