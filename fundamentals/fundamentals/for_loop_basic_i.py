# Print all integers from 0 to 150
for i in range (0, 151):
    print(i)

# Print all the multiples of 5 from 5 to 1,000
for i in range (5,1001):
    if i % 5 == 0:
        print (i)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range (1, 101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else: print(i)

# Add odd integers from 0 to 500,000, and print the final sum
odd_sum = 0
for i in range (0, 500001):
    if i%2 == 1:
        odd_sum += i
print(odd_sum)

# Print positive numbers starting at 2018, counting down by fours.
for i in range (2018, 0, -4):
    print(i)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 707
highNum = 789
mult = 10

for Boeing in range (lowNum, highNum, mult):
    print("Today's Aircraft Type:", Boeing)

short_haul = 320
long_haul = 381
mult = 10

for Airbus in range (short_haul, long_haul, mult):
    if Airbus == 360:
        print("Invalid Type")
    elif Airbus == 370:
        print("Invalid Type")
    else: print("Today's Aircraft Type:", Airbus)

