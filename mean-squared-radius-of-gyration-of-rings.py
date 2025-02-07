import numpy as np
import plotly.graph_objects as go

# Definitions of Scalars
b = 100*10**(-10)
N = 5000
#R = 10*b/np.pi

# Definition of arrays
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
X = np.logspace(-1, 4, num=100)

MSROG_sum = []
MSROG_arctan = []
for i in X:
    temp1 = 2*np.sum(((4*np.pi**2*p**2)/(N*b**2)+N/(i*b/np.pi)**2)**(-1))
    temp2 = i*b**2/np.pi**2*(np.arctan(i)-np.arctan(2/N*i))
    MSROG_sum.append(temp1)
    MSROG_arctan.append(temp2)

MSROG_sum = np.array(MSROG_sum)
MSROG_arctan = np.array(MSROG_arctan)

# Normalization
MSROG_sum_norm = MSROG_sum * (np.pi/b)**2
MSROG_arctan_norm = MSROG_arctan * (np.pi/b)**2

# Plot MSROG vs R=X*b/pi
fig = go.Figure()
fig.add_trace(go.Scatter(x=X, y=MSROG_sum_norm, mode='markers+lines', name='sum'))
fig.add_trace(go.Scatter(x=X, y=MSROG_arctan_norm, mode='lines', name='arctan', line=dict(dash='solid', color='green', width=2)))
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(
    title='MSROG vs. R',
    xaxis_title=r'$\frac{\pi R}{b}$',
    yaxis_title=r'$R_g^2\cdot\left(\frac{\pi}{b}\right)^2$',
    xaxis=dict(tickformat='.0e'),
    yaxis=dict(tickformat='.0e'),
    legend_font_size=16,
    title_font_size=20
)
fig.show()