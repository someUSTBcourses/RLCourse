## **一、简介**

Jupyter Notebook是一个开源的Web应用程序，允许用户创建和共享包含代码、方程式、可视化和文本的文档。它的用途包括：数据清理和转换、数值模拟、统计建模、数据可视化、机器学习等等。它具有以下优势：

- 可选择语言：支持超过40种编程语言，包括Python、R、Julia、Scala等。
- 分享笔记本：可以使用电子邮件、Dropbox、GitHub和Jupyter Notebook Viewer与他人共享。
- 交互式输出：代码可以生成丰富的交互式输出，包括HTML、图像、视频、LaTeX等等。
- <font color=red>大数据整合</font>：通过Python、R、Scala编程语言使用Apache Spark等大数据框架工具。支持使用pandas、scikit-learn、ggplot2、TensorFlow来探索同一份数据。

## **二、安装与运行**

虽然Jupyter可以运行多种编程语言，但Python是安装Jupyter Noterbook的必备条件（Python2.7，或Python3.3以上）。有两种安装方式：使用Anaconda安装或使用pip命令安装。关于安装的全部信息可以在官网读到：[安装Jupyter](https://jupyter.org/install.html)。

**2.1使用Anaconda安装**

对于小白，强烈建议使用[Anaconda发行版](https://link.zhihu.com/?target=https%3A//www.anaconda.com/download/)安装Python和Jupyter，其中包括Python、Jupyter Notebook和其他常用的科学计算和数据科学软件包。

首先，下载[Anaconda](https://link.zhihu.com/?target=https%3A//www.anaconda.com/download/)。建议下载Anaconda的最新Python 3版本。其次，请按照下载页面上的说明安装下载的Anaconda版本。最后，安装成功！

**2.2使用pip命令安装**

对于有经验的Python用户，可以使用Python的包管理器pip而不是Anaconda 来安装Jupyter。

如果已经安装了Python3：

```text
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```

如果已经安装了Python2：

```text
python -m pip install --upgrade pip
python -m pip install jupyter
```

恭喜，你已经成功安装好了！

**2.3运行Jupyter Notebook**

成功安装Jupyter Notebook后，在Terminal (Mac / Linux)或Command Prompt(Windows)中运行以下命令就可打开Jupyter Notebook。

```text
jupyter notebook 
```

下面演示一下在Windows系统中打开Jupyter Notebook：

![img](https://pic2.zhimg.com/80/v2-621dd19e08f9b2adfb6d942429bc54ed_720w.jpg)打开Command Prompt

![img](https://pic2.zhimg.com/80/v2-87ace2def3f49c0712190a97885c1681_720w.jpg)输入jupyter notebook，回车

![img](https://pic3.zhimg.com/80/v2-fdca19cb6b2e631a900108d2d18195aa_720w.jpg)显示jupyter notebook页面

参阅[运行Notebook](https://jupyter.readthedocs.io/en/latest/running.html)了解更多详情。

## **三、主面板(Notebook Dashboard)**

打开Notebook，可以看到主面板。在菜单栏中有Files、Running、Clusters、Conda四个选项。用到最多的是Files，我们可以在这里完成notebook的新建、重命名、复制等操作。具体功能如下：

![img](https://pic3.zhimg.com/80/v2-6be3545ddd0dcfb9b92918cfa3f4b9aa_720w.jpg)Notebook主面板：File

在Running中，可以看到正在运行的notebook，我们可以选择结束正在运行的程序。

![img](https://pic4.zhimg.com/80/v2-91ed21423b1a7f8d34c3f03eb40ed9c3_720w.jpg)Notebook主面板：Running

至于Clusters、Conda一般用不到，暂不做介绍，后续补充。

## **四、编辑界面(Notebook Editor)**

一个notebook的编辑界面主要由四部分组成：名称、菜单栏、工具条以及单元(Cell)，如下图所示：

![img](https://pic1.zhimg.com/80/v2-5bca7035e7fd4cb8c97c083766087ac4_720w.jpg)notebook界面

**4.1 名称**

在这里，我们可以修改notebook的名字，直接点击当前名称，弹出对话框进行修改：

![img](https://pic4.zhimg.com/80/v2-3e05545e9b642466016f7223e3e193f3_720w.jpg)notebook名称修改

**4.2菜单栏**

菜单栏中有File、Edit、View、Insert、Cell、Kernel、Help等功能，下面逐一介绍。

**4.2.1 File**

File中的按钮选项如下图所示：

![img](https://pic4.zhimg.com/80/v2-51cd9a3188f373fcfb18101c399fe7a3_720w.jpg)File中的按钮选项

具体功能如下表：

![img](https://pic3.zhimg.com/80/v2-76227cce3591b2900de9be91fd0f2952_720w.jpg)

**4.2.2 Edit**

Edit中的按钮选项

![img](https://pic3.zhimg.com/80/v2-b92adc9ef1910c2691010f5d3e16c10a_720w.jpg)

**4.2.3 View**

View中的按钮选项如下图所示：

![img](https://pic4.zhimg.com/80/v2-3543f27895dabcebb4b8643ef86a9363_720w.jpg)

![img](https://pic2.zhimg.com/80/v2-c85e3b2c911f701ddd6ebec6b47c75b1_720w.jpg)

View中的功能可以让用户更好的展示自己的notebook，但对编写代码、实现功能没有影响。

**4.2.4 Insert**

![img](https://pic2.zhimg.com/80/v2-faa8ddb9521381d5a539a68daa25dcdd_720w.jpg)

功能：在当前单元上方/下方插入新的单元。

**4.2.5 Cell**

![img](https://pic3.zhimg.com/80/v2-b969a960c54bddb734ed4145bd39e2fe_720w.jpg)

![img](https://pic1.zhimg.com/80/v2-edb4fbe0c31520ce5f71a6df487aacc8_720w.jpg)

**4.2.6 Kernel**

![img](https://pic2.zhimg.com/80/v2-f69aa73d9f8f054cc84450b3a8a6e3e5_720w.jpg)

![img](https://pic3.zhimg.com/80/v2-a5c5fa22bc0e255a091560ba555bced6_720w.jpg)

**4.2.7 Help**

![img](https://pic3.zhimg.com/80/v2-51c51f0119843ce4e9649981fa09780a_720w.jpg)

![img](https://pic4.zhimg.com/80/v2-41878b9135b65ec3491aa788daceed03_720w.jpg)

**4.3 工具条**

工具条中的功能基本上在菜单中都可以实现，这里是为了能更快捷的操作，将一些常用按钮放了出来。下图是对各按钮的解释。

**4.4 单元(Cell)**

在单元中我们可以编辑文字、编写代码、绘制图片等等。对于单元的详细内容放在第五节中介绍。

## **五、单元(Cell)**

**5.1两种模式与快捷键**

对于Notebook中的单元，有两种模式：命令模式(Command Mode)与编辑模式(Edit Mode)，在不同模式下我们可以进行不同的操作。

![img](https://pic2.zhimg.com/80/v2-41a4d9258d7f385c55114751f7ac45f9_720w.jpg)

如上图，在编辑模式(Edit Mode)下，右上角出现一只铅笔的图标，单元左侧边框线呈现出绿色，点Esc键或运行单元格(ctrl-enter)切换回命令模式。

![img](https://pic3.zhimg.com/80/v2-d1670ade217edb1f5bfd53240a3d0db2_720w.jpg)

在命令模式(Command Mode)下，铅笔图标消失，单元左侧边框线呈现蓝色，按Enter键或者双击cell变为编辑状态。

**5.1.1命令模式下的快捷键**

![img](https://pic4.zhimg.com/80/v2-a9968b4189aff6fc84d2141218286ca3_720w.jpg)

**5.1.2编辑模式下的快捷键**

![img](https://pic4.zhimg.com/80/v2-6d9bc9bdc8c75dc4d06ae1be0cbf361b_720w.jpg)

注意不要死记硬背，在使用过程中需要什么就去查，多用用就能记住了。

**5.2 Cell的四种功能**

Cell有四种功能：Code、Markdown、Raw NBConvert、Heading，这四种功能可以互相切换。Code用于写代码，Markdown用于文本编辑，Raw NBConvert中的文字或代码等都不会被运行，Heading是用于设置标题的，这个功能已经包含在Markdown中了。四种功能的切换可以使用快捷键或者工具条。

Code用于写代码，三类提示符及含义如下：

![img](https://pic3.zhimg.com/80/v2-d4db4f6f1723191a00af316347cafcea_720w.jpg)

Markdown用于编辑文本，给出常用的Markdown用法：

![img](https://pic3.zhimg.com/80/v2-c9a44ddc812970ed39b9e92bcf2b409e_720w.jpg)

其他非常用的用法需要时可以再查阅。

## **六、魔法函数**

使用魔法函数可以简单的实现一些单纯python要很麻烦才能实现的功能。



%：行魔法函数，只对本行代码生效。

%%：Cell魔法函数，在整个Cell中生效，必须放于Cell首行。

%lsmagic：列出所有的魔法函数

%magic查看各个魔法函数的说明

?后面加上魔法函数名称，可以查看该函数的说明



一些常用魔法函数的示例：

![img](https://pic3.zhimg.com/80/v2-e9877938d1aa3614c6d6e0e02cd3f952_720w.jpg)

注意这些命令是在Python kernel中适用的，其他 kernel 不一定适用。

## **七、其他**

（1）按tab键查看提示信息或者补全命令

![img](https://pic4.zhimg.com/80/v2-4c95438d5609a684f4b5092b6c767073_720w.jpg)

（2）在一个库、方法或变量前加上 ?，就可以获得它的一个快速语法说明

![img](https://pic3.zhimg.com/80/v2-418f8735c7ce401088dbc90a994e990e_720w.jpg)

（3）使用分号可以阻止该行函数的结果输出

![img](https://pic3.zhimg.com/80/v2-a44bf7852637d416d923030dbca8f696_720w.jpg)