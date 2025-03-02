import numpy as np
import plotly.graph_objects as go

## Definitions
# User Input
b = 11 # length of Kuhn segment (Angstrom); no influence due to later normalization by b^2
N = 1000 
X = 10 # define R as multiple (X) of b

# Arrays
t_norm = np.logspace(-1, 8, num=100) # t_norm = t/tau_s
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
MSD = []

## Calculations
# characteristic radius of the potential
R = X*b

# MSD for t_norm values
A = 6/(3*np.pi**2) * b**2/N # MSD of center of mass
B = ((4*np.pi**2*p**2)/(N*b**2)+N/R**2)**(-1)
C = (2*p/N)**2 + (b/(np.pi*R))**2

for i in t_norm:
    temp = A*i + 4*np.sum(B*(1-np.e**(-C*i)))
    MSD.append(temp)

# mean square radius of gyration (MSROG)
MSROG = 2*np.sum(((4*np.pi**2*p**2)/(N*b**2)+N/(R)**2)**(-1))

# characteristic times and corresponding MSD
t_char0 = 1
t_char1 = 4*np.pi**2*MSROG**2/b**4
t_char2 = np.pi**2*MSROG*N/b**2
t_char = np.array([t_char0, t_char1, t_char2])

MSD_tchar0 = A*t_char[0] + 4*np.sum(B*(1-np.e**(-C*t_char[0])))
MSD_tchar1 = A*t_char[1] + 4*np.sum(B*(1-np.e**(-C*t_char[1])))
MSD_tchar2 = A*t_char[2] + 4*np.sum(B*(1-np.e**(-C*t_char[2])))

# approximations between characteristic times
t_regime0 = np.logspace(0,np.log10(t_char1),10)
MSD_regime0 = []
for i in t_regime0:
    temp = 2*b**2/np.pi**(3/2)*i**(1/2)
    MSD_regime0.append(temp)

t_regime1 = np.logspace(np.log10(t_char1),np.log10(t_char2),10)
MSD_regime1 = []
for i in t_regime1:
    temp = 2*MSROG
    MSD_regime1.append(temp)

t_regime2 = np.logspace(np.log10(t_char2),np.log10(np.max(t_norm)),10)
MSD_regime2 = []
for i in t_regime2:
    temp = 6/(3*np.pi**2) * b**2/N * i
    MSD_regime2.append(temp)

## Processing
# Conversion in numpy arrays
MSD = np.array(MSD)
MSD_regime0 = np.array(MSD_regime0)
MSD_regime1 = np.array(MSD_regime1)
MSD_regime2 = np.array(MSD_regime2)

# Normalization
MSROG_norm = MSROG/b**2
MSD_norm = MSD/b**2
MSD_norm_tchar0 = MSD_tchar0/b**2
MSD_norm_tchar1 = MSD_tchar1/b**2
MSD_norm_tchar2 = MSD_tchar2/b**2
MSD_norm_regime0 = MSD_regime0/b**2
MSD_norm_regime1 = MSD_regime1/b**2
MSD_norm_regime2 = MSD_regime2/b**2

## Plotting
# MSD vs t_norm
fig = go.Figure()
fig.add_trace(go.Scatter(x=t_norm, y=MSD_norm, mode='markers+lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle = \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}+4\sum\limits_{p=1}^{N/2}\left[\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}\left(1-e^{-\left(\left(\frac{2p}{N}\right)^2+\left(\frac{b}{\pi \tilde{R}}\right)^2\right)\frac{t}{\tau_s}}\right)\right]$'))

# limits
fig.add_trace(go.Scatter(x=[t_char0], y=[MSD_norm_tchar0], mode='markers', name=r'$\frac{t}{\tau_s}=1$', marker=dict(color='red', symbol='square', size=10)))
fig.add_trace(go.Scatter(x=[t_char1], y=[MSD_norm_tchar1], mode='markers', name=r'$\frac{t}{\tau_s}=4\pi^2\frac{R_g^4}{b^4}$', marker=dict(color='red', symbol='circle', size=10)))
fig.add_trace(go.Scatter(x=[t_char2], y=[MSD_norm_tchar2], mode='markers', name=r'$\frac{t}{\tau_s}=\pi^2\frac{R_g^2N}{b^2}$', marker=dict(color='red', symbol='diamond', size=10)))

# Approximations
fig.add_trace(go.Scatter(x=t_regime0, y=MSD_norm_regime0, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{2b^2}{\pi^{3/2}}\left(\frac{t}{\tau_s}\right)^{1/2}$', line=dict(dash='dot', color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime1, y=MSD_norm_regime1, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx 2R_g^2$', line=dict(dash='dash', color='green', width=2)))
fig.add_trace(go.Scatter(x=t_regime2, y=MSD_norm_regime2, mode='lines', name=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}$', line=dict(dash='solid', color='green', width=2)))

# value of MSROG
fig.add_annotation(
    x=np.log10(np.median(t_norm)), y=np.log10(0.75*np.max(MSD_norm)),
    text=fr'$\frac{{R_g^2}}{{b^2}}=\frac{{2}}{{b^2}}\sum\limits_{{p=1}}^{{N/2}}\left(\frac{{4\pi^2p^2}}{{Nb^2}}+\frac{{N}}{{\tilde{{R}}^2}}\right)^{{-1}}={MSROG_norm:.4g} $',
    showarrow=False,
    font=dict(size=20)
)

# Plot Properties
fig.update_layout(
    title=fr'$\tilde{{R}} = {X:.3g} b, N = {N}$',
    xaxis_title=r'$t/\tau_s$',
    yaxis_title=r'$\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle \Big/ b^2$',
    xaxis=dict(tickformat='.0e', title_font=dict(size=20)),
    yaxis=dict(tickformat='.0e', title_font=dict(size=20)),
    legend_font_size=16,
    title_font_size=20
)
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")

fig.show()

## Export
export = np.column_stack((t_norm, MSD_norm))
comment = f"R = {X}b,N = {N}"
column_titles = f"t/tau_s,MSD/b²"
header = f"{comment}\n{column_titles}"
np.savetxt('export.csv', export, fmt='%.2e', delimiter=',', header=header, comments='')