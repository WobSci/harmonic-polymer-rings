import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Definitions of Scalars
b = 11*10**(-10)
N = 5000
R = 25*10**(-9)

# Definitions of Arrays
t_norm = np.logspace(0, 8, num=100)
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))

# Calculate MSD for t_norm values
A = 6/(3*np.pi**2) * b**2/N # MSD of center of mass
B = ((4*np.pi**2*p**2)/(N*b**2)+N/R**2)**(-1)
C = (2*p/N)**2 + (b/(np.pi*R))**2

MSD = []
for i in t_norm:
    temp = A*i + 4*np.sum(B*(1-np.e**(-C*i)))
    MSD.append(temp)

MSD = np.array(MSD)

# Plot MSD vs t_norm
fig = go.Figure()
fig.add_trace(go.Scatter(x=t_norm, y=MSD, mode='markers+lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle = \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}+4\sum\limits_{p=1}^{N/2}\left[\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}\left(1-e^{-\left(\left(\frac{2p}{N}\right)^2+\left(\frac{b}{\pi \tilde{R}}\right)^2\right)\frac{t}{\tau_s}}\right)\right]$'))
fig.update_layout(
    title=fr'$b = {b*10**9:.2g} \text{{ nm, }} \tilde{{R}} = {R*10**9:.2g} \text{{ nm, }} N = {N}$',
    xaxis_title=r'$t/\tau_s$',
    yaxis_title=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle$',
    xaxis=dict(tickformat='.0e'),
    yaxis=dict(tickformat='.0e'),
    legend_font_size=16,
    title_font_size=20
)
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")

# Calculate characteristic time points
RMS_ROG = R*b/np.pi * (np.arctan(np.pi*R/b)-np.arctan(2/N*np.pi*R/b))

t_char0 = 1
t_char1 = 4*np.pi**2*RMS_ROG**2/b**4
t_char2 = np.pi**2*RMS_ROG*N/b**2
t_char = np.array([t_char0, t_char1, t_char2])

MSD_tchar0 = A*t_char[0] + 4*np.sum(B*(1-np.e**(-C*t_char[0])))
MSD_tchar1 = A*t_char[1] + 4*np.sum(B*(1-np.e**(-C*t_char[1])))
MSD_tchar2 = A*t_char[2] + 4*np.sum(B*(1-np.e**(-C*t_char[2])))

# Add limits to plot
fig.add_trace(go.Scatter(x=[t_char0], y=[MSD_tchar0], mode='markers', name=r'$\frac{t}{\tau_s}=1$', marker=dict(color='red', symbol='square', size=10)))
fig.add_trace(go.Scatter(x=[t_char1], y=[MSD_tchar1], mode='markers', name=r'$\frac{t}{\tau_s}=4\pi^2\frac{\left\langle R_g^2\right\rangle_{eq}^2}{b^4}$', marker=dict(color='red', symbol='circle', size=10)))
fig.add_trace(go.Scatter(x=[t_char2], y=[MSD_tchar2], mode='markers', name=r'$\frac{t}{\tau_s}=6\pi^2\frac{\left\langle R_g^2\right\rangle_{eq}N}{b^2}$', marker=dict(color='red', symbol='diamond', size=10)))

# Calculate approximations between characteristic times
t_regime0 = np.logspace(0,np.log10(t_char1),10)
MSD_regime0 = []
for i in t_regime0:
    temp = 2*b**2/np.pi**(3/2)*i**(1/2)
    MSD_regime0.append(temp)

t_regime1 = np.logspace(np.log10(t_char1),np.log10(t_char2),10)
MSD_regime1 = []
for i in t_regime1:
    temp = 2*RMS_ROG
    MSD_regime1.append(temp)

t_regime2 = np.logspace(np.log10(t_char2),np.log10(np.max(t_norm)),10)
MSD_regime2 = []
for i in t_regime2:
    temp = 6/(3*np.pi**2) * b**2/N * i
    MSD_regime2.append(temp)

# Add approximations to plot
fig.add_trace(go.Scatter(x=t_regime0, y=MSD_regime0, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{2b^2}{\pi^{3/2}}\left(\frac{t}{\tau_s}\right)^{1/2}$', line=dict(dash='dot', color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime1, y=MSD_regime1, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx 2\left\langle R_g^2\right\rangle_{eq}$', line=dict(dash='dash', color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime2, y=MSD_regime2, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}$', line=dict(dash='solid', color='green', width=2)))
fig.add_annotation(
    x=np.log10(np.median(t_norm)), y=np.log10(0.75*np.max(MSD)),
    text=fr'$\left\langle R_g^2\right\rangle_{{eq}}=\frac{{\tilde{{R}}b}}{{\pi}}\left(\arctan\left(\frac{{\pi\tilde{{R}}}}{{b}}\right)-\arctan\left(\frac{{2\pi\tilde{{R}}}}{{Nb}}\right)\right)={RMS_ROG:.3g} \text{{ nm}}^2$',
    showarrow=False,
    font=dict(size=20)
)
fig.show()