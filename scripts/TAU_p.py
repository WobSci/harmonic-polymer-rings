import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# Set the default renderer to 'browser' when running as a script
import __main__ as main
if hasattr(main, '__file__'):
    pio.renderers.default = 'browser'

## Definitions
# User Input
X = 10 # define R as multiple (X) of b

# Arrays
p_N = np.logspace(-5, np.log10(0.5), 64) # x-axis = p/N

tau_ratio = 4 * ( (p_N)**2 + 1/(4 * np.pi**2 * X**2)) # eq. 12 normalized to tau_s/tau_p
p_N_limit = 1 / (2*np.pi * X) # p/N << p_N_limit --> dependence of tau_p on p ceases
tau_ratio_min = 1/(np.pi**2 * X**2)
tau_ratio_max = 1 + tau_ratio_min

## Plotting
# MSD vs t_norm
fig = go.Figure()
fig.add_trace(go.Scatter(x=p_N, y=tau_ratio, mode='markers+lines', name=r'$\tau_s/\tau_p$'))
fig.add_shape(
    type="line",
    x0=p_N_limit, x1=p_N_limit,
    y0=10**np.floor(np.log10((1/(np.pi**2 * X**2)))), y1=2,
    line=dict(color="Red", width=2, dash="dot"),
    name=r'$\frac{p}{N}=\frac{b}{2\pi\tilde{R}}$',
    showlegend=True
)

# Plot Properties
fig.update_layout(
    title=fr'$\tilde{{R}} = {X:} b$',
    xaxis_title=r'$\frac{p}{N}\big|_{p=1}^{N/2}$',
    yaxis_title=r'$\tau_s/\tau_p$',
    xaxis=dict(title_font=dict(size=20)),
    yaxis=dict(title_font=dict(size=20)),
    legend_font_size=16,
    title_font_size=20
)
fig.update_xaxes(type="log", exponentformat="power")
fig.update_yaxes(type="log", exponentformat="power")

fig.show()



## Export
export = np.column_stack((p_N, tau_ratio))
comment = f"R = {X}b"
column_titles = f"p/N,tau_s/tau_p"
header = f"{comment}\n{column_titles}"
np.savetxt('export.csv', export, delimiter=',', header=header, comments='')