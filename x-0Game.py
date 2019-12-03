import sys
from numpy import *
class tic_tae_toe:
    mat=array([['_','_','_'],['_','_','_'],['_','_','_']])
    def __init__(self,name,name1):
        self.name=name
        self.name1=name1
    def disp(self):
        for i in range(0,3,1):
            for j in range(0,3,1):
               print(self.mat[i][j],end=" ")
            print()
        print()
        print()
    def draw(self):
        print("game ended as draw")
        sys.exit()
    def result(self,i):
        if i == '#':
            print(self.name + " is the winner")
            sys.exit()
        else:
            print(self.name1 + "%s is the winner")
            sys.exit()
    def check(self):
        if (self.mat[0][0]=='#' and self.mat[0][1]=='#' and self.mat[0][2]=='#') or (self.mat[1][0]=='#' and self.mat[1][1]=='#' and self.mat[1][2]=='#') or (self.mat[2][0]=='#' and self.mat[2][1]=='#' and self.mat[2][2]=='#') or (self.mat[0][0]=='#' and self.mat[1][0]=='#' and self.mat[2][0]=='#') or (self.mat[0][1]=='#' and self.mat[1][1]=='#' and self.mat[2][1]=='#') or(self.mat[0][2]=='#' and self.mat[1][2]=='#' and self.mat[2][2]=='#') or (self.mat[0][2]=='#' and self.mat[1][1]=='#' and self.mat[2][0]=='#') or (self.mat[0][0]=='#' and self.mat[1][1]=='#' and self.mat[2][2]=='#') :
            self.disp()
            self.result('#') 
        elif(self.mat[0][0]=='0' and self.mat[0][1]=='0' and self.mat[0][2]=='0') or (self.mat[1][0]=='0' and self.mat[1][1]=='0' and self.mat[1][2]=='0') or (self.mat[2][0]=='0' and self.mat[2][1]=='0' and self.mat[2][2]=='0') or (self.mat[0][0]=='0' and self.mat[1][0]=='0' and self.mat[2][0]=='0') or (self.mat[0][1]=='0' and self.mat[1][1]=='0' and self.mat[2][1]=='0') or(self.mat[0][2]=='0' and self.mat[1][2]=='0' and self.mat[2][2]=='0') or (self.mat[0][2]=='0' and self.mat[1][1]=='0' and self.mat[2][0]=='0') or (self.mat[0][0]=='0' and self.mat[1][1]=='0' and self.mat[2][2]=='0'):  
            self.disp()
            self.result('0')
        elif self.mat[0][0]!='_' and self.mat[0][1]!='_' and self.mat[0][2]!='_' and self.mat[1][0]!='_' and self.mat[1][1]!='_' and self.mat[1][2]!='_' and self.mat[2][0]!='_' and self.mat[2][1]!='_' and self.mat[2][2]!='_' :
            self.disp()
            self.draw()
    def game(self):
        self.disp()
        a=int(input("choose the index: " + self.name))
        if a<4:
            self.mat[0][a-1]='#'
        elif(a<7):
            self.mat[1][a-4]='#'
        else:
            self.mat[2][a-7]='#'
        #n=n+1
        self.check()
        self.disp()
        a=int(input("choose the index: " + self.name1))
        if a<4:
            self.mat[0][a-1]='0'
        elif(a<7):
            self.mat[1][a-4]='0'
        else:
            self.mat[2][a-7]='0'
            print()
        #n=n+1
        self.check()
        self.game()
play=tic_tae_toe(input("player1 name"),input("player2 name"))
play.game()        
