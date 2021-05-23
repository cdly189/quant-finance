from scipy.integrate import quad
import numpy as np
a = 1
b = 3
n = 8
I_mid = 0
h = (b-a) /n

f = lambda x: 1 / (x+1)**2

# Using scipy
I = quad(f,a,b)
print(I)

# Midpoint rule
for i in range(1,n+1):
    x_i = a + (i - 0.5) * h
    I_mid = I_mid + f(x_i)

I_mid = h * I_mid

print(I_mid)

# Trapezoidal Rule
I_trap = f(a) / 2 + f(b) / 2
for i in range(1,n):
    a_i = a + i * h
    I_trap = I_trap + f(a_i)

I_trap = h * I_trap
print(I_trap)

# Simpson's Rule
I_simpson = f(a) / 6 + f(b) / 6
for i in range(1,n):
    a_i = a + i * h
    I_simpson = I_simpson + f(a_i) / 3

for i in range(1, n +1):
    x_i = a + (i - 0.5) * h
    I_simpson = I_simpson + 2 * f(x_i) / 3

I_simpson = h * I_simpson
print(I_simpson)

# Find the best method
# By finding absolute difference

print(abs(I[0] - float(I_mid)))
print(abs(I[0] - float(I_trap)))
print(abs(I[0] - float(I_simpson)))

# From here, we can conclude that by using the Simpson's Rule, we get the
# closest result