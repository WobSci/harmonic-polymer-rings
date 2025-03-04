import numpy as np
import plotly.graph_objects as go

## Definitions
# User Input
b = 11 # length of Kuhn segment (Angstrom); no influence due to later normalization by b^2
X = 100 # X=R/b, to later define R as multiple of b

# range of logarithmic x-axis
Nlog_start = 1
Nlog_end = 4

# Arrays
N_log = np.logspace(Nlog_start,Nlog_end, 100)
N_int = np.round(N_log).astype(int)
N = np.unique(N_int)
MSROG_sum = [] # mean squared radius of gyration of polymer rings, with potential
MSROG_lin = [] # mean squared radius of gyration of polymer chains, no potential
MSROG_ring = [] # mean squared radius of gyration of polymer rings, no potential, "ideal"

## Calculations
#  Scalars
R = X*b # characteristic radius of the potential

# Arrays
for i in N:
    p = np.linspace(1, np.floor(i/2), int(np.floor(i/2)))
    temp1 = 2*np.sum(((4*np.pi**2*p**2)/(i*b**2)+i/(R)**2)**(-1))
    temp2 = (i*b**2)/6
    temp3 = (i*b**2)/12
    MSROG_sum.append(temp1)
    MSROG_lin.append(temp2)
    MSROG_ring.append(temp3)

# Calculation of chararcteristiv value of N
# For a very weak potential R²>>(N²b²)/(2pi)² the MSROG of ring segments with harmonic potential equals the MSROG of ring segments without harmonic potential   
N_char = 2*np.pi*X
p_char = p = np.linspace(1, np.floor(N_char/2), int(np.floor(N_char/2)))
MSROG_char = 2*np.sum(((4*np.pi**2*p**2)/(N_char*b**2)+N_char/(R)**2)**(-1)) # value of MSROG when R = Nb/2pi

# Processing
MSROG_sum = np.array(MSROG_sum)
MSROG_lin = np.array(MSROG_lin)
MSROG_ring = np.array(MSROG_ring)
MSROG_char = np.array(MSROG_char)

# Normalization
MSROG_sum_norm = MSROG_sum / b**2
MSROG_lin_norm = MSROG_lin / b**2
MSROG_ring_norm = MSROG_ring / b**2
MSROG_char_norm = MSROG_char / b**2

# Plot MSROG vs N
fig = go.Figure()
fig.add_trace(go.Scatter(x=N, y=MSROG_sum_norm, mode='markers', name=r'$R_g^2=2\sum\limits_{p=1}^{N/2}\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}$', marker=dict(color='blue')))
fig.add_trace(go.Scatter(x=N, y=MSROG_lin_norm, mode='lines', name=r'$R_{g,lin}^2=\frac{Nb^2}{6}$', marker=dict(color='black')))
fig.add_trace(go.Scatter(x=N, y=MSROG_ring_norm, mode='lines', name=r'$R_{g,ring}^2=\frac{Nb^2}{12}$', marker=dict(color='blue')))
fig.add_trace(go.Scatter(x=[N_char], y=[MSROG_char_norm], mode='markers', name=r'$R_g^2\left(\tilde{R}=\frac{Nb}{2\pi}\right)$', marker=dict(color='red')))
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(
    title=fr'$\tilde{{R}} = {X}b$',
    xaxis_title=r'$N$',
    yaxis_title=r'$R_g^2\Big/b^2$',
    xaxis=dict(tickformat='.0e', title_font=dict(size=20)),
    yaxis=dict(tickformat='.0e', title_font=dict(size=20)),
    legend_font_size=16,
    title_font_size=20
)
fig.show()

## Export
export = np.column_stack((N, MSROG_sum_norm))
comment = f"R = {X}b,"
column_titles = f"N,MSROG/b²"
header = f"{comment}\n{column_titles}"
np.savetxt('export.csv', export, fmt='%.2e', delimiter=',', header=header, comments='')