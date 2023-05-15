---
marp: true
# theme: uncover
theme: default
# _class: invert
footer: '无模型-P,R未知  -> 蒙特卡洛方法 -> 基于所有经验E的RL'
paginate: true
---


# Monte Carlo Learning

## 复习：Belman方程BE与Belman最优方程BOE

 $\tau_{t} = S_t \stackrel{A_t}{\rightarrow} S_{t+1},R_{t+1} \stackrel{A_{t+1}}{\rightarrow} S_{t+2},R_{t+2} \stackrel{A_{t+2}}{\rightarrow} S_{t+3},R_{t+3}....$

其中，$S_t,{A_t},R_{t}$均为随机变量

For $\tau_{t}$, $G_t=R_{t+1}+\gamma R_{t+2}+ {\gamma}^2 R_{t+3}$, $G_t$是随机变量

For some s, state value is defined as： $v_\pi(s)=\mathbb E[{G_t|S_t=s}]$

---
|      | matrix-vector form                                           |                      elementewise form                       |
| ---- | ------------------------------------------------------------ | :----------------------------------------------------------: |
| BE   | $v_\pi=r_\pi +\gamma P_\pi v_\pi$<br />$q_\pi(s,a)=r_\pi(a)+\gamma P_\pi(s,a) v_\pi$ | ![](.\images\BE_1.png)<br/> $v_\pi(s_i)=r_\pi (s_i)+\gamma \underset {s_j}{\sum}p_\pi(s_j|s_i)v_\pi(s_j)$<br />$q_\pi(s_i,a)=r_\pi (s_i,a)+\gamma \underset {s_j}{\sum}p_\pi(s_j|s_i,a)v_\pi(s_j) $<br />= $\underset {r}{\sum}p_\pi(r|s,a) r+\gamma \underset {s_j}{\sum}p_\pi(s_j|s_i,a)v_\pi(s_j)$ |
| BOE  | $v=\underset {\pi}{max}(r_\pi+\gamma P_{\pi}v)$              |                    ![](.\images\BOE1.png)                    |



---

## 本节目标

* **Belman最优方程**：$v=f(v) = \underset {\pi}{max}(r_\pi+\gamma P_{\pi}v)$
* **求解状态值$v$**：
  * 以前假设： 环境模型已知 $r_\pi,P_\pi$  $\leftarrow$ model-based 值迭代/策略迭代
  * 问题：环境模型未知$r_\pi,P_\pi$    $\leftarrow$  利用数据！大数定理

* Model Free RL model  需要大量的数据 - 遍历问题域中{state, action}  
  * MC  Basic   - 最简单的MC-based RL algorithm   1个episode
  * MC  Exploring Starts - 更有效地利用交互获取的数据  多个episode
  * MC without exploring starts - MC $\epsilon$- Greedy
  * 总结下概念
    * Exploiting and Exploration 利用/探索
    *  占用度量


---
## 目 录
### 1. 例子：无环境模型下的随机变量的取值-sampling
### 2. MC Basic 算法
### 3. MC Exploring Starts 算法
### 4. MC without Exploring Starts - MC $\epsilon$- Greedy算法

---

## 看个例子：理解Monte Carlo预测
-  **Example: Flip a coin**

  - The result (either head or tail) is denoted as a random variable *X*

    - if the result is head, then $X = +1$

    - if the result is tail, then  $X = -1$

  - 求解： $\mathbb E[X]$

- **Case 1：Model-based**

  - 假设/已知有概率模型 $p(X=1)=0.5,P(X=-1)=0.5$
    - $\mathbb E[X]== \underset {x}{\sum}xp(x)=1 \times 0.5 +(-1) \times 0.5=0$

- **Case 2: Model free 不知道$p$概率的准确分布**  - 没有模型，就得利用**数据**！


---

## 看个例子：理解Monte Carlo预测

-  **Example: Flip a coin**

  - 求解： $\mathbb E[X]$

- **Case 2: Model free 不知道$p$概率的准确分布**  - 没有模型，就得利用**数据**！

  - *Idea:* Flip the coin many times, and then calculate the average of the outcomes.
  - Suppose we get a sample sequence: $ {x_1,x_2,...,x_N}.$

  ​              平均值近似表示期望：$\mathbb E[X]  \approx \overline{x}= \frac{1}{N} \underset{j=1} \sum^{N}x_j$

  - This is **the idea of Monte Carlo estimation!**




---

- **Question:** Is the Monte Carlo estimation accurate?

  *•* When *N* is *small*, the approximation is inaccurate.

  *•* As *N* *increases*, the approximation becomes more and more accurate

- Law of Large Numbers - **采样要求是iid(独立同分布！)**

  ![](.\images\MC1.png)

---

## Monte Carlo estimation

Summary:
- Monte Carlo estimation refers to a broad class of techniques that rely on repeated random sampling **to solve approximation problems.**
- Why we care about Monte Carlo estimation?  
  - Because it does not require the model!
- Why we care about mean estimation? 
  - Because state value and action value are  defined as **expectations of random variables**!
---

##  Convert policy iteration  to be model-free

算法关键是：  **to understand how to convert the policy iteration algorithm to be model-free**.

基础：

- policy iteration
- Monte Carlo mean estimation

---
##  Convert policy iteration  to be model-free


Policy iteration has **two steps** in each iteration:

- **Policy evaluation:** $ v_{\pi_k}=r_{\pi_k}+\gamma P_{\pi_k}v_{\pi_k}$
- **Policy improvement:** $\pi_{k+1}=argmax_\pi(r_\pi+\gamma P_\pi v_{\pi_k})$

The elementwise form of the **policy improvement step** is:

![](.\images\elementwisePI.png)

**The key is** $q_{\pi_k} (s, a)!$

---

##  Convert policy iteration  to be model-free

Two expressions of action value:

-  **Expression 1 requires the model:**

  $q_{\pi_k}(s_i,a)=r_\pi (s_i,a)+\gamma \underset {s_j}{\sum}p_\pi(s_j|s_i,a)v_\pi(s_j)$

  $= \underset {r}{\sum}p_\pi(r|s,a) r+\gamma \underset {s_j}{\sum}p_\pi(s_j|s_i,a)v_{\pi_k}(s_j)$

- **Expression 2 does not require the model:**

  $q_{\pi_k}(s_i,a)=\mathbb E[G_t|S_t=s,A_t=a]$

- Idea to achieve model-free RL: using **expression 2** to calculate   $q_{\pi_k}(s_i,a)$based on ***data (samples or experiences)***!

---
##  Convert policy iteration  to be model-free

![](.\images\14.png)

---

## The MC Basic algorithm

**Given an initial policy $\pi_0$, there are two steps at the $kth$ iteration.**

- **Step 1: policy evaluation.** This step is to obtain $q_{\pi_k}(s,a)$ for all $(s, a)$. Specificially, for each action-state pair $ (s, a)$, run an infinite number of (or sufficiently many) episodes. The average of their returns is used to approximate $q_{\pi_k}(s,a)$.
- **Step 2: policy improvement.** This step is to solve

   $\pi_{k+1}(s)=arg max_{\pi}\sum_a \pi (a|s)q_{\pi_k}(s,a) $  for all $s \in S$. 

The greedy optimal policy is： $\pi_{k+1}(a^*_k|s)=1$ where $a^*_k=argmax_a q_{\pi_k}(s,a)$

**Exactly the same as the policy iteration algorithm, except**

- Estimate $q_{\pi_k}(s,a)$directly, instead of solving $v_{\pi_k}(s,a)$.

