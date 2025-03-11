# collections = set()
# collections.add("list")
# collections.add("tuple")
# collections.add("dict") 
# collections.add("set")
# collections.add((1,2,3))
# collections.clear()

# print(collections)   


# uncomment the above code and run it. 




#set is a collection of unordered and unindexed elements.
#set is a collection of unique elements.

set1 = {"list", "tuple", "dict", "set"}
set2 = {1,2,3,4,5,6,7,8,9,10}

# print(set1+set2) # this will give an error.

print(set1.union(set2)) # this will give the union of two sets.

print(set1) # set1 will remain unchanged.
print(set2) # set2 will remain unchanged.


print (set1.intersection(set2)) # this will give the intersection of two sets.





for i in set1:
    print(i)