---
marp: true
footer: 'micl-强化学习环境搭建'
paginate: true
style: |
  section a {
      font-size: 30px;
  }
---

# RL开发环境搭建
## 1. gym库 - 开发流程 
## 2. RLlib平台 - 搭建**实现未知环境navigation**和baseline算法
## 3. MARLlib平台 - 搭建多智能体强化学习平台
## 4. 竞赛平台 - 试试打点竞赛吧！
## 5. 编辑工具熟悉下

----

## 1.gym库

### (1) 总结gym相关的其他强化学习库
### (2) 试错学习的程序逻辑
### (3) gym提供了什么，怎么使用搭建基于path planing的试错/强化学习过程 

 **AI Habitat能够在一个高度逼真和高效的3D模拟器中训练这种具身的AI代理（虚拟机器人和以自我为中心的助手），然后再将学到的技能转移到现实中**

---

# 附录 

## 编辑文档的工具 - vscode

### 1. vscode 编辑md文件

不需要增加任何控件，但是使用了marp插件，在pdf文件和ppt可以轻松切换，特别喜欢！

---

### 2. vsocde + latex编辑

安装很方便，熟悉下texlive的包管理软件，感觉不错。

包管理的启动命令：安装主目录下运行
```
tl-tray-menu.exe
```
出错的时候，修改了setting.json, 修改发了"latex-workshop.latex.recipes": 节的内容

---
