#display the no of times each item is present in an array

from collections import defaultdict
count = defaultdict(int)
array = [1,1,4,2,4,1,4,5,5,5,6,6,4,3]

for item in array:
    count[item] += 1

for a,b in count.items():
    print (f'{a} is present {b} times.')