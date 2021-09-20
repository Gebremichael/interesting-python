# strange all()
# it suppose to return false if any false, 0 or [[]] (empty list in list)
# but can return true if added another empty list

print(all([]))  # true
print(all([[]])) # false
print(all([[[]]])) # true