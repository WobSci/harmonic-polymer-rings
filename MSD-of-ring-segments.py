import numpy as np

# Definitions of Scalars
b = 2
N = 100
R = 1

# Definitions of Arrays
t_norm = np.logspace(1, 12, num=10)
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
print(p)

# Calculation
A = 6/(3*np.pi) * b**2/N * t_norm # MSD of center of mass
print(A)

B = ((4*np.pi**2*p**2)/(N*b**2)+N/R**2)**-1
C = (2*p/N)**2 + 1/np.pi**2 * b**2/R**2
print(C)

#MSD = np.sum(B*1-np.e**(-C*t_norm))
#print(MSD)