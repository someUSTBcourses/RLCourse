---
marp: true
# theme: uncover
theme: default
# _class: invert
footer: 'marl-定义，环境与平台，难点问题和解决算法'
paginate: true
style: |
  section a {
      font-size: 100px;
      text-align: center;
  }

---


# **MARL-形式化定义和常用算法**

## 本节目标
* **定义**：MARL,distributrial RL, distributed RL
* **基础概念**:  形式化方式
* **基础工具**： 求解的方法核心
* **环境和平台**：
* **算法实现和比较**：
---
## 参考文献
1. 综述类相关的文献
   1. 知乎的笔记:  

---

   1. 2303：《ScalableMulti-Agent Reinforcement Learning for Networked Systems with Average Reward》。这是加州理工学院发表在计算机顶级会议Nips2020上的一篇文章
---
## 目 录
### 1. 概念定义及其关系：$v^*_t(s)$,$q^*_t(s,a)$,$\leftrightarrow$ $\pi^*(s)$
### 2. BOE基础 
### 3. BOE求解 
### 4. 分析最优策略
---

## 看个例子：网格路径规划策略
<!-- footer: '' -->

![bg left:30% width:300 height:300](images/ex1.png)
**Bellman equation:** 
$v_{\pi}(s1)=-1+\gamma v_{\pi}(s2)$
$v_{\pi}(s2)=1+\gamma v_{\pi}(s4)$
$v_{\pi}(s3)=1+\gamma v_{\pi}(s4)$
$v_{\pi}(s4)=1+\gamma v_{\pi}(s4)$
计算: $v_{\pi}(s1)$, $v_{\pi}(s2)$,$v_{\pi}(s3)$,$v_{\pi}(s4)$
Let $\gamma=0.9$, 做4元1次方程求解
$v_{\pi}(s1)=8$, $v_{\pi}(s2)=10$,$v_{\pi}(s3)=10$,$v_{\pi}(s4)=10$

---
## 看个例子：网格路径规划策略
<!-- footer: '' -->

![bg left:30% width:300 height:300](images/ex1.png)
**动作值$q_\pi(s_i,a_{ij})$:跟特定的$\pi$和状态$s_i$有关** ,选择不同的动作$a_{ij}$有不同的值/累计奖励值
$q_{\pi}(s_1,a_{11})=-1+\gamma v_{\pi}(s_1)= 6.2 \quad (a_{11}=向上) ,$
$q_{\pi}(s_1,a_{12})=-1+\gamma v_{\pi}(s_2)= 8 \quad (a_{12}=向右) ,$
$q_{\pi}(s_1,a_{13})= 0+\gamma v_{\pi}(s_3)= 9 \quad (a_{13}=向下) ,$
$q_{\pi}(s_1,a_{14})= -1+\gamma v_{\pi}(s_1)= 6.2\quad (a_{14}=向左) ,$
$q_{\pi}(s_1,a_{15})= 0+\gamma v_{\pi}(s_1)=7.2 \quad (a_{15}=不动) ,$
计算: $v_{\pi}(s1)$
Let $\gamma=0.9$,  $v_{\pi}(s1) = \mathbb E\{\sum_{a1 \in \mathcal A}q_\pi(s_1,a_{1})\}=6.2+8+9+6.2+7.2=$

---
## 看个例子：网格路径规划策略
<!-- footer: '' -->

![bg left:30% width:350 height:700](images/RLcourse-Lect3-1.png)
**问题: 策略可以调优吗，如何做？ ** 

---
## Usage

Marp preview for Markdown document will be enabled when `marp: true` is written in front-matter.

```markdown

# Your slide deck

Start writing!
```

---
