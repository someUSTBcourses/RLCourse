---
marp: true
footer: '强化学习实践'
paginate: true
style: |
  section a {
      font-size: 30px;
  }
---

# 实践用平台
## 1. docker / anaconda /colab 
## 2. gym[ansium]库和常见的扩展
## 3. 强化学习平台
## 4. 多智能体强化学习平台
----
## 1. docker / anaconda / colab
### 主要目标：避免重复的环境配置

### 程序：.ipython, .py  

### colab的使用 
### pytorch的使用 

----

### (3) 安装vcxsrv 这个步骤很重要，古月居建议的是vnc viewer需要注册不好，但是xlaunch后需要配置。但是感觉存不了呢？
问题1：存在can not display的问题
解答：需要设置DISPLAY环境变量![](images/DisplaySet.png)

----
### (4) 需要安装软件
1. vim
   ```
   apt-get update
   apt-get install vim
   export DISPLAY="WSL-IP:0.0"
   ```
2. ipconfig
   ```
   cat /etc/resolv.conf
   apt install net-tools
   ```
   参考资料：https://stackoverflow.com/questions/61860208/running-graphical-linux-desktop-applications-from-wsl-2-error-e233-cannot-op
3. gedit
   ```
   sudo apt install gedit 
   ```
4. 

----

## 2.下载ros的docker镜像和docker-ros环境

### 2.1 直接下载镜像
拉取镜像：  
```
docker pull osrf/ros:melodic-desktop-full
```
拉取镜像：  
```
拉取并运行： docker run -it  -p 6000:22 -p 6001:8080 --name=base-ros-melodic osrf/ros:melodic-desktop-full  /bin/bash
```
---
### 2.2 自己制作dockerfile
参考：https://blog.csdn.net/weixin_43134049/article/details/123182003

1. Dockerfile 以官方镜像配置自己的ros镜像，新建一个 Dockerfile 文件后写入下面的
   ```
   docker build -t rocker .
   ```
2. 基于Dockerfile 生成镜像
      ```
   docker build -t rocker .
   ```
3. 生成的镜像文件创建docker容器，运行如下命令， --name后面就是生成的镜像的名字，也可换成 镜像id ，成功运行后就可以进入容器了
  ```
  docker run -it --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix  --env="DISPLAY=$DISPLAY"  --name=rocker osrf/ros:melodic-desktop-full  /bin/bash
  ```
----
4. 进入容器后运行指令
```
RUN apt-get update && \
apt-get install -y \
build-essential \
libgl1-mesa-dev \
libglew-dev \
libsdl2-dev \
libsdl2-image-dev \
libglm-dev \
libfreetype6-dev \
libglfw3-dev \
libglfw3 \
libglu1-mesa-dev \
freeglut3-dev \
vim
```
----

export ROS_HOSTNAME=localhost
export ROS_MASTER_URI=http://localhost:11311

----
### 2.3  docker-ros上小海龟的测试
多开几个终端，每个终端用
docker attach  无法建立一个新的终端!
```
docker exec -it <container_name_or_id> bash
1、在Terminal中运行以下命令：
roscore
2、新开一个terminal，运行以下命令，弹出一个小乌龟窗口：
rosrun turtlesim turtlesim_node
3、新开一个terminal，运行以下命令，打开乌龟控制窗口，可使用方向键控制乌龟运动：
rosrun turtlesim turtle_teleop_key
4、选中控制窗口，按方向键，可看到小乌龟窗口中乌龟在运动。
5、新开一个terminal，运行以下命令，可以看到ROS的图形化界面，展示结点的关系：
rosrun rqt_graph rqt_graph
6、terminal 4
rostopic pub -r 5 /turtle1/cmd_vel geometry_msg/Twist
# 测试瞎走圆圈，输入命令后Tab，修改“Linear”和"angular"中数据，便可以让小海龟做圆周运动了
7、terminal 5：测试瞎自己建立的控制海龟转圆圈的package
https://www.jianshu.com/p/1efe8fe41800
```
----
记录下问题
问题1： roscore，rosrun找不到命令
解决：source /opt/ros/melodic/setup.bash  写到.bashrc
问题2：
----
### (3) gym提供了什么，怎么使用搭建基于path planing的试错/强化学习过程 

 **AI Habitat能够在一个高度逼真和高效的3D模拟器中训练这种具身的AI代理（虚拟机器人和以自我为中心的助手），然后再将学到的技能转移到现实中**

---

# 附录 

## 编辑文档的工具 - vscode

### 1. vscode 编辑md文件

不需要增加任何控件，但是使用了marp插件，在pdf文件和ppt可以轻松切换，特别喜欢！

---

### 2. vsocde + latex编辑

安装很方便，熟悉下texlive的包管理软件。参考安装的链接：

包管理的启动命令：安装主目录下运行
```
tl-tray-menu.exe
```
出错的时候，修改了setting.json, 修改发了"latex-workshop.latex.recipes": 节的内容

---
