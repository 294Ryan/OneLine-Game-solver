# One Line game solver
# v5.0 孤島檢查 無Bug 顯示地圖
# 大型地圖速度慢
'''
_map = [
                [-1,-1,-1,-1,0,0,0,0],
                [-1,-1,-1,0,0,0,0,-1],
                [-1,-1,0,0,0,0,0,0],
                [1,0,0,0,0,0,-1,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,-1,0,0],
                [-1,-1,-1,0,0,0,0,0]]
'''
_map = [[-1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, -1],
                [1, 0, 0, 0, -1, 0],
                [-1, 0, 0, 0, 0, 0],
                [-1, -1, 0, 0, 0, 0]]

#-------------functions-------------#

def countCanGoAround(y, x):
    count = 0
    for iY, iX in DIRECTIONS:
        nY = y + iY
        nX = x + iX
        if (0 <= nY < len(_map)) and (0 <= nX < len(_map[0])) and (_map[nY][nX] == 0):
            count += 1
    return count

def checkDead(nowStep):    
# True已經死局了
# False可以繼續試
    if nowStep == totalDot or nowStep+1 == totalDot:
        return False
    
    for r in range(len(_map)):
        for c in range(len(_map[0])):
            if _map[r][c] == 0:
                if countCanGoAround(r, c) == 0:
                    return True
    
    return False

def dfs(y, x, step):
    global times
    times += 1
    if times % 100000 == 0:    # show progress every 100000 (十萬) times
        print(f'DFS in {times}times.')
        
    _map[y][x] = step
    if step == totalDot:
        return True
    
    if checkDead(step):
        _map[y][x] = 0
        return False
    
    canGoAround = []
    for iY, iX in DIRECTIONS:
        nY = y + iY
        nX = x + iX
        if (0 <= nY < len(_map)) and (0 <= nX < len(_map[0])) and (_map[nY][nX] == 0):
            canGoNum = countCanGoAround(nY, nX)
            canGoAround.append((nY, nX, canGoNum))
    canGoAround.sort(key = lambda c: c[2])
        
    for nY, nX, _ in canGoAround:
        isCanGo = dfs(nY, nX, step+1) # try
            
        if isCanGo:
            return True
                  
    _map[y][x] = 0 # 回溯
    return False
    
def showMap():
    elements = ['▓' , '▢']
    print()
    print('The map is: ')
    for i in _map:
        for j in i:
            if j == -1:
                print(elements[0], end = '')
            else:
                print(elements[1], end = '')
        print()

    print()
    print(f'{elements[0]}is wall.')
    print(f'{elements[1]}is road.')

#-------------initialize-------------#

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

totalDot = 1
for i in _map:
    for j in i:
        if j == 0:
            totalDot += 1

start = tuple()    # find where to start
for i in range(len(_map)):
    for j in range(len(_map[0])):
        if _map[i][j] == 1:
            start = (i, j)
            break
_map[start[0]][start[1]] = 0    # 還原起點成0 還沒走

times = 0
print('init finished.')
    
#-------------main-------------#

condition = dfs(start[0], start[1], 1)      
print(f'DFS done in {times} times.')

_map[start[0]][start[1]] = 1    # 把起點標成1

showMap()

if condition:
    print('----------The ans is----------')
    for i in _map:
        for j in i:
            print(f'{j:3}', end = '  ')
        print()
else:
    print('The map has no way to finish.')