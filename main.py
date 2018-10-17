# -*- coding: utf-8 -*-
'''
Jerry's games
'''
import map
from roles import Hero

print(map.east)

# 创建角色Jerry
hero=Hero('Jerry', '男', 9)


hero.detail()
hero.look(hero)
