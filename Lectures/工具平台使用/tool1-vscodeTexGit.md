---
marp: true
footer: 'micl-MARL-常用工具vscode和操作命令'
paginate: true
style: |
  section a {
      font-size: 30px;
  }
---

# VSCode实现的环境搭建
## 1. vscode + TexLive + Git
## 2. vscode + Java - 估计不如idea方便
## 3. vscode实现的强化学习框架


----

## 1.vscode + TexLive + Git
参考资料：vscode + latex: https://zhuanlan.zhihu.com/p/166523064 
### 基于参考资料配置vscode+latex的编辑环境
### vscode 实现git命令，但是commit的时候一直卡着
1. git checkout Chapter7   更换github上的分支 
2. git add .   暂存更改
3. git commit -m"update 7-1" 提交更改，双引号中的是提交说明
4. git push
结论： git操作命令，尽量还是用git desktop，很方便。

---

## vscode-jupyter和web jupyterlab
参考资料：https://zhuanlan.zhihu.com/p/493282170

### 1. vscode-jupyter的好处

- vscode-jupyter自带了“变量表”
- vscode-jupyter有更强大的编程功能： 转到定义 - 转到引用  -  重命名符号 - **重构**
### 2. web jupyterlab的好处
- 主要vscode-jupyter的设置还有bug
---

### 2. vsocde + colab + github + Jupyter
参考资料：
1，https://medium.com/analytics-vidhya/colab-vs-code-github-jupyter-perfect-for-deep-learning-2b257ae94d01
2. https://bebi103a.github.io/lessons/02/git_with_colab.html
3. https://colab.research.google.com/github/JayThibs/jacques-blog/blob/master/_notebooks/2021-09-27-connect-to-colab-from-local-vscode.ipynb#scrollTo=WA2MmkhS0Prd 
4. https://blog.csdn.net/king52113141314/article/details/122955879 

- 使用 Vs Code 设置 Google Colab 远程机器
- 将您的本地存储库放到 Colab 
- 使用端口转发从 Colab 中运行 Jupyter Notebook

---
