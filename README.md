This repository contains code to calculate some equations from [Publication] and export the data to be used in the publications figures.

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