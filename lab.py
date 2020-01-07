import argparse
parser = argparse.ArgumentParser()
parser.add_argument("maze_path")
args = parser.parse_args()
path = args.maze_path

def voln(x,y,cur,lab):
    lab[y][x] = cur
    if y+1<17:
        if lab[y+1][x] == 0 or (lab[y+1][x] != 1 and lab[y+1][x] > cur):
            voln(x,y+1,cur+10,lab)
    if x+1<17:
        if lab[y][x+1] == 0 or (lab[y][x+1] != 1 and lab[y][x+1] > cur):
            voln(x+1,y,cur+10,lab)
    if x-1>=0:
        if lab[y][x-1] == 0 or (lab[y][x-1] != 1 and lab[y][x-1] > cur):
            voln(x-1,y,cur+10,lab)
    if y-1>=0:
        if lab[y-1][x] == 0 or (lab[y-1][x] != 1 and lab[y-1][x] > cur):
            voln(x,y-1,cur+10,lab)
    return lab

def create_matrix(x1,y1,v,lab, matrix):
    x2=out_x2(lab)
    y2=out_y2(lab)
    print("("+str(x2)+','+str(y2)+')')
    x=x2    
    y=y2
    matrix[y][x]=0
    for i in range(v-10, -1, -10):
        if y+1 < 17:
            if lab[y+1][x] == i:
                y+=1
        if x+1 < 17:
            if lab[y][x+1] == i:
                x+=1
        if x-1 > -1:
            if lab[y][x-1] == i:
                x-=1
        if y-1 > -1:
            if lab[y-1][x] == i:
                y-=1
        matrix[y][x]=0

def create_matrix2(x1,y1,v,lab, matrix):
    x2=out_x2(lab)
    y2=out_y2(lab)
    x=x2    
    y=y2
    matrix[y][x]=0
    for i in range(v-10, -1, -10):
        if y+1 < 17:
            if lab[y+1][x] == i:
                y+=1
        if x+1 < 17:
            if lab[y][x+1] == i:
                x+=1
        if x-1 > -1:
            if lab[y][x-1] == i:
                x-=1
        if y-1 > -1:
            if lab[y-1][x] == i:
                y-=1
        matrix[y][x]=0

def print_lab(lab):
    print()
    for l in lab:
        for i in l:
            print("{:4d}".format(i), end='')
        print()
    print()

def search1_x(lab):# считать текущий x
    for y in range(17):
        for x in range(17):
            if lab[y][x]==2:
                return x
            
def search1_y(lab):# считать текущий y
    for y in range(17):
        for x in range(17):
            if lab[y][x]==2:
                return y
            
def search2_x(lab):# считать текущий x
    for y in range(16, -1, -1):
        for x in range(16, -1, -1):
            if lab[y][x]==2:
                return x
            
def search2_y(lab):# считать текущий y
    for y in range(16, -1, -1):
        for x in range(16, -1, -1):
            if lab[y][x]==2:
                return y
            
def out_v(lab):
    v = 10000 # ищем ближайщую точку выхода
    for i in range(17):
        if lab[0][i]>9 and lab[0][i]<v:
            v = lab[0][i]
        if lab[16][i]>9 and lab[16][i]<v:
            v = lab[16][i]
    for j in range(17):       
        if lab[j][0]>9 and lab[j][0]<v:
            v = lab[j][0]
        if lab[j][16]>9 and lab[j][16]<v:
            v = lab[j][16]
    return v

def out_y2(lab):
    v = 10000 # ищем ближайщую точку выхода
    for i in range(17):
        if lab[0][i]>9 and lab[0][i]<v:
            v = lab[0][i]
            y2 = 0
        if lab[16][i]>9 and lab[16][i]<v:
            v = lab[16][i]
            y2 = 16
    for j in range(17):       
        if lab[j][0]>9 and lab[j][0]<v:
            v = lab[j][0]
            y2 = j
        if lab[j][16]>9 and lab[j][16]<v:
            v = lab[j][16]
            y2 = j
    return y2

