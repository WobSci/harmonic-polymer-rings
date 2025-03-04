This repository contains the Python scripts used to visualize the mean squared displacement and radius of gyration of polymer rings based on the Rouse model modified by a spherical attractive harmonic potential as presented in the [Publication].
A snapshot of this repository at the status of the article publication is available on Zenodo, DOI: [10.5281/zenodo.14956318](https://doi.org/10.5281/zenodo.14956318). 
- Language: [Python](https://www.python.org/) (3.13.1)
- Packages: [NumPy](https://numpy.org/) (2.2.3), [Plotly](https://plotly.com/python/) (6.0.0)

# Getting Started
The Python scripts can be executed in the browser using GitHub Codespaces. 
- Click the green `<> Code` button at the top right of the repository
- Select the `Codespaces` tab
- Click `Create codespace on main`
- The codespace uses [VS Code](https://code.visualstudio.com/docs) as editor
- You may be asked/need to install the VS Code Python extension
- Use `STRG + SHIFT + E` to open the `EXPLORER` and navigate to the Python scripts in the folder `Scripts`
- Open a script by clicking on it and execute  with the $\vartriangleright$ button in the top right
- The plots open in a new browser tab

To explore different variables, change the values listed below `# User Input` starting at line 5 in the scripts.

# Script Overview
Each script exports its results into a csv file called `export.csv`.
## Mean Squared Displacement
- [MSD_t.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSD_t.py) calculates and plots the time-evolution of the mean squared displacement. The number $N$ of Kuhn segments and the characteristic radius $\tilde{R}$ of the potential can be freely chosen.

## Mean Squared Radius of Gyration
- [MSROG_R.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_R.py) calculates and plots the mean squared radius of gyration vs the characteristic radius $\tilde{R}$ of the potential for a fixed number $N$ of Kuhn segments. $N$ can be freely chosen.
- [MSROG_N.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N.py) calculates and plots again the mean squared radius of gyration vs the number $N$ of Kuhn segments for a fixed characteristic radius $\tilde{R}$ of the potential. $\tilde{R}$ can be freely choosen as a multiple $X$ of the length $b$ of a Kuhn segment.
- [MSROG_N_RpropN.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N_RpropN.py) calculates and plota the mean squared radius of gyration vs the number $N$ of Kuhn segments for a fixed characteristic radius $\tilde{R}$ of the potential. $N$ and $\tilde{R}$ are not longer independent from each other.
The user has to provide the polymer charachteristic values for the length $b$ of the Kuhn segment, the packing length $L$, the (experimentally determined) radius of gyration $R_g$ and the radius $R_{sf}$ the polymer would have when contracted to a spherical globule. 

# Equations
## Mean Squared Displacement
The mean squared displacement in [MSD_t.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSD_t.py) is calculated according to
```math
\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle = \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}+4\sum\limits_{p=1}^{N/2}\left[\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}\left(1-e^{-\left(\left(\frac{2p}{N}\right)^2+\left(\frac{b}{\pi \tilde{R}}\right)^2\right)\frac{t}{\tau_s}}\right)\right]
```
Additionally plotted are
- the characteristic limits 
  - $\frac{t}{\tau_s}=1$
  - $\frac{t}{\tau_s}=4\pi^2\frac{R_g^4}{b^4}$
  - $\frac{t}{\tau_s}=\pi^2\frac{R_g^2N}{b^2}$
- the approximations between the characteristic limits
  - $\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{2b^2}{\pi^{3/2}}\left(\frac{t}{\tau_s}\right)^{1/2}$
  - $\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx 2R_g^2$
  - $\left\langle\left(\vec{r}_n\left(t\right)-\vec{r}_n\left(0\right)\right)^2\right\rangle\approx \frac{6}{3\pi^2}\frac{b^2}{N}\frac{t}{\tau_s}$

## Mean Squared Radius of Gyration
The equations to calculate the mean squared radius of gyration in [MSROG_R.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_R.py) and [MSROG_N.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N.py) are
```math
R_g^2=2\sum\limits_{p=1}^{N/2}\left(\frac{4\pi^2p^2}{Nb^2}+\frac{N}{\tilde{R}^2}\right)^{-1}
```
and
```math
R_g^2=\frac{{\tilde{{R}}b}}{{\pi}}\left(\arctan\left(\frac{{\pi\tilde{{R}}}}{{b}}\right)-\arctan\left(\frac{{2\pi\tilde{{R}}}}{{Nb}}\right)\right)
```
In [MSROG_R.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_R.py) additionally plotted are
- the characteristic limits 
  - $\tilde{R}=\frac{b}{\pi}$
  - $\tilde{R}=\frac{Nb}{2\pi}$ 
- the approximations
  - $R_g^2\left(\tilde{R}\ll\frac{b}{\pi}\right)=\tilde{R}^2$
  - $R_g^2\left(\frac{b}{\pi}\ll\tilde{R}\ll\frac{Nb}{2\pi}\right)=\tilde{R}^2$

In [MSROG_N.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N.py) additionally plotted are
- the mean squared radii of gyration of 
  - linear polymers $R_{g,lin}^2=\frac{Nb^2}{6}$
  - ideal ring polymers $R_{g,ring}^2=\frac{Nb^2}{12}$
- the value of the mean squared radius of gyration when $\tilde{R}=\frac{Nb}{2\pi}$

In [MSROG_N_RpropN.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N_RpropN.py) $\tilde{R}$ and $N$ are not longer independent from each other but related via
```math
\tilde{R}^2 = \beta N^{4/3}L^{4/3}b^{2/3}=\beta N^{4/3}\left(\frac{L}{b}\right)^{4/3}b^2
```
with the numeric coefficient
```math 
\beta = \left(\frac{3}{\pi}\right)^2\left(\frac{\pi}{6}\right)^{2/3}\left(\frac{R_g}{R_{sf}}\right)
```
The radius of the polymer contracted to a spherical globule can be estimated via
```math
R_{sf} = \left[\frac{3}{4\pi}\frac{m_p}{\rho}M\right]^{1/3}
```
with the proton mass $m_p$the density of the polymer melt $\rho$ and the polymers molecular mass $M$.
The mean squared radius of gyration is then calculated according to
```math
R_g^2=2\frac{Nb^2}{4\pi^2}\sum\limits_{p=1}^{N/2}\left(p^2+\frac{1}{4\pi^2}\frac{N^{2/3}}{\beta}\left(\frac{b}{L}\right)^{4/3}\right)^{-1}
```
Additionally plotted are again the mean squared radii of gyration of linear and ideal ring polymers. Furthermore the $N$ dependence of the mean squared radius of gyration is plotted for $\left(\frac{b}{\pi}\ll\tilde{R}\ll\frac{Nb}{2\pi}\right)$: 
```math
R_g^2 = \frac{1}{2}\beta^{1/2}N^{2/3}\left(\frac{L}{b}\right)^{2/3}b^2
```

# Variables
| Variable | Name (Comment) | Comment |
| :------------- | :------------- | :------------- |
| $b$  | length of a Kuhn segment | $b_{PEO}\approx 11\text{ }\mathring{A}$ [1], actual value only relevant in [MSROG_N_RpropN.py](https://github.com/WobSci/harmonic-polymer-rings/blob/main/scripts/MSROG_N_RpropN.py), due to normalization by $b^2$ in the scripts |
| $\beta$  | numeric coefficient  |  proportional to the fraction of the globule's own segments density relative to the density of all segments at the globule's center of mass  |
| $L$  | packing length  |  $L_{PEO}\approx 1.91\text{ }\mathring{A}$ [2]  |
| $M$  | molecular mass  |    |
| $m_p$  | proton mass  |    |
| $N$  | number of Kuhn segments | size of polymer |
| $p$  | Rouse modes | runs from 1 to $N/2$  |
| $\tilde{R}$  | characteristic radius of the potential | reflects the strength of the potential. The smaller $\tilde{R}$, the stronger the potential. Expressed in multiples X of $b$ |
| $R_g^2$  | mean squared radius of gyration  |    |
| $R_g$  | radius of gyration  |  $R_{g,PEO}^{96000\text{ }g/mol}\approx 49.5\text{ }\mathring{A}$ [3,4]  |
| $R_{sf}$  | radius of a polymer contracted to a spherical globule  |  $R_{sf,PEO}^{96000\text{ }g/mol}\approx 33.6\text{ }\mathring{A}$  |
| $\rho$  | density of polymer melt  |  $\rho_{PEO}\approx 1.08\text{ }\frac{g}{cm^2}$ [2] |
| $t$  | time  |    |
| $\tau_s$  | segmental relaxation time  |    |

[1] M. Rubinstein, R. H. Colby, Polymer Physics, Oxford University Press, 2003. Table 2.1, p. 53

[2] L. J. Fetters, D. J. Lohse, D. Richter, T. A. Witten, A. Zirkel in Physical properties of Polymers Handbook (Ed. J. E. Mark), Springer 2007, Ch. 25. Table 25.5

[3] M. Kruteva, M. Monkenbusch, J. Allgaier, O. Holderer, S. Pasini, I. Hoffmann, D. Richter, Phys. Rev. Lett. 2020, 125, 238004. DOI: [10.1103/PhysRevLett.125.238004](https://www.doi.org/10.1103/PhysRevLett.125.238004). Table 1

[4] M. Kruteva, J. Allgaier, M. Monkenbusch, I. Hoffmann, D. Richter, J. Rheol. 2021, 65, 713–727. DOI: [10.1122/8.0000206](https://www.doi.org/10.1122/8.0000206). Table 1