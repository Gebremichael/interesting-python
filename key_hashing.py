# reason for same key being accessed with different value
a ={}
a[1]= "Morning"
a[1.0]="Afternoon"
a[True]="Evening"
a[3-2]="Night"

print(a)

#reason is due to the fact that keys in dictionary are hashed
print(hash(1)== hash(True))
print(hash(7-6)== hash(1.0))
