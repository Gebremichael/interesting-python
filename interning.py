# Interesting python optimisation on immutable strings

# you would expect all 2 objects below to be in different addresses
a = "h"+"i"
b = "hi"

#but with interning, python knowing the same immutiable string existing during compile 
# it doesnt create a new address, it just point to existing on
print(a is b)
#same as
print(id(a)==id(b))

# not that join doesnt work since it doesnt know during complile
c = "".join(["h","i"])
print(b is c)

# NOTE this is because it doesnt know that c == "hi" at compile time