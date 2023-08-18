## 1.2
- Simpson's paradox: A statistical association that holds for an entire population is reversed in every subpopulation
    - In some cases it is appropriate to see agregated data, while in other cases we should see data separated based on groups.

## 1.3
- Orthogonality principle: If we write $Y$ as a liniar combination of $X _ 1$ ~ $X _ k$ plus a noise term $\epsilon$, regardless of the true distribution of $Y$, $X _ 1$, ..., and $X _ k$, the least-square coefficients are obtained when $Cov(\epsilon, X _ i) = 0$ for any i.

## 1.5
- SCM
    - components: exogeneous variable $U$, endogenous variables $V$, and functions $f$
    - $f$ assigns values to each variable in $V$ based on the values of other variables.
- In a graphical causal model, $Y$ is not necessarilly a cause of $X$ even when $X$ is a descendant of $Y$.
- The difference between SCM and graphical causal model
    - Edges in a graphical causal model do not tell us the exact underlying functions between variables. Thus, A graphical causal models contain less information than SCMs.
- Product decomposition in a graphical causal model --> More accurate estimation of joint probabilities