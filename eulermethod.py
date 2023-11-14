# import statements
import numpy as np
import matplotlib.pyplot as plt

# stylistic choices
#plt.style.use('seaborn-poster')
#%matplotlib inline

# define parameters
f = lambda t, s: np.exp(-t) # ODE
h = 0.2 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

# euler method setup
s = np.zeros(len(t))
s[0] = s0

# for each step in the range, perform the explicit calculation
for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

# plotting functions
plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()