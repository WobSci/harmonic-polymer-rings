This repository contains the Python scripts used to visualize the mean squared displacement and radius of gyration of polymer rings based on the Rouse model modified by a spherical attractive harmonic potential as presented in the [Publication].
A snapshot of this repository at the status of the article publication is available on Zenodo, DOI: [10.5281/zenodo.14956318](https://doi.org/10.5281/zenodo.14956318). 
- Language: [Python](https://www.python.org/) (3.13.1)
- Packages: [NumPy](https://numpy.org/) (2.2.3), [Plotly](https://plotly.com/python/) (6.0.0)

# Script Overview
- [MSD_t.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSD_t.py) calculates and plots the time-evolution of the mean squared displacement. 
- [MSROG_R.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_R.py) calculates and plots the mean squared radius of gyration vs the characteristic radius $\tilde{R}$ of the potential for a fixed number $N$ of Kuhn segments. $N$ can be freely chosen by the user.
- [MSROG_N.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N.py) calculates and plots again the mean squared radius of gyration vs the number $N$ of Kuhn segments for a fixed characteristic radius $\tilde{R}$ of the potential. $\tilde{R}$ can be freely choosen by the user as a multiple $X$ of the length $b$ of a Kuhn segment $b$.
- [MSROG_N_RpropN.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N_RpropN.py) calculates the mean squared radius of gyration vs the number $N$ of Kuhn segments for a fixed characteristic radius $\tilde{R}$ of the potential. $N$ and $\tilde{R}$ are not longer independent from each other but related via $\tilde{R}^2 = \beta N^{4/3}L^{4/3}b^{2/3}=\beta N^{4/3}\left(\frac{L}{b}\right)^{4/3}b^2$ with the numeric coefficient $\beta = \left(\frac{3}{\pi}\right)^2\left(\frac{\pi}{6}\right)^{2/3}\left(\frac{R_g}{R_sf}\right)$. The user has to provide the polymer charachteristic values for the length $b$ of the Kuhn segment, the packing length $L$, the radius of gyration $R_g$ and the radius $R_{sf}$ of the polymer when it would be contracted to a spherical globule.




## MSROG_N23.py
This script calculates the mean squared radius of gyration of the ring macromolecule according to eguation [X], i.e. where the characteristic radius of the harmonic potential $\tilde{R}$ is not independent from the number of Kuhn segments $N$ of the macromolecule.

The relation between these two variables is described by 
```math
\tilde{R}^2 = \frac{\beta}{b^2}\left(\frac{N}{\rho_s}\right)^{4/3}
```
where $\beta$ is a dimensionless numerical coefficient which can be estimated with $\beta = \left(\frac{3}{\pi}\right)^2\left[\frac{\rho_s}{\tilde{\rho}_s(0)}\right]^{4/3}$. $\rho_s$ is the concentration of Kuhn segments in the melt, while $\tilde{\rho}_s$ is the concentration of the intrinsic ring segments inside a globule. Using the packing length $L$ defined as $L^{-1}=\rho_s b$ the characteristic radius of the potential can be expressed as 
```math
\tilde{R}^2 = \beta N^{4/3}L^{4/3}b^{2/3}=\beta N^{4/3}\left(\frac{L}{b}\right)^{4/3}b^2
```
With that the mean squared radius of gyration can be written as
```math
R_g^2=2\frac{Nb^2}{4\pi^2}\sum\limits_{p=1}^{N/2}\left(p^2+\frac{1}{4\pi^2}\frac{N^{2/3}}{\beta}\left(\frac{b}{L}\right)^{4/3}\right)^{-1}
```
This equation is calculated by `MSROG_N23.py` for a range of different $N$ and its normalization by $b^2$ is then plotted. 