set = {"vijith", "man", "ruvi", "sakip", "pollard"}
for x in set:
  print(set)

# remove the last item by using pop() method
# so when usings the pop() method you will not know which that get removed
a =  {'san', 'ball', 'bat'}
x = a.pop()
print(x)
print(a)

set1 = {"a", "b", "v",}
set2 = {1,2,4}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "v",}
set2 = {1,2,4}
set1.add(set2)
print(set1)
