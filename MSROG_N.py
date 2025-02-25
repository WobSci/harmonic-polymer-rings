import numpy as np
import plotly.graph_objects as go

# Definitions of Scalars (User Choice)
b = 1 # no influence due to normalization of MSROG by b^2
X = 100 # define R as multiple (X) of b

# Calculation of the radius of the potential
R = X*b

# Specify the first and last N (logarithmic scale)
Nlog_start = 1
Nlog_end = 4

# Definition of arrays
N_log = np.logspace(Nlog_start,Nlog_end, 100)
N_int = np.round(N_log).astype(int)
N = np.unique(N_int)
MSROG_sum = []
MSROG_lin = []
MSROG_ring = []

# Calculation of mean squared radius of gyration (MSROG)
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
MSROG_char = 2*np.sum(((4*np.pi**2*p**2)/(N_char*b**2)+N_char/(R)**2)**(-1))

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
fig.add_trace(go.Scatter(x=[N_char], y=[MSROG_char_norm], mode='markers', name=r'$\tilde{R}=\frac{N^2b^2}{4\pi^2}$', marker=dict(color='red')))
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
column_titles = f"N,R_g^2/b^2 (eq.9 sum)"
header = f"{comment}\n{column_titles}"
np.savetxt('export.csv', export, fmt='%.2e', delimiter=',', header=header, comments='')