## 课程介绍：

本课程是计算机理论课程，讲述计算机的基本功能和局限性，形式化描述计算机硬件和软件的数学特性；主要内容包括3个方面的知识：

- 计算模型：主要总结两个计算模型FA和PDA的基本功能和局限性
- 可计算理论：主要总结图灵机模型，并熟悉如何判定计算机的基本计算能力，以及什么样的问题是计算机不可计算的问题。
- 复杂性理论：这个是本学期的重点，如果确认要解决问题的复杂性，以及如何为复杂问题给出近似解

另外本课程在上述计算模型以及分析计算能力：能判定、识别的形式语言的基础之上，进行了理论和应用的扩展

- 理论扩展：通过读取论文，理解量子计算机是否计算能力 > 图灵机模型

- 应用扩展：通过读取论文，基于图计算，理解问题的形式化、问题求解，求解的可解释性。

  

  本课程课程目标如下：

  1. 计算机理论：希望学习如何思考、证明、论证、解决问题、表达和抽象。
  2. 理论与实践结合：学习到解决问题的技巧，涉及到的实践包括：新的编程语言设计、编译器、字符串搜索、模式匹配、计算机安全、人工智能等方面。 

  

### **纸上得来终觉浅，绝知此事要躬行**

1. 第2章 上下文无关的语言后可以复习下自己做的编译器。https://pandolia.net/tinyc/ch10_top_down_parse.html、
2. 图灵介绍和解读：http://www-history.mcs.st-andrews.ac.uk/Biographies/Turing.html
3. 计算模型仿真：http://www.jflap.org/
4. 。。。。。



## The key point in the course： Computational complexity

### Idea

Computational complexity is the mathematical study of computational efficiency. It is concerned with identifying efficient models of computation and understanding their power, their limitations, and their interrelationships.

Besides learning about basic techniques, I wish we can talk about  how computational complexity informs what is feasible and infeasible in other information processing areas (cryptographic protocols, combinatorial optimization, "big data" computations, machine learning, game theory and economics).



### Requirements

For your final project, you can do one of the following.

- **Do a small research project.** You can master how to describe the complexity, and prove the complexity class of  the problem related with your own research interest.

