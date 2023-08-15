# 1.1

## 1.2.1
### (a)
Marriage is probably not the cause of income. It is likely that higher income leads to higher chance of marriage.

### (b)
It is clear that the number of fire fighters is not the cause of the number of fires. It is likely that the increasing number of fires causes the more number of fire fighters.

### (c)
It is clear that people are not late to meetings because they hurry. It is likely that they hurry because they are about to late.

## 1.2.2
| | Tim | Frank |
| ---- | ---- | ---- |
| right-handed | 38 / 80 | 10 / 20 |
| left-handed | 2 / 20 | 20 / 80 |
| total | 40 / 100 | 30 / 100 |

## 1.2.3
### (a)
Since the stone size is the cause of both treat selection and recovery, patients should examine the stone size-specific data.
```mermaid
graph LR;
stone_size-->treat;
stone_size-->recovery;
treat-->recovery;
```

### (b)
Easiness of the surgery is the cause of both the doctor and the success rate. Thus, you should examing the success rate of each doctor for the easy and difficult caases separately.
```mermaid
graph LR;
easiness-->doctor;
easiness-->success;
doctor-->success;
```

## 1.2.4 (TODO)

### (c)
```mermaid
graph LR;
depression-->lollipop;
depression-->recovery;
drug-->recovery;
drug-->lollipop;
```

## 1.3.1
variables: "receive drug or not", "receive lollipops or not", "depressed or not", "recover or not".

events: combination of variables and values, such as "receive drug and does not recover"

## 1.3.2
$$
\begin{aligned}
P(\mathrm{High ~ School}) &= \frac{(231 + 189)}{2440} \fallingdotseq 0.17 \\
P(\mathrm{High ~ School ~ OR ~ Female}) &= \frac{(231 + 1260)}{2440} \fallingdotseq 0.61 \\
P(\mathrm{High~School ~ \vert ~ Female}) &= \frac{189}{1260} = 0.15 \\
P(\mathrm{Female ~ \vert ~ High ~ School}) &= \frac{189}{231 + 189} = 0.45 \\
\end{aligned}
$$

## 1.3.3
### (a)
$$
\begin{aligned}
P(\mathrm{craps ~ \vert ~ 11}) &= \frac{P(\mathrm{11 ~ \vert ~ craps})P(\mathrm{craps})}{P(11)} \\
&= \frac{\frac{1}{18} \times \frac{1}{3}}{\frac{1}{18} \times \frac{1}{3} + \frac{1}{38} \times \frac{2}{3}} \\
&\fallingdotseq 0.51
\end{aligned}
$$

### (b)
$$
\begin{aligned}
P(\mathrm{roulette ~ \vert ~ 10}) &= \frac{P(\mathrm{10 ~ \vert ~ roulette})P(\mathrm{roulette})}{P(10)} \\
&= \frac{\frac{1}{38} \times \frac{1}{3}}{\frac{1}{38} \times \frac{1}{3} + \frac{1}{12} \times \frac{2}{3}} \\
&\fallingdotseq 0.14
\end{aligned}
$$

## 1.3.4
### (a), (b)
omit
### (c)
$$
\begin{aligned}
P(C _ D = B \vert C _ U = B) &= \sum _ {i \in \{1, 2, 3\}} P(C _ D = B, I = i \vert C _ U = B) \\
&= \frac{\sum _ {i \in \{1, 2, 3\}} P(C _ D = B, I = i, C _ U = B)}{P(C _ U = B)} \\
&= \frac{\frac{1}{3}}{\frac{1}{2}} \\
&= \frac {2}{3}
\end{aligned}
$$

### 1.3.5
Let $X$ be a door behind which the car exists. Let $Y$ be a door that the host opens. We can assume the participant chose the door $A$ without loss of generality.

$$
\begin{aligned}
P(X = A \vert Y = B) &= \frac{P(Y = B \vert X = A)P(X = A)}{P(Y = B)} \\
&= \frac{\frac{1}{2} \times \frac{1}{3}}{\frac{1}{2} \times \frac{1}{3} + 0 + 1 \times \frac{1}{3}} \\
&= \frac{1}{3}
\end{aligned}
$$

Since $P(X=B \vert Y=B) = 0$, $P(X=C \vert Y=B) = \frac{1}{3}$ is derived. The same thing holds if you change $Y=B$ to $Y=C$. Thus, the probability of winning the car will be doubled if you change the door.
