sectionA={10,20,30,40,50}
print(sectionA)

sectionA.add(100)   #to add single value
print(sectionA)

sectionA.update( {5,6,7,8})   #to insert multiple values
print(sectionA)

sectionB={90,80,70,50}
a=sectionA.union(sectionB)  #to combine two sets
print(a)

b=sectionA.intersection(sectionB)   #to find common value
print(b)

c=sectionA.intersection_update(sectionB)
print(sectionB)

#symmetric_difference
set1={1,2,3,4}
set2={5,6,7,8}
c=set1.symmetric_difference(set2)   #remove the common value
print(c)

d=set1.isdisjoint(set2) #if any value common it give false otherwise true
print(d)