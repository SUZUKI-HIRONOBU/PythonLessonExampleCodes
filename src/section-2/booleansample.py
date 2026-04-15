# File: booleansample.py

a=True
b=False
c=True

# True and False -> False
a and b
# True and True -> True
a and c
# False and True -> False
b and c

# All True
a or b
a or c
b or c


# zの値は 1 + 2 の結果が入る
z = a and (1+2)
print(z)

b and print(1+2)


a or (1+2)
(1+2) or a
b or (1+2)
(1+2) or b

