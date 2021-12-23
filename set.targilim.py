# תרגיל 8.1
set1={1,2,3,4,5}
set2={1,2,7,8,9}
set3=set1.copy()
set3.update(set2)
print(set3)
set3.remove(3)
print(set3)
print(max(set3))
print(min(set3))
print(len(set3))
set4={10,11,12}
set4.update(set3)
print(set4)
for i in set4:
    if set3 in set4:
        set.remove(set3)
print(set4)

