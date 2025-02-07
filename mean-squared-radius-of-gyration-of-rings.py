import numpy as np
import plotly.graph_objects as go

# Definitions of Scalars
b = 1 # not relevant due to normalization
N = 500

xlog_start = -1
xlog_end = 4

# Definition of arrays
p = np.linspace(1, np.floor(N/2), int(np.floor(N/2)))
X = np.logspace(xlog_start, xlog_end, num=100)

MSROG_sum = []
MSROG_arctan = []
for i in X:
    temp1 = 2*np.sum(((4*np.pi**2*p**2)/(N*b**2)+N/(i*b/np.pi)**2)**(-1))
    temp2 = i*b**2/np.pi**2*(np.arctan(i)-np.arctan(2/N*i))
    MSROG_sum.append(temp1)
    MSROG_arctan.append(temp2)

MSROG_sum = np.array(MSROG_sum)
MSROG_arctan = np.array(MSROG_arctan)


# Calculation of characteristic values of piR/b
char1 = 1
char2 = N/2

# Calculation of approximations between characteristic values
regime0 = np.logspace(xlog_start,np.log10(char1),10)
MSROG_regime0 = []
for i in regime0:
    temp = (i*b/np.pi)**2
    MSROG_regime0.append(temp)

regime1 = np.logspace(np.log10(char1),np.log10(char2),10)
MSROG_regime1 = []
for i in regime1:
    temp = b**2/(2*np.pi)*i
    MSROG_regime1.append(temp)

MSROG_regime0 = np.array(MSROG_regime0)
MSROG_regime1 = np.array(MSROG_regime1)

# Normalization
MSROG_sum_norm = MSROG_sum / b**2
MSROG_arctan_norm = MSROG_arctan / b**2
MSROG_regime0_norm = MSROG_regime0 / b**2
MSROG_regime1_norm = MSROG_regime1 / b**2

# Plot MSROG vs R=X*b/pi
fig = go.Figure()
fig.add_trace(go.Scatter(x=X, y=MSROG_sum_norm, mode='markers', name=r'$2\sum\limits_{p=1}^{N/2}\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}$', marker=dict(color='blue')))
fig.add_trace(go.Scatter(x=X, y=MSROG_arctan_norm, mode='lines', name=r'$R_g^2=\frac{{\tilde{{R}}b}}{{\pi}}\left(\arctan\left(\frac{{\pi\tilde{{R}}}}{{b}}\right)-\arctan\left(\frac{{2\pi\tilde{{R}}}}{{Nb}}\right)\right)$', line=dict(dash='solid', color='blue', width=2)))

fig.add_vline(x=char1, line_width=3, line_color="red", line=dict(dash='dash'))
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                         line=dict(color="red", width=2, dash="dash"),
                         name=r'$\tilde{R}=\frac{b}{\pi}$'))
fig.add_vline(x=char2, line_width=3, line_color="red")
fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines',
                         line=dict(color="red", width=2, dash="solid"),
                         name=r'$\tilde{R}=\frac{Nb}{2\pi}$'))

fig.add_trace(go.Scatter(x=regime0, y=MSROG_regime0_norm, mode='lines', name=r'$\frac{\tilde{R}^2}{b^2}$', line=dict(dash='dash', color='green', width=2)))
fig.add_trace(go.Scatter(x=regime1, y=MSROG_regime1_norm, mode='lines', name=r'$\frac{1}{2}\frac{\tilde{R}}{b}$', line=dict(dash='solid', color='green', width=2)))
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.update_layout(
    title=fr'$N = {N}$',
    xaxis_title=r'$\frac{\pi \tilde{R}}{b}$',
    yaxis_title=r'$R_g^2\Big/b^2$',
    xaxis=dict(tickformat='.0e'),
    yaxis=dict(tickformat='.0e'),
    legend_font_size=16,
    title_font_size=20
)
fig.show()