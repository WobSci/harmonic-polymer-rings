import numpy as np

# Definitions
b = 2
N = 100

# Time Range
t_norm = np.logspace(1, 12, num=10)

#
ring_CMS_diffusion = 6/(3*np.pi) * b**2/N * t_norm
print(ring_CMS_diffusion)