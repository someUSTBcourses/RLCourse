import numpy as np
import random
#跟v1版本的区别主要是两点，v1是针对deteministic的策略的，v2是针对stochastic的策略的，
#具体来说的话就是，v2版本支持在同一个state概率选择若干个动作
#它的策略矩阵，现在是 shape==(25,5)的第一维表示state，第二维表示action，返回一个概率
#在打印策略的时候，将把每个state最大概率的动作打印出来
#
#第二点区别是，在v2版本里面，引入了trajectory的概念
#通过getTrajectoryScore方法可以直接按照提供的policy，进行采样若干步

#v3是最终版本，它引入了是否终止的概念，在trajectory里面每一步都有一个是否终止的标志。
#此外v3的最后一步，不再是以target state为起点，而是以target state为终点。也就是trajectory比v2版本会少了一步

class GridWorld_v3(object): 
    # n行，m列，随机若干个forbiddenArea，随机若干个target
    # A1: move upwards
    # A2: move rightwards;
    # A3: move downwards;
    # A4: move leftwards;
    # A5: stay unchanged;

    stateMap = None  #大小为rows*columns的list，每个位置存的是state的编号
    scoreMap = None  #大小为rows*columns的list，每个位置存的是奖励值 0 1 -1
    score = 0             #targetArea的得分
    forbiddenAreaScore=0  #forbiddenArea的得分

    
    def __init__(self,rows=4, columns=5, forbiddenAreaNums=3, targetNums=1, seed = -1, score = 1, forbiddenAreaScore = -1, desc=None):
        
        self.score = score
        self.forbiddenAreaScore = forbiddenAreaScore
        if(desc != None):
            #if the gridWorld is fixed
            self.rows = len(desc)
            self.columns = len(desc[0])
            l = []
            for i in range(self.rows):
                tmp = []
                for j in range(self.columns):
                    tmp.append(forbiddenAreaScore if desc[i][j]=='#' else score if desc[i][j]=='T' else 0)
                l.append(tmp)
            self.scoreMap = np.array(l)
            self.stateMap = [[i*self.columns+j for j in range(self.columns)] for i in range(self.rows)]
            return
            
        #if the gridWorld is random
        self.rows = rows
        self.columns = columns
        self.forbiddenAreaNums = forbiddenAreaNums
        self.targetNums = targetNums
        self.seed = seed

        random.seed(self.seed)
        l = [i for i in range(self.rows * self.columns)]
        random.shuffle(l)  #用shuffle来重排列
        self.g = [0 for i in range(self.rows * self.columns)]
        for i in range(forbiddenAreaNums):
            self.g[l[i]] = forbiddenAreaScore;        # 设置禁止进入的区域，惩罚为1
        for i in range(targetNums):
            self.g[l[forbiddenAreaNums+i]] = score # 奖励值为1的targetArea
            
        self.scoreMap = np.array(self.g).reshape(rows,columns)
        self.stateMap = [[i*self.columns+j for j in range(self.columns)] for i in range(self.rows)]

    def show(self):
        for i in range(self.rows):
            s = ""
            for j in range(self.columns):
                tmp = {0:"⬜️",self.forbiddenAreaScore:"🚫",self.score:"✅"}
                s = s + tmp[self.scoreMap[i][j]]
            print(s)
        
    def getScore(self, nowState, action):
        nowx = nowState // self.columns
        nowy = nowState % self.columns
        
        if(nowx<0 or nowy<0 or nowx>=self.rows or nowy>=self.columns):
            print(f"coordinate error: ({nowx},{nowy})")
        if(action<0 or action>=5 ):
            print(f"action error: ({action})")
            
        # 上右下左 不动
        actionList = [(-1,0),(0,1),(1,0),(0,-1),(0,0)]
        tmpx = nowx + actionList[action][0]
        tmpy = nowy + actionList[action][1]
        # print(tmpx,tmpy)
        if(tmpx<0 or tmpy<0 or tmpx>=self.rows or tmpy>=self.columns):
            return -1,nowState
        return self.scoreMap[tmpx][tmpy],self.stateMap[tmpx][tmpy]

    def getTrajectoryScore(self, nowState, action, policy):
        #policy是一个 (rows*columns) * actions的二维列表，其中每一行的总和为1，代表每个state选择五个action的概率总和为1
        #Attention: 返回值是一个大小为steps+1的列表，因为第一步也计算在里面了
        #其中的元素是(nowState, nowAction, score, nextState, nextAction, terminal)元组
        
        res = []
        nextState = nowState
        nextAction = action
        
        for i in range(1001):
            nowState = nextState
            nowAction = nextAction

            score, nextState = self.getScore(nowState, nowAction)
            nextAction = np.random.choice(range(5), size=1, replace=False, p=policy[nextState])[0]

            terminal = 0
            nxtx, nxty = nextState // self.columns, nextState % self.columns
            if self.scoreMap[nxtx][nxty] == self.score:
                terminal = 1
            
            res.append((nowState, nowAction, score, nextState, nextAction, terminal))

            if terminal:
                return res
        return res

    def showPolicy(self, policy):
        #用emoji表情，可视化策略，在平常的可通过区域就用普通箭头⬆️➡️⬇️⬅️
        #但若是forbiddenArea，那就十万火急急急,于是变成了双箭头⏫︎⏩️⏬⏪
        rows = self.rows
        columns = self.columns
        s = ""
        # print(policy)
        for i in range(self.rows * self.columns):
            nowx = i // columns
            nowy = i % columns
            if(self.scoreMap[nowx][nowy]==self.score):
                s = s + "✅"
            if(self.scoreMap[nowx][nowy]==0):
                tmp = {0:"⬆️",1:"➡️",2:"⬇️",3:"⬅️",4:"🔄"}
                s = s + tmp[np.argmax(policy[i])]
            if(self.scoreMap[nowx][nowy]==self.forbiddenAreaScore):
                tmp = {0:"⏫️",1:"⏩️",2:"⏬",3:"⏪",4:"🔄"}
                s = s + tmp[np.argmax(policy[i])]
            if(nowy == columns-1):
                print(s)
                s = ""