import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Definitions of Scalars
b = 1
N = 100
R = 1

# Definitions of Arrays
t_norm = np.logspace(1, 12, num=100)
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
print(p)

# Calculate MSD for t_norm values
A = 6/(3*np.pi) * b**2/N # MSD of center of mass
B = ((4*np.pi**2*p**2)/(N*b**2)+N/R**2)**(-1)
C = (2*p/N)**2 + 1/np.pi**2 * b**2/R**2

MSD = []
for i in t_norm:
    temp = A*i + 4*np.sum(B*(1-np.e**(-C*i)))
    MSD.append(temp)

MSD = np.array(MSD)

# Plot MSD vs t_norm
fig = go.Figure()
fig.add_trace(go.Scatter(x=t_norm, y=MSD, mode='markers+lines'))
fig.update_layout(
    title='MSD of ring segments',
    xaxis_title='t/tau_s',
    yaxis_title='MSD'
)
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.show()
