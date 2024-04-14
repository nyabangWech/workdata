tuple1=("banana","apple","orange","apple","mango","banana")
print(tuple1)

print(len(tuple1))

print(tuple1[1])

print(tuple1[2:5])

tuple2=("mango","maize","kiwi","pineapple")

tuple3 = tuple1+tuple2

print(tuple3)

del tuple2

tuples = list(tuple3)

tuples[1]="kiwi"

print(tuple1[-1])

vegtuple=("cabbage","sukumawiki","potatoes","tomatoes","onions","onions")
veg = vegtuple.count("onions")
print(veg)
