
# IMP : tuple is faster than list:  beacuse it samll memory loss

# # 1.  (suntax)

tu = (10,)   ### use some for singal value
tu = (10, 20, 30, 'a', 3.14, 10)


# # 2. (type of data)

# Heterogenous

# # 3.  (sequance)

# ordered 


# # 4.   (changeble)
# immutable


# # 5.  (duplication)

# Duplicate elements are allowed

print(type(tu))
print(tu)



##### tuple is faster than  list

import sys
list= []
tuple = ()
print(sys.getsizeof(list))
print(sys.getsizeof(tuple))

