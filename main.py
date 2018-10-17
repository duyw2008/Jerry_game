# -*- coding: utf-8 -*-
'''
Jerry's games
'''
import map
import actor_lines as al
from roles import Hero

# 欢迎词
print(al.welcome)

# 故事背景
print(al.background)

# 创建角色Jerry
Jerry=Hero('Jerry', '男', 9)


Jerry.detail()
Jerry.look(Jerry)
