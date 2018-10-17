# -*- coding: utf-8 -*-
'''
角色设定
'''
######################################
class Hero:
    def __init__(self, name, gender, age):
        self.health=100
        self.name=name
        self.gender=gender
        self.age=age
        self.fight=30
        self.defend=30
        self.speed=30
        print('欢迎'+self.name+'来到东土世界，这里的百姓正在遭受恶魔的袭击，急需你加入战斗。')
    
    def say(self, string):
        '''
        跟英雄说话
        '''
        print(string)

    def look(self,role):
        '''
        查看其它角色的详细信息
        '''
        temp = "姓名:%s; 性别:%s; 年龄:%s岁; 战斗力:%s; 速度:%s; 防御力:%s" % (role.name, role.gender, role.age, role.fight,role.defend,role.speed)
        print(temp)

    def detail(self):
        '''
        显示主角的详细信息
        '''
        temp = "姓名:%s; 性别:%s; 年龄:%s岁; 战斗力:%s; 速度:%s; 防御力:%s" % (self.name, self.gender, self.age, self.fight,self.defend,self.speed)
        print(temp)
    
    def attack(self, target):
        '''
        让英雄攻击一次敌人
        '''
        target.health-=30

    def cleave(self, targets):
        '''
        必杀技，可以大面积杀伤敌人
        '''
        for i in targets:
            targets[i].health-=100
##########################################################################
class orge:
    def __init__(self, enemy):
        self.health = enemy[0] 
        self.skill = enemy[1]
        self.speed = enemy[2]
        self.damage= enemy[3]
