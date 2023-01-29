BracketMaker 사용해보

#### Taekwondo Tournamnet Tree Sytem ####

### made by Park Guen Woo

import os
import pandas as pd
path = "C:\\Users\\a\\Desktop\\코드\\Project"
old_path = os.getcwd()
os.chdir(path)

team_xsl = pd.read_excel('TTTS_TEAM.xlsx',sheet_name = 'Team_rawdt')
team_len = len(team_xsl.columns)
team_dic = {}

for i in range(0,team_len):
    team_dic[team_xsl.columns[i]] = list(team_xsl[team_xsl.columns[i]].dropna())

team_name = list(team_dic.keys())

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #프로그램 실행 시 두개의 ComboBox를 동기화시키는 코드

        for i in range(0,len(team_name)):            
            self.team.addItem(f"{team_name[i]}")
            
        self.pushButton.clicked.connect(self.showText)    
        self.show()
    
        self.method.addItem('Method 1')
        self.method.addItem('Method 2')

    
    def showText(self):
        for i in range(0,len(team_name)):
            if self.team.currentText() == f'{team_name[i]}':
                self.team_lst.setText(str(team_dic[team_name[i]]).replace('[',"").replace(']',""))


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))

    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
#%%
#### Taekwondo Tournamnet Tree Sytem ####
### made by Park Guen Woo
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import os
import pandas as pd
import matplotlib.font_manager as fm
from matplotlib import rc
import networkx as nx

font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


path = "C:\\Users\\a\\Desktop\\코드\\Project"
old_path = os.getcwd()
os.chdir(path)

team_xsl = pd.read_excel('TTTS_TEAM.xlsx',sheet_name = 'Team_rawdt')
team_len = len(team_xsl.columns)
team_dic = {}

for i in range(0,team_len):
    team_dic[team_xsl.columns[i]] = list(team_xsl[team_xsl.columns[i]].dropna())

team_name = list(team_dic.keys())

team_lst = None
for i in range(0,len(team_xsl.columns)):    
    team_lst = pd.concat([team_lst, team_xsl[team_xsl.columns[i]].dropna()])

team_lst = list(team_lst)
team_lst = team_lst[:8]
#team_lst.append(1)


def seed(aa):
    seed_dic = {}
    z = aa
    while z != 1:
        seed_dic[z] = aa/2
        aa = aa/2
        z = z/2
    return seed_dic

seed_lst = seed(len(team_lst))


G = nx.Graph()
DG = nx.Graph()
pos = {}
range_lst = []

for i in range(0,len(team_lst)):
    DG.add_node(team_lst[i])
    pos[team_lst[i]] = (0,i)
            
code = [0,2,6,12]
key = list(seed_lst.keys())
for i in range(0,len(seed_lst)):
    for z in range(0,int(seed_lst[key[i]])):
        # 이부분 정교하게 짜기
        G.add_node(f'{i}{z}')
        pos[f'{i}{z}'] = (i+1, z * 2*(i+1) + 0.5 *(code[i]+1))

        #G.add_node(f'{i}{z-0.1}')=
        #pos[f'{i}{z-0.1}'] = (i+1, z * 2*(i+1) - 0.5 *(code[i]))

        #G.add_node(f'{i}{z+0.1}')
        #pos[f'{i}{z+0.1}'] = (i+1, z * 2*(i+1) + 0.5 * (code[i]))

        #G.add_edge(f'{i}{z+0.1}', f'{i}{z-0.1}')

        
nx.draw(DG, pos, with_labels = True, node_color = 'white', font_family = font_name, font_size = 10)
nx.draw(G, pos, with_labels = True, node_color = 'white', font_family = font_name, font_size = 10)


#%%
for i in range(0,len(team_lst)):
    G.add_node(team_lst[i])
    pos[team_lst[i]] = (0,i)
    if i != 0:
        G.add_node(f'{i}')
        pos[f'{i}'] = (1,i)
        if i%2 == 1:
            range_lst.append(i+0.5)
            
cnt = len(abcd(len(team_lst)))


p =0    
for p in range(0,cnt):
    range_lst2 = []
    for z in range(0,len(range_lst)):
        G.add_node(f'{p}{z}')
        pos[f'{p}{z}'] = (p+1,range_lst[z])
        
        
        
        if z%2 == 1:
            range_lst2.append(z +0.5)
    range_lst = range_lst2
            
for i in range(0,len(range_lst)):
    G.add_node(f'{P}{i}')
    pos[f'{P}{i}'] = (1,range_lst[i])
    G.add_node(f'WW{i}')
    pos[f'{P}{i}'] = (2,range_lst[i]) 





#%%

bo_ = []
nb_ = []
if len(team_lst) > 4 and len(team_lst) <8:
    bo_ = team_lst[4:]
    nb_ = team_lst[:4]
elif len(team_lst) > 8 and len(team_lst) < 16:
    bo_ = team_lst[8:]
    nb_ = team_lst[:8]
elif len(team_lst) > 16 and len(team_lst) <32:
    bo_ = (team_lst[16:])
    nb_ = team_lst[:16]

if len(bo_) > 1:
    print("참가자를 다시 작성해주세요")
#%%
# 2 4 8 16 32 가 되어야 한다.
team_lst.append(1)


if len(team_lst) > 16:
    bo_ = len(team_lst) - 16


team_lst



lenth = len(team_lst)
seed_dic = abcd(lenth)

team_lst.append('김김김')

#%%


    #%%
for p in range(0,len(abcd(len(team_lst)))):
    if len(team_lst)%2 : # ODD
        for i in range(0,abcd(len(team_lst))):
            G.add_node(f"{p차전}{i}")
            pos[f"w{i}"] = (1,i) 
        G.add_node




#%%
nx.draw_networkx_labels(G, pos, font_family=font_name , font_size=10)


#%%
nx.draw(G, pos, with_labels = True, node_color = 'white')

plt.show
nx.draw(DG)



            
            
else: # Not ODD
    for i in range(0,len(team_lst)/2):
        G.add_node("")
        for i in range(0,len(team_lst)/2):
            G.add_node("")
    
    
    
#%%




==
nx.draw(G,pos,font_family='AppleGothic',with_labels = True, node_color = 'white')

nx.draw_shell(G, pos, font_family='AppleGothic', font_size=10)

nx.draw_shell(G,pos,font_family=font_name,font_size=10)

 


G = nx.Graph()


G.add_node('김태훈')
G.add_node('박근우')
G.add_node('승자')

G.add_edge('김태훈', '승자')
G.add_edge('박근우', '승자')

pos = {}
pos['박근우'] = (0,0)
pos['김태훈'] = (0,1)
pos['승자'] = (1,1)




#%%
G=nx.star_graph(20)
pos=nx.spring_layout(G)
colors=range(20)
nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)

plt.savefig("edge_colormap.png") # save as png
plt.show() # display
