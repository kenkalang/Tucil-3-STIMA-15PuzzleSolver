import time
import numpy as np
from copy import deepcopy
import sys
sys.setrecursionlimit(2000)

def getCost(start):
    return start.cost

# nge append + sort berdasar cost
def add(queue,start):
    queue.append(start)
    queue.sort(key=getCost)

# buat pergerakan
def ke_kiri(mat, x,y):
    a = mat[x][y]
    b = mat[x][y-1]
    mat[x][y] = b
    mat[x][y-1] = a
    return mat

def ke_kanan(mat,x,y):
    a = mat[x][y]
    b = mat[x][y+1]
    mat[x][y] = b
    mat[x][y+1] = a
    return mat

def ke_bawah(mat,x,y):
    a = mat[x][y]
    b = mat[x+1][y]
    mat[x][y] = b
    mat[x+1][y] = a
    return mat

def ke_atas(mat,x,y):
    a = mat[x][y]
    b = mat[x-1][y]
    mat[x][y] = b
    mat[x-1][y] = a
    return mat

# boolean cek bisa solve apa ga
def isSolvable(mat):
    count = 0
    list = mat.flatten()
    cek = True
    jumlahkurang = [0 for i in range(16)]
    for i in range (16):
        kurang = 0
        for j in range (i+1,16):
            if list[i] > list[j]:
                kurang += 1
                count += 1
                jumlahkurang[list[i]-1] +=1
        
    for i in range(16):
        print("Jumlah nilai kurang(" + str(i+1) + ") = " + str(jumlahkurang[i]))

    print("\n")
    

    if isBlankTileBlack(mat) == True:
        count += 1
    
    print("Jumlah kurang(i) + X adalah " + str(count) + "\n")
    if count % 2 != 0:
        cek = False
    
    return cek

# ngecek ubin kosong di arsiran atau tidak
def isBlankTileBlack(mat):
    list = mat.flatten()
    cek = False
    kosong = None
    for i in range (16):
        if list[i] == 16:
            kosong = i
            break
    for i in range (len(black_tile)):
        if kosong == black_tile[i]:
            cek = True
            break
    return cek

# hitung cost matriks belum ditambah depth
def cost(mat):
    count = 0
    cek = mat.flatten()
    sol = solution.flatten()
    for i in range (16):
        if cek[i] != 16 and cek[i] != sol[i]:
            count += 1
    
    return count

def getBlankx(mat):
    for i in range (4):
        for j in range (4):
            if mat[i][j] == 16:
                return i

def getBlanky(mat):
    for i in range (4):
        for j in range (4):
            if mat[i][j] == 16:
                return j

#fungsi print  
def displayMat(mat):
    puzzle_string = '—' * 13 + '\n'
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 16:
                puzzle_string += '│{0: >2}'.format("-")
                if j == 3:
                    puzzle_string += '│\n'
            else:
                puzzle_string += '│{0: >2}'.format(str(mat[i][j]))
                if j == 3:
                    puzzle_string += '│\n'

    puzzle_string += '—' * 13
    return puzzle_string

# untuk ngecek udah divisit belum
def isVisited(mat,queue):
    flag = False
    for i in range(len(queue)):
        if np.array_equal(mat,queue[i]):
            flag =  True
    return flag

# inti program
def solving(mat,queue,solusi,start):
    if isSolvable(mat):
        print("Puzzle dapat diselesaikan")
        penyelesaian(queue,solusi,start)
    
    else:
        print(" Puzzle tidak bisa diselesaikan")


def getBapak(start):
    return start.parent

# buat cari langkah kalo solusi dah ketemu
def cariBapak(queue,start):
    if start.parent == None:
        queue.append(start)
        return
    queue.append(start)
    cariBapak(queue,start.parent)
    
def getMatriks(start):
    return start.matriks

#tambahan
def ngePrintJalur(list):
    list.reverse()
    for i in range(len(list)):
        path = getMatriks(list[i])
        print(displayMat(path))

# Fungsi solve pakai rekursif
# def solve(mat,queue,solusi,start):
#     global visited
#     global pembangkitan
#     if np.array_equal(mat,solusi):
#         bapakMatriks = []
#         cariBapak(bapakMatriks,start)
#         print("Solusi ditemukan")
#         ngePrintJalur(bapakMatriks)
#         print ("Langkah yang ditempuh = " + str(len(bapakMatriks)))
#         print("Jumlah pembagkitan = " + str(pembangkitan + 1))
#         return
#     else:
#         tempQueue = []
#         if start.blankx != 0:
#             next = ke_atas(deepcopy(mat),start.blankx,start.blanky)
#             if isVisited(next,visited) == False:
#                 move = puzzleSolve(next, cost(next) + start.depth + 1, getBlankx(next),getBlanky(next), start.depth + 1, start)
#                 add(queue, move)
#                 tempQueue.append(move)

