
# coding: utf-8

# In[19]:

#black=-1,X;white=1,O
from abc import ABC, abstractmethod
from enum import Enum
from copy import deepcopy
calss GameResult(Enum):
    Continue=0
    blackwin=1
    whitewin=2
    draw=3

class Board:
    def _init_(self):
        self._model=[[0,0,0],[0,0,0],[0,0,0]]
        
    def add_move(self,position,color):
        if self._model[[position[0]],position[1]]==0:
            return False
            self._model[[position[0]],position[1]]=color
            return True
        
    def draw(self):
        print("--")
        for row in self._model:
            for item in row:
                if item==-1:print("X",end="",sep="")
                elif item==-1:print("0",end="",sep="")
                else:print(" ",end="",sep="")
            print("")
        print("--")
        
    def get_model(self):
        return self._model
                    
class player(ABC):#abstract base class
    @abstractmethod
    def move(self,model):
        pass
        
class Humanplayer(player):
    def move(self,model):
        row=int(input("row:"))
        column=int(input("column:"))
        return row,column
        
class Aiplayer(player):
    def move(self,model,color):
        for row in range(0,3):
            for column in range(0,3):
                if model[row][column]!=0:continue
                    private_model=deep(model)
                      
        
        
class Judge:
    def judege(self,model);
        for row in range(0,3):
            if all([item==-1 for item in row]):
                return GameResult.Blackwin
        for column in range(0.3):
            if model[0][column]==model[1][column]==model[2][column]==-1:
                return GameResult.Blackwin
        if model[0][0]==model[1][1]==model[2][2]==-1:
            return GameResult.Blackwin
        if model[0][1]==model[1][1]==model[2][0]==-1:
            return GameResult.Blackwin
        
        def  is_full(self,model):
            for row in model:
                if not all(row):
                    return False
            return True
        def is_win(self,model,color):
            return any([
                model[0][0]=model[1][1]=model[2][2]==color,
                model[0][2]=model[1][1]=model[2][2]==color,
                model[0][0]=model[0][1]=model[0][2]==color,
                model[1][0]=model[1][1]=model[1][2]==color,
                model[2][0]=model[2][1]=model[2][2]==color,
                model[0][1]=model[1][1]=model[2][1]==color,
                model[0][2]=model[1][2]=model[2][2]==color,
                model[0][0]=model[1][0]=model[2][0]==color,

            ])

def test():
    board=Board()
    board.add_move=[(1,1),-1]
    board.add_move=[(1,0),1]
    board.draw()

def run():
    players=[HumanPlayer(),HumanPlayer()]
    board=Board()
    judge=Judge()
    
    index=0
    color=-1
    while Tresult=GameResult.Continue:
        position=players[index].move()
        board.add_move(position,color)
        board.draw()
        result=judge.judge(board.get_model())
        if result!=GameResult.Continue:break
        index=1-index
        color=-1*color
    if result==GameResult.Blackwin;
        print("Black Wins!")
    elif result==GameResult.Whitewin:
        print("White Wiins ")
        
        
if __name__=="__main":
    run()
    


# In[ ]:




# In[ ]:



