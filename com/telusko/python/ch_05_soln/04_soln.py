s=set()

#In Python, integers and floats with the same value are considered equal.
# So 20 and 20.0 are treated as the same element in a set
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print(s)