#                 pembangkitan += 1
#         if start.blankx != 3:
#             next = ke_bawah(deepcopy(mat),start.blankx,start.blanky)
#             if isVisited(next,visited) == False:
#                 move = puzzleSolve(next, cost(next) + start.depth + 1, getBlankx(next),getBlanky(next), start.depth + 1, start)
#                 add(queue, move)
#                 tempQueue.append(move)
#                 pembangkitan += 1
#         if start.blanky != 0:
#             next = ke_kiri(deepcopy(mat),start.blankx,start.blanky)
#             if isVisited(next,visited) == False:
#                 move = puzzleSolve(next, cost(next) + start.depth + 1, getBlankx(next),getBlanky(next), start.depth + 1, start)
#                 add(queue, move)
#                 tempQueue.append(move)
#                 pembangkitan += 1
#         if start.blanky != 3:
#             next = ke_kanan(deepcopy(mat),start.blankx,start.blanky)
#             if isVisited(next,visited) == False:
#                 move = puzzleSolve(next, cost(next) + start.depth + 1, getBlankx(next),getBlanky(next), start.depth + 1, start)
#                 add(queue, move)
#                 tempQueue.append(move)
#                 pembangkitan += 1
#         visited.append(mat)
#         path = dequeue(queue)
#         solve(path.matriks,queue,solusi,path)


# Fungsi solve pakai iterasi
def penyelesaian(queue,solusi,start):
    global visited
    global pembangkitan
    path = start
    visited.add(tuple(np.reshape(path.matriks,16)))
    while np.array_equal(path.matriks,solusi) == False:

        if path.blankx != 0:
            next = ke_atas(deepcopy(path.matriks),path.blankx,path.blanky)
            if tuple(np.reshape(next,16)) not in visited:
                move = puzzleSolve(next, cost(next) + path.depth + 1, getBlankx(next),getBlanky(next), path.depth + 1, path)
                add(queue, move)
                visited.add(tuple(np.reshape(next,16)))
                pembangkitan += 1
        if path.blankx != 3:
            next = ke_bawah(deepcopy(path.matriks),path.blankx,path.blanky)
            if tuple(np.reshape(next,16)) not in visited:
                move = puzzleSolve(next, cost(next) + path.depth + 1, getBlankx(next),getBlanky(next), path.depth + 1, path)
                add(queue, move)
                visited.add(tuple(np.reshape(next,16)))
                pembangkitan += 1
        if path.blanky != 0:
            next = ke_kiri(deepcopy(path.matriks),path.blankx,path.blanky)
            if tuple(np.reshape(next,16)) not in visited:
                move = puzzleSolve(next, cost(next) + path.depth + 1, getBlankx(next),getBlanky(next), path.depth + 1, path)
                add(queue, move)
                visited.add(tuple(np.reshape(next,16)))
                pembangkitan += 1
        if path.blanky != 3:
            next = ke_kanan(deepcopy(path.matriks),path.blankx,path.blanky)
            if tuple(np.reshape(next,16)) not in visited:
                move = puzzleSolve(next, cost(next) + path.depth + 1, getBlankx(next),getBlanky(next), path.depth + 1, path)
                add(queue, move)
                visited.add(tuple(np.reshape(next,16)))
                pembangkitan += 1
        
        path = queue.pop(0)
    
    bapakMatriks = []
    cariBapak(bapakMatriks,path)
    print("Solusi ditemukan")
    ngePrintJalur(bapakMatriks)
    print("Jumlah simpul yang dibangkitkan = " + str(pembangkitan + 1))
    queue.clear()

# baca file eksternal
def teks_to_matriks(file_eks):
    matriks = []
    with open(file_eks) as file:
        for char in file:
            matriks.append([int(i) for i in char.split()])
    return matriks

# buat simpen data parent dsb
class puzzleSolve:
    def __init__(self,matriks,cost,blankx,blanky,depth,parent):
        self.matriks = matriks
        self.cost = cost
        self.blanky = blanky
        self.blankx = blankx
        self.depth = depth
        self.parent = parent




black_tile = [1,3,4,6,9,11,12,14]
solution = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]])

pembangkitan = 0

queue = []
visited = set()

fileinput = input("Masukkan nama file : ")

dummy = np.array(teks_to_matriks("test/"+fileinput))
#buat simpul pertama
start = puzzleSolve(dummy,0,getBlankx(dummy),getBlanky(dummy),0,None)

waktu = time.time()
print(displayMat(dummy))
solving(dummy,queue,solution,start)
end = time.time()

# total time taken
print(f"Waktu berjalan program {end - waktu}" + " detik")
