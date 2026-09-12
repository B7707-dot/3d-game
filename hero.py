from direct.showbase.ShowBase import ShowBase
class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode = False
        self.model = 'smiley.egg'
        self.hero = loader.loadModel(self.model)
        self.hero.setColor((0.5,0.3,0.0,0.1))
        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.CameraBind()
        self.accept_events()
    def CameraBind(self):
        base.camera.setH(180)
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    def CameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0],-pos[1],-pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def turn_right(self):
        a = self.hero.getH()
        a = a-5
        self.hero.setH(a%360)

    def turn_left(self):
        a = self.hero.getH()
        a = a+5
        self.hero.setH(a%360)
    def turn_down(self):
        a = self.hero.getP()
        a = a+5
        self.hero.setP(a%360)
    def turn_up(self):
        a = self.hero.getP()
        a = a-5
        self.hero.setP(a%360)


    def k1(self):
        a = self.hero.getR()
        if a == 20:
            self.hero.setR(0)
        a = a-20
        if a ==-20:
            self.hero.setR(a%360)
    def k2(self):
        a = self.hero.getR()
        if a == 340:
            self.hero.setR(0)
        a = a+20
        if a == 20:
            self.hero.setR(a%360)



    
    

    def check_dir(self,angle):
        if (angle  >= 0 and angle <=20) or (angle >=335):
            return 0,-1
        elif angle >=20 and angle<=65:
            return 1,1
        elif angle >=65 and angle<= 110:
            return 1,0
        elif angle >=110 and angle<=155:
            return 1,1
        elif angle >=155 and angle<=200:
            return 0,1
        elif angle <=245:
            return -1,1
        elif angle <=290:
            return-1,0
        elif angle <=335:
            return -1,-1

        

    def just_move(self,angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def try_move(self,angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0],pos[1],pos[2]+1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def move_to(self,angle):
        if self.mode == True:
            self.just_move(angle)
        elif self.mode == False:
            self.try_move(angle)

    def back(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90)%360
        self.move_to(angle)
    def straight(self):
        angle = self.hero.getH()
        self.move_to(angle)

    def up(self):
        if self.mode == True:
            x = self.hero.getX()
            y = self.hero.getY()
            z = self.hero.getZ() + 1
            self.hero.setPos(x,y,z)

    def down(self):
        if self.mode == True:
            x = self.hero.getX()
            y = self.hero.getY()
            z = self.hero.getZ() - 1
            self.hero.setPos(x,y,z)

        
        
        

    

    def look_at(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())
        dx,dy = self.check_dir(angle)
        return x+dx,y+dy,z


    def changeView(self):
        if self.cameraOn == False:
            self.CameraBind()
        elif self.cameraOn == True:
            self.CameraUp()


    def build(self):
        angle = self.hero.getH()%360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)
    def destroy(self):
        angle = self.hero.getH()%360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        base.accept('c',self.changeView)
        base.accept('arrow_left',self.turn_left)
        base.accept('arrow_right',self.turn_right)
        base.accept('arrow_up',self.turn_up)
        base.accept('arrow_down',self.turn_down)
        base.accept('arrow_left' + '-repeat',self.turn_left)
        base.accept('arrow_right' + '-repeat',self.turn_right)
        base.accept('arrow_up' + '-repeat',self.turn_up)
        base.accept('arrow_down' +'-repeat',self.turn_down)


        base.accept('k',self.k1)
        base.accept('j',self.k2)



        base.accept('w',self.straight)
        base.accept('w' + '-repeat',self.straight)
        base.accept('a',self.left)
        base.accept('a' + '-repeat',self.left)
        base.accept('d',self.right)
        base.accept('d' + '-repeat',self.right)
        base.accept('s',self.back)
        base.accept('s' + '-repeat',self.back)


        base.accept('o',self.up)
        base.accept('o' + '-repeat',self.up)
        base.accept('l',self.down)
        base.accept('l' + '-repeat',self.down)

        base.accept('b',self.build)
        base.accept('v',self.destroy)

        base.accept('m',self.land.savemap)
        base.accept('n',self.land.loadmap)
        
    





    