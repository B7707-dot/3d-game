# напиши здесь код создания и управления картой
from direct.showbase.ShowBase import ShowBase
from random import *
import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [(0.5,0.3,0.0,0.1),(0.2,0.2,0.3,1),(0.5,0.2,0.2,1),(0.0,0.6,0.0,0.1)]
        self.startNew()
    def getColor(self,z):
        if z > len(self.colors):
            a = randint(0,len(self.colors)-1)
            return self.colors[a]
        else:
            return self.colors[z-1]


    def addBlock(self,pos):
        self.block = loader.loadModel(self.model)
        self.set_texture = loader.loadTexture(self.texture)
        self.block.setTexture(self.set_texture)
        col = self.getColor(pos[2])
        self.block.setColor(col)
        self.block.setPos(pos)
        self.block.reparentTo(self.land)
        self.block.setTag('at',str(pos))
    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def LoadLand(self,filename):
        self.clear()
        with open(filename,'r') as file:
            y = 0
            for string in file:
                x = 0
                st = string.split(' ')
                for z in st:
                    z = int(z)
                    z = z+1
                    for z in range(z):
                        self.addBlock((x,y,z))
                    x = x+1
                y = y+1
    def findBlocks(self,pos):
        return self.land.findAllMatches('=at=' + str(pos))
    def findHighestEmpty(self,pos):
        x,y,z = pos
        z = 1
        while self.isEmpty((x,y,z)) != True:
            z+=1
        return x,y,z


    def delBlock(self,position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def buildBlock(self,position):
        pos = self.findHighestEmpty(position)
        self.addBlock(pos)

    
    def delBlockFrom(self,position):
        x,y,z = position
        z+=3
        sch = 0
        while self.isEmpty((x,y,z)) == True:
            sch+=1
            z-=1
            if sch == 10:
                break
        self.delBlock((x,y,z))

    def savemap(self):
        blocks = self.land.getChildren()
        count = len(blocks)
        with open('my_map.dat','wb') as f:
            pickle.dump(count,f)
            for block in blocks:
                x,y,z = block.getPos()
                pos = (int(x),int(y),int(z))
                pickle.dump(pos,f)

            








    def loadmap(self):
        self.clear()
        with open('my_map.dat','rb') as f:
            a = pickle.load(f)
            for i in range(a):
                pos = pickle.load(f)
                self.addBlock(pos)
                
                



        
        

        
            
            
                

