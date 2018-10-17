# -*- coding: utf-8 -*-
'''
Jerry's games
'''
import toml

map_toml = toml.load("/home/duyw/Desktop/program/Jerry_game/map.toml")

east = map_toml["east"]
west = map_toml["west"]
north = map_toml["north"]
south = map_toml["south"]

