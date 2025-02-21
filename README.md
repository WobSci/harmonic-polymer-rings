This repository contains code to calculate some equations from [Publication] and export the data to be used in the publications figures.

## MSROG_N23.py
This script calculates the mean squared radius of gyration of the ring macromolecule according to eguation [X], i.e. where the characteristic radius of the harmonic potential $\tilde{R}$ is not independent from the number of Kuhn segments $N$ of the macromolecule.

The relation between these two variables is described by $$\tilde{R} = \frac{\beta}{b^2}\left(\frac{N}{\rho_s}\right)^{4/3}$$
where $\beta$ is a dimensionless numerical coefficient which can be estimated with $\beta = \left(\frac{3}{\pi}\right)^2\left[\frac{\rho_s}{\tilde{\rho}_s(0)}\right]^{4/3}$. $\rho_s$ is the concentration of Kuhn segments in the melt, while $\tilde{\rho}_s$ is the concentration of the intrinsic Kuhn segments inside a globule.