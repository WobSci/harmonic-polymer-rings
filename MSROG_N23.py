import numpy as np
import plotly.graph_objects as go

# Definitions of Scalars
b = 11 # no influence due to normalization of MSROG by b^2
X = 11/1.91
X_round = np.round(X,2) # only for display in plot and csv export
L = b/X
N = 100
beta = 3.25

xlog_start = -1
xlog_end = 4

# Definition of arrays
N_log = np.logspace(1,4, 100)
N_int = np.round(N_log).astype(int)
N = np.unique(N_int)
MSROG_sum = []
MSROG_lin = []
MSROG_ring = []
MSROG_limit = []

# Calculation of mean squared radius of gyration (MSROG)
for i in N:
    p = np.linspace(1, np.floor(i/2), int(np.floor(i/2)))
    temp1 = 2*b**2/(4*np.pi**2)*i*np.sum((p**2+i**(2/3)/(4*np.pi**2*beta)*(b/L)**(4/3))**(-1))
    temp2 = (i*b**2)/6
    temp3 = (i*b**2)/12
    temp4 = beta**(1/2)/2*i**(2/3)*(L/b)**(2/3)*b**2
    MSROG_sum.append(temp1)
    MSROG_lin.append(temp2)
    MSROG_ring.append(temp3)
    MSROG_limit.append(temp4)

MSROG_sum = np.array(MSROG_sum)
MSROG_lin = np.array(MSROG_lin)
MSROG_ring = np.array(MSROG_ring)
MSROG_limit = np.array(MSROG_limit)

# Normalization
MSROG_sum_norm = MSROG_sum / b**2
MSROG_lin_norm = MSROG_lin / b**2
MSROG_ring_norm = MSROG_ring / b**2
MSROG_limit_norm = MSROG_limit / b**2

# Plot MSROG vs N
fig = go.Figure()
fig.add_trace(go.Scatter(x=N, y=MSROG_sum_norm, mode='markers', name=r'$R_g^2=2\frac{Nb^2}{4\pi^2}\sum\limits_{p=1}^{N/2}\left(p^2+\frac{1}{4\pi^2}\frac{N^{2/3}}{\beta}\left(\frac{b}{L}\right)^{4/3}\right)^{-1}$', marker=dict(color='blue')))
fig.add_trace(go.Scatter(x=N, y=MSROG_lin_norm, mode='lines', name=r'$R_{g,lin}^2=\frac{Nb^2}{6}$', marker=dict(color='black')))
fig.add_trace(go.Scatter(x=N, y=MSROG_ring_norm, mode='lines', name=r'$R_{g,ring}^2=\frac{Nb^2}{12}$', marker=dict(color='blue')))
fig.add_trace(go.Scatter(x=N, y=MSROG_limit_norm, mode='lines', name=r'$R_{g}^2\left(\frac{Nb}{2\pi}\gg\tilde{R}\gg\frac{b}{\pi}\right)\approx\frac{1}{2}\beta^{1/2}N^{2/3}\left(\frac{L}{b}\right)^{2/3}b^2$', marker=dict(color='red')))
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(
    title=fr'$\beta = {beta} \text{{, }} \frac{{b}}{{L}} \approx {X_round}$',
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
comment = f"beta = {beta},b/L = {X_round}"
column_titles = f"N,R_g^2/b^2"
header = f"{comment}\n{column_titles}"
np.savetxt('export.csv', export, fmt='%.2e', delimiter=',', header=header, comments='')