def out_x2(lab):
    v = 10000 # ищем ближайщую точку выхода
    for i in range(17):
        if lab[0][i]>9 and lab[0][i]<v:
            v = lab[0][i]
            x2 = i
        if lab[16][i]>9 and lab[16][i]<v:
            v = lab[16][i]
            x2 = i
    for j in range(17):       
        if lab[j][0]>9 and lab[j][0]<v:
            v = lab[j][0]
            x2 = 0
        if lab[j][16]>9 and lab[j][16]<v:
            v = lab[j][16]
            x2 = 16
    return x2

def clear(lab):
    for x in range(17):
        for y in range(17):
            if (lab[y][x]%10)==0:
                lab[y][x]=0


                
                
file = open("maze.txt")
lab = []
for line in file.readlines():
    l = line.replace('\n', '')
    lab.append([])
    for c in l:
        lab[-1].append(int(c))

print("Лабиринт:")
print_lab(lab)
        
        
matrix = []
for i in range(17):
    matrix.append([])
    for j in range(17):
        matrix[i].append(1)
matrix2 = []
for i in range(17):
    matrix2.append([])
    for j in range(17):
        matrix2[i].append(1)             

        
x1 = search1_x(lab)
y1 = search1_y(lab)
print("Положение первого робота: ("+str(x1)+','+str(y1)+')')
lab = voln(x1,y1,0,lab)
lab[y1][x1]=2
v1 = out_v(lab)
clear(lab)    
x1 = search2_x(lab)
y1 = search2_y(lab)
print("Положение второго робота: ("+str(x1)+','+str(y1)+')')
lab = voln(x1,y1,0,lab)
lab[y1][x1]=2
v2 = out_v(lab)
print() 

if v1<v2:
    clear(lab)    
    x1 = search1_x(lab)
    y1 = search1_y(lab)
    lab = voln(x1,y1,0,lab)
    lab[y1][x1]=0
    print("Волновой алгоритм для поиска кратчайшего маршрута первого робота:")
    print_lab(lab)
    print("Выход из лабиринта для первого робота: ", end='')
    create_matrix(x1,y1,v1,lab, matrix)
    print_lab(matrix)
    lab[out_y2(lab)][out_x2(lab)]=1
    clear(lab)
    x1 = search1_x(lab)
    y1 = search1_y(lab)
    lab = voln(x1,y1,0,lab)
    lab[y1][x1]=0
    v2 = out_v(lab)
    print("Волновой алгоритм для поиска кратчайшего маршрута второго робота:")
    print_lab(lab)
    print("Выход из лабиринта для второго робота: ", end='')
    create_matrix(x1,y1,v2,lab, matrix)
    create_matrix2(x1,y1,v2,lab, matrix2)
    print("Бинарная матрица отражающая оптимальный маршрут первого робота:")
    print_lab(matrix2)
    
else:
    lab[y1][x1]=0
    print("Волновой алгоритм для поиска кратчайшего маршрута второго робота:")
    print_lab(lab)
    print("Выход из лабиринта для второго робота: ", end='')
    create_matrix(x1,y1,v2,lab, matrix)
    print_lab(matrix)
    lab[out_y2(lab)][out_x2(lab)]=1
    clear(lab)    
    x1 = search1_x(lab)
    y1 = search1_y(lab)
    lab = voln(x1,y1,0,lab)
    lab[y1][x1]=0
    v1 = out_v(lab)
    print("Волновой алгоритм для поиска кратчайшего маршрута первого робота:")
    print_lab(lab)
    print("Выход из лабиринта для первого робота: ", end='')
    create_matrix(x1,y1,v1,lab, matrix)
    create_matrix2(x1,y1,v1,lab, matrix2)
    print("Бинарная матрица отражающая оптимальный маршрут второго робота:")
    print_lab(matrix2)   
print("Бинарная матрица отражающая оптимальный маршрут двух роботов:")
print_lab(matrix)
