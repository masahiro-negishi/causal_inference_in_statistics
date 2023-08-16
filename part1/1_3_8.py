import numpy as np

X = np.array([6, 3, 4, 6, 6, 5, 1, 3, 6, 3, 5, 4])
Z = np.array([3, 4, 6, 2, 4, 3, 5, 5, 5, 5, 3, 5])
Y = X + Z
n = len(X)

E_X = np.sum(X) / n
E_Y = np.sum(Y) / n

E_Y_cond_X = []
E_X_cond_Y = []
for x in [1, 2, 3, 4, 5, 6]:
    if x in X:
        E_Y_cond_X.append(np.sum(Y[X==x]) / len(Y[X==x]))
    else:
        E_Y_cond_X.append("cannot be estimated")
for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    if y in Y:
        E_X_cond_Y.append(np.sum(X[Y==y]) / len(X[Y==y]))
    else:
        E_X_cond_Y.append("cannot be estimated")

V_X = np.sum((X - E_X) ** 2) / n
V_Y = np.sum((Y - E_Y) ** 2) / n
Cov_X_Y = np.sum((X - E_X) * (Y - E_Y)) / n
rho_X_Y = Cov_X_Y / (V_X**0.5 * V_Y**0.5)
Cov_X_Z = np.sum((X - E_X) * (Z - np.sum(Z) / n)) / n

print(f"E[X] = {E_X}")
print(f"E[Y] = {E_Y}")
for i, x in enumerate([1, 2, 3, 4, 5, 6]):
    print(f"E[Y|X={x}] = {E_Y_cond_X[i]}")
for i, y in enumerate([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    print(f"E[X|Y={y}] = {E_X_cond_Y[i]}")
print(f"V[X] = {V_X}")
print(f"V[Y] = {V_Y}")
print(f"Cov[X, Y] = {Cov_X_Y}")
print(f"rho[X, Y] = {rho_X_Y}")
print(f"Cov[X, Z] = {Cov_X_Z}")
