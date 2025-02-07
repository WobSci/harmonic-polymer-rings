import numpy as np
import plotly.graph_objects as go

# Definitions of Scalars
b = 100*10**(-10)
N = 500
#R = 10*b/np.pi

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
MSROG_sum_norm = MSROG_sum * (np.pi/b)**2
MSROG_arctan_norm = MSROG_arctan * (np.pi/b)**2
MSROG_regime0_norm = MSROG_regime0 * (np.pi/b)**2
MSROG_regime1_norm = MSROG_regime1 * (np.pi/b)**2

# Plot MSROG vs R=X*b/pi
fig = go.Figure()
fig.add_trace(go.Scatter(x=X, y=MSROG_sum_norm, mode='markers', name='sum'))
fig.add_trace(go.Scatter(x=X, y=MSROG_arctan_norm, mode='lines', name='arctan', line=dict(dash='solid', color='blue', width=2)))
fig.add_vline(x=char1, line_width=3, line_color="red")
fig.add_vline(x=char2, line_width=3, line_color="red")
fig.add_trace(go.Scatter(x=regime0, y=MSROG_regime0_norm, mode='lines', name=r'$\frac{1}{2}Rb$', line=dict(dash='dash', color='green', width=2)))
fig.add_trace(go.Scatter(x=regime1, y=MSROG_regime1_norm, mode='lines', name=r'$R^2$', line=dict(dash='solid', color='green', width=2)))
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