import random

#Q: What did you see on line 1? | random.randint(5, 20)
#A: It generated an Integer between 5 and 20

#Q: What did you see on line 2? | random.randrange(3, 10, 2)
#A: It generated an Integer between 3 and 9 with increments of 2 (3, 5, 7, 9)
#Q: Could line 2 have produced a 4?
#A: No

#Q: What did you see on line 3? | random.uniform(2.5, 5.5)
#A: It generated a Float between 2.5 and 5.5

print(random.randint(1,100)) # this will return an int between 1 and 100
print(random.uniform(1,100)) # this will return a floating point between 1 and 100