- **Study and reflect upon a work in computational complexity of your choice.** we will likely need to do some background reading. When presenting your work you are expected to place it in proper context in relation to the material in the course and give your own judgment about the advantages and disadvantages of the work. Two good places to look for possibilities are the [ECCC](http://eccc.hpi-web.de/) and [ArXiv](http://arxiv.org/list/cs.CC/recent) preprints. (A word of warning: The ArXiv papers are not refereed and the ones on ECCC are scrutinized minimally. If you find a serious error bonus points to you!)

- **Tell us about computational hardness (and how it is coped with) in your own research area.** we will try to define the problems and computational models rigorously, justify why your definitions are sensible .

  

  ### **课程分数**

  1. 计算理论书籍阅读和讲解： 60分

  2. 扩展论文阅读和讲解：40分
  
     
  
  ### Research project possibilities
  
  - #### Models
  
  - | 1    | Decision tree              |
    | ---- | -------------------------- |
    | 2    | Parallel computation       |
    | 3    | Sequential computation     |
    | 4    | Sublinear-time computation |
    | 5    | Quantum computation        |

  - #### Application

  - | 1    | Big Data         |
    | ---- | ---------------- |
    | 2    | Machine learning |

  - #### Monotone circuit lower bounds

  - In the monotone circuit lower bound for CLIQUE we showed that no small monotone circuit can simultaneously accept all positive instances and reject all negative instances. However there is a simple monotone circuit that accepts all negative instances and rejects all positive ones (what is it?) Can you come up with a possibly different monotone function so that no small monotone circuit can completely distinguish positive or negative in either direction?
  
  - #### Average-case complexity of approximate counting and sampling
  
  - Extend the theory of average-case complexity from search and decision to approximate counting and approximate sampling problems. I suggest you start with some examples of such problems that are easy and hard on average, state definitions, and try to relate these two types of problems (they are known to be worst-case equivalent in certain settings, e.g. approximately counting and sampling perfect matchings in graphs.)
  
  - #### 
  
  - 

## 课程内容安排：

| Lecture       | Topics                                                       | 讲义                       | 教材                                                        | 负责人 | 讨论题目 |
| ------------- | ------------------------------------------------------------ | -------------------------- | ----------------------------------------------------------- | ------ | -------- |
| 第1次课程     | Overview + 任务分拆 + 复杂性定义+extension （quantum，Interpretability） |                            |                                                             | 老师   |          |
| 第2次课程     | 自动机理论（DFA，NFA） + 形式语言1-正则语言（RL的运算性质:闭包，RE） | 第1章1，2 3，4             | 中文第2章<br />英文:§1.1-§1.3                               | 宋昆   | 问题1    |
|               | 自动机理论 RE=NFA=DFA +（NRL） pump lemma                    | 第1章5，6 （举简单的例子） | 中文第1章 + 补充<br />英文:§2.3-§2.4                        | 吉锋瑞 | 问题2    |
| 第3次课程     | 1. 上下文无关的语言:<br />   1) CFL，CFG形式化定义<br />   2) 派生过程:CFG->检查代码是否符合文法？（CFG是否能够派生出代码字符串？）<br />   3) 设计CFG (FA -> CFG,等等)<br />   4) 讨论下歧义性 | 第2章1，2 3，4             | 中文第2章                                                   | 刘孟寅 | 问题3    |
|               | 2. 上下文无关的语言CFG<br />     1) 标准化：乔姆斯基范式<br />     2) CFL的运算性质 <br />3. 下推自动机的形式化定义<br />     1) 计算过程的形式化<br />     2) 下推自动机举例 |                            |                                                             | 杨聚旺 | 问题4    |
|               | 4. CFG =下推自动机<br />5. NCFL与证明 + 总结                 | 第2章5，6习题课            | 中文第2章                                                   | 庄雨   | 问题5    |
| 第4次课程     | 1. 图灵机的形式化描述，计算过程的形式化 <br />2.  图灵机的变形（Stay-Option, Semi-Infinite,Off-Line；。多带，非确定性），算法鲁棒性分析（等价） | 第3章1,2,3                 | 中文第3章                                                   | 朱康希 | 问题5    |
|               | 3. 图灵机的变形-枚举，通用图灵机<br />4. 图灵丘奇定理<br />5. 图灵机论文的理解 | 第3章                      | 中文第3章                                                   | 刘雪松 | 问题6    |
| 第5次课程     | **1. 可计算问题分析<br />1）可判定的定义：decidable languages are languages that can be decided by TM **(that means, the corresponding TM will accept or reject correctly, never loops)<br />2）判定其他计算模型的计算能力： investigating some decidable languages that are related to DFA, NFA, and CFG：Acceptance, Emptiness, or Equality，we show how TM can simulate CFG | 第4章1                     | 中文第4章                                                   | 李长泰 |          |
|               | 2. 不可解问题所涉及的基础：不可判定，不可识别<br />1) 可数集合与不可数集合<br />2）对角线法 | 第4章2                     | 中文第4章                                                   | 任世奇 |          |
|               | 3. 不可解问题分析<br />1）不是识别的问题举例<br />2）可识别，不可判定问题举例<br />3）Examples of undecidable Language-Turning recognizable but not decidable:Halt problem，Non-Turning recognizable |                            |                                                             | 李潇睿 |          |
| 第6次课程     | 1. 归约<br />1）举例：可以用来证明问题是可判定的；<br />2）举例：可以用来证明问题是不可判定的；(State-entry problem,Halting Problem,空带问题 <br />3）其他不可判断给你问题的举例，主要看看TM是否能模拟判定某些算法的能力 | 第5章1，2                  | 中文第5章                                                   | 肖楠   |          |
|               | 2.Undecidable Problems for Recursively Enumerable Languages<br />3. Rice定理：中文书 (习题**5.28**)  + 尽量分析下第一次课给大家说的静态软件分析中的感兴趣问题是无解的，或者分析其他可能用到Rice定义的问题你 | 第5章3，4                  | 中文第5章                                                   | 国贤玉 |          |
|               | 4. The Chomsky Hierarchy<br />1）Linear-Bounded Automata - Context sensitive language<br />2）分析LBA接受性问题是否可判定；<br />3）总结下我们已经看到过的形式语言<br />5. 归约技巧1：历史格局+PC问题， 举例-CFG相关的判定问题 | 第5章3，4                  | 中文第5章                                                   | 胡旭   |          |
| 第7次课程     | 时间复杂度讨论：<br />1. 复杂性的度量（中文书：8.1.1）<br />2. 模型间的复杂性关系 （中文书：8.1.2，8.1.3）<br />1）Church-Turing thesis，Cobham-Edmonds thesis<br />2）单带图灵机，多带图灵机，不确定图灵机的复杂度分析<br />3. P问题定义和分析（中文书:8.2）：<br />1）理解P是问题分类的一种，不是算法；<br />2）时间TIME(t(n)),多项式时间与P定义<img src="C:\Users\duan\AppData\Roaming\Typora\typora-user-images\image-20211103142921088.png" alt="image-20211103142921088" style="zoom: 80%;" /> | 第7章1                     | 电子中文书第8章8.1，8.2<br />电子英文书chapter 7： 7.1，7.2 | 杨晓芬 |          |
|               | 4. P问题定义和举例  （中文书8.2.2，定理8.12，813）<br /><img src="C:\Users\duan\AppData\Roaming\Typora\typora-user-images\image-20211103165053184.png" alt="image-20211103165053184" style="zoom:67%;" /><br />5. NP问题定义：Nondeterministic Complexity，确定性TM 多项式时间可验证。。。(中文书，定义8.16,定理7.17-推论8.19)<br />6.典型的NP类问题 (HAMPATH and COMPOSITES∈ NP) |                            |                                                             | 刘海壮 |          |
|               | 7. 典型的NP类问题：CLIQUE，SUBSET-SUM，The Satisfiability Problem SAT等；<br />8. P和NP（书上简单说明了，由于二者并未解决，所以可以参看其他资料，简单分析下）；<br />9. coNP总结下 | **第7章2**                 | 电子中文书第8章8.3，8.4.1                                   | 师亚勇 |          |
| 第8次课程     | 时间复杂度再讨论：<br />1. 多项式时间归约（定理8.26）归约举例:SAT and 3SAT，SCNF->CLIQUE, CLIQUE->IS，IS->VC, 3SAT ->CLIQUE<br />2. NPC定义，库克-列文定理（定理8.22，8.30，中文定理7.22，7.30）与证明； | 第7章3                     | 电子中文书第7章7.4                                          | 李荣洋 |          |
|               | 3. 总结下常见的NPC问题，分析推论8.32(中文 定理7.32)，<br />4. 常见的NPC问题，定义8.34(中文 定理7.34)，8.35(中文定理7.35)， |                            |                                                             | 杜泉成 |          |
|               | 5. 常见的NPC问题，定义8.36(中文 定理7.36)，8.37(中文 定理7.37)，TRICOVER is NP-complete，3COL is NP-complete<br />6. NP hard定义 | 第7章3                     | 电子中文书第7章7.5                                          | 国峰   |          |
| 第**9次课程** | space complexity：<br />1. 空间复杂度的定义：Definition 1,2 and examples 3, 4; <br />2. 萨维奇定理 (中文8.1节) Savitch's theorem; <br />3. 空间复杂性定义PSPACE类：（中文8.2 PSPACE class）特别是中文书的图8.1 <br />4. PSPACE完全性，PSAPCE难的定义 |                            | 中文第8章，chapter 8 in English book                        | 万菲   |          |
|               | 5. PSPACE completeness(中文书8.3)：definition <br />6. PSAPCE 完全问题举例分析：8.3.1 TQBF is PSPACE complete，Winning strategies for games.  example 8.10 and theorem 8.11; ：Generalized Geography-theorem 8.14 |                            |                                                             | 赵秀锋 |          |
|               | 7. L and NL，coNL（中文书8.4）<br />1）NL complete<br />2）NL=coNL<br />8. 总结下空间复杂度和用途 |                            | 中文第9章9.3后半部分+9.4，chapter 8 in English book 8.3     | 张世学 |          |
| 第10次课程    | 难解性分析<br />1. 层次定理(中文电子书9.1)                   |                            | 中文电子书9章                                               | 陈龙   |          |
|               | 2. 相对化（中文电子书9.2）:Provably intractable problems, oracles |                            |                                                             | 屈志远 |          |
|               | 3. 电路复杂性(中文电子书9.3)                                 |                            | 中文电子书9章                                               | 马启程 |          |
| 第11次课程    | 高级专题：<br />1. NP近似求解：10.1，<br />2. 概率算法(Probabilistic computation, BPP):10.2.1,10.2.2 |                            | 中文电子书10章                                              | 杨文金 |          |
|               | 3. 概率算法:10.2.3<br />4. 高级专题-交错式：10.3.1           |                            | 中文电子书10章                                              | 韩铮   |          |
| 第12次课程    | 高级专题再讨论下：<br />1. 高级专题-交错式：10.3.2<br />2. 高级专题-并行计算：10.5 |                            | 中文电子书10章                                              | 熊琛   |          |
|               | 3. 高级专题-交互式证明系统，coNP ⊆ IP ，中文10.4             |                            | 中文电子书10章                                              | 王稼祥 |          |
| 第13次课程    | 论文总结 (6-7个报告)                                         |                            | 补充资料                                                    |        |          |
| 第14次课程    | 论文总结(6-7个报告)                                          |                            | 补充资料                                                    |        |          |
| 第15次课程    | 论文总结(6个报告)                                            |                            | 补充资料                                                    |        |          |
| 第16次课程    | 论文总结(6个报告)                                            |                            | 补充资料                                                    |        |          |

