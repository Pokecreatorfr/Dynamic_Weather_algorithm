import math

player_id = 1498921231 # random 32 bits number

region_map = [[''for x in range(28)] for i in range(15)]

day = 16
month = 7
year = 2022
hour = 8

random_count = [0 for i in range(256)]

weather_keypoints_coords = [[5,9] , [10,9] , [5,18] , [10,18]]
weather_keypoints_offset = [[0,0] , [1,0] , [0,1] , [1,1]]
weather_temp_var = 0
def pseudo_random_id(day , month , year , hour , player_id , var):
    return ((1103515245 * month*hour*(var+1) - day + player_id - year ) & (0b11111111 <<hour) >>hour)


print(pseudo_random_id(day , month , year , hour , player_id, 2))

for i in range(1):
    for x in range(12):
        for y in range(30):
            for z in range(24):
                #print(pseudo_random_id_1(y+1 , x+1 , 2020+i , z+1 , player_id))
                random_count[(pseudo_random_id(y+1 , x+1 , 2020+i , z+1 , player_id , 1)) ] += 1

#print(random_count)

for i in range(len(weather_keypoints_coords)):
    if pseudo_random_id(day , month , year , hour , player_id, i) < 75:
        region_map[weather_keypoints_coords[i][0]][weather_keypoints_coords[i][1]] = 'C'
    else :
        region_map[weather_keypoints_coords[i][0]][weather_keypoints_coords[i][1]] = 'S'

for i in range(len(weather_keypoints_coords)):
    for x in range(8):
        for y in range(14):
            print(i , x , y)
            region_map[weather_keypoints_offset[i][0]*7+x][weather_keypoints_offset[i][1]*13+y] = region_map[weather_keypoints_coords[i][0]][weather_keypoints_coords[i][1]]

for i in range(len(region_map)):
    print(region_map[i])