a = int(input("a value: "))
b = int(input("b value: "))
c = int(input("c value: "))
x = a
y = b
z = c
# takes b value and makes it negative
d = y * -1
# b^2
e = y * y
# -4ac
l = -4 * x * z
# b^2 - 4ac
m = e + l
# finds sqroot
f = m ** 0.5
g = d + f
i = d - f
k = 2 * x
# all over 2a
h = g / k
j = i / k
print ("%s" %h)
print ("%s" %j)
