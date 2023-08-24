## 3.2.1
### (a), (b)
$$
\begin{aligned}
P(Y = y _ 1 \vert do (X = x _ 1)) &= P _ m(Y = y _ 1 \vert X = x _ 1) \\
&= P_ m(Y=y _ 1 \vert X=x _ 1, Z=z _ 0)P(Z=z _ 0) + P_ m(Y=y _ 1 \vert X=x _ 1, Z=z _ 1)P(Z=z _ 1) \\
&= p _ 2(1-r) + p _ 4r \\
P(Y = y _ 1 \vert do (X = x _ 0)) &= p _ 1(1-r) + p _ 3r \\
P(Y = y _ 0 \vert do (X = x _ 1)) &= (1 - p _ 2)(1-r) + (1 - p _ 4)r \\
P(Y = y _ 0 \vert do (X = x _ 0)) &= (1 - p _ 1)(1-r) + (1 - p _ 3)r \\
\end{aligned}
$$

### (c)
$$
\begin{aligned}
ACE &= (p _ 2 - p _ 1)(1-r) + (p _ 4 - p _ 3)r \\
RD &= \frac{p _ 4q _ 2r + p _ 2q _ 1(1-r)}{q _ 1(1 - r)+q _ 2r} - \frac{p _ 3(1 - q _ 2)r + p _ 1(1 - q _ 1)(1-r)}{(1 - q _ 1)(1 - r)+(1 - q _ 2)r}
\end{aligned}
$$

When $q _ 1 = q _ 2$, the difference between the two is equal to zero. 

### (d)
(TODO) Set variables so that ACE is positive and RD is negative. 
