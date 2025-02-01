import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Definitions of Scalars
b = 11*10**(-10)
N = 100
R = 1*10**(-9)

# Definitions of Arrays
t_norm = np.logspace(0, 14, num=100)
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
print(p)

# Calculate MSD for t_norm values
A = 6/(3*np.pi**2) * b**2/N # MSD of center of mass
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
    yaxis_title='MSD',
    xaxis=dict(tickformat='.0e'),
    yaxis=dict(tickformat='.0e')
)
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")

# Calculate characteristic time points
RMS_ROG = R*b/np.pi * (np.arctan(np.pi*R/b)-np.arctan(2/N*np.pi*R/b))
print(RMS_ROG)
limit1 = 4*np.pi**2*RMS_ROG**2/b**4
limit2 = 6*np.pi**2*RMS_ROG*N/b**2
t_char = np.array([1, limit1, limit2])

MSD_char = []
for i in t_char:
    temp = A*i + 4*np.sum(B*(1-np.e**(-C*i)))
    MSD_char.append(temp)

# Add limits to plot
fig.add_trace(go.Scatter(x=t_char, y=MSD_char, mode='markers', marker=dict(color='red', symbol='diamond', size=10)))

# Calculate approximations between characteristic times
t_regime1 = np.logspace(0,np.log10(limit1),10)
MSD_regime1 = []
for i in t_regime1:
    temp = 2*b**2/np.pi**(3/2)*i**(1/2)
    MSD_regime1.append(temp)

t_regime2 = np.logspace(np.log10(limit1),np.log10(limit2),10)
MSD_regime2 = []
for i in t_regime2:
    temp = 2*RMS_ROG
    MSD_regime2.append(temp)

t_regime3 = np.logspace(np.log10(limit2),np.log10(np.max(t_norm)),10)
MSD_regime3 = []
for i in t_regime3:
    temp = 6/(3*np.pi**2) * b**2/N * i
    MSD_regime3.append(temp)

# Add approximations to plot
fig.add_trace(go.Scatter(x=t_regime1, y=MSD_regime1, mode='lines', name='Approx. 1', line=dict(color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime2, y=MSD_regime2, mode='lines', name='Approx. 2', line=dict(color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime3, y=MSD_regime3, mode='lines', name='Approx. 3', line=dict(color='green', width=2)))
fig.show()