import math
import random
from re import S
import struct

def seed_generator():
    return random.randint(0,255) # à remplacer par un calcul a partir du player id et de la RTC


def first_pass_generation(table):
    for i in range(len(table)):
        for x in range(len(table[i])):
            if seed_generator() < 120:
                table[i][x] = 'S'
            else : 
                table[i][x] = 'C'

def second_pass_generation(table):
    for i in range(int(len(table)/2)):
        for x in range(int(len(table[i])/2)):
            s = 0
            c = 0
            for y in range(2):
                for z in range(2):
                    if table[i*2+y][x*2+z] =='S':
                        s += 1
                    else:
                        c += 1
            if c != 0 :
                if seed_generator() < (s/c)*255:
                    zone_weather = "S"
                else:
                    zone_weather = "C"
            else:
                zone_weather = "S"
            for y in range(2):
                for z in range(2):
                    table[i*2+y][x*2+z] = zone_weather

map_table = [[''for x in range(28)] for i in range(16)]

first_pass_generation(map_table)
second_pass_generation(map_table)
for i in range(len(map_table)):
    print(map_table[i])