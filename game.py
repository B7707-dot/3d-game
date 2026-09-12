# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from hero import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        base.camLens.setFov(90)
        #self.land.LoadLand('land3.txt')
        #self.land.LoadLand('land.txt')
        self.land.LoadLand('land2.txt')
        self.hero = Hero((5,5,1),self.land)
game = Game()
game.run()