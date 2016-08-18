import math

def theta_term(n):
    return math.atan2(1, n ** 0.5)

def radius(n):
    return (n + 1) ** 0.5

#
# In our case, we have a closed for the radius at n. However, the total rotation for a given n is actually given by the
# sum of every theta_term(n) below it:
#   sum(theta_term(k) for k in range(1, n+1))
# This is not feasible for large n! We have find a way to accurately estimate!
