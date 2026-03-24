# One Line game solver
# v1.0

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

# _map = [[1, 0, 0, 0, 0]]    # for test

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

visited = set()
# pathRecord = [i[:] for i in _map]
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

def dfs(y, x, step):
    
    global times
    times += 1
    if times % 100000 == 0:    # show progress every 100000 times
        print(f'DFS in {times}times.')
    if step == totalDot:
        return True
        
    for iY, iX in DIRECTIONS:
        nY = y + iY
        nX = x + iX
        
        if (0 <= nY < len(_map)) and (0 <= nX < len(_map[0])) and (_map[nY][nX] == 0):
            _map[nY][nX] = step + 1 # update the map
            canGo = dfs(nY, nX, step+1) # try
            
            if canGo:
                return True
            else:
                _map[nY][nX] = 0 # 回溯
    return False
    
#---main---#

condition = dfs(start[0], start[1], 1)      

print(f'DFS done in {times} times.')

_map[start[0]][start[1]] = 1    # 把起點標成1

if condition:
    print('----------The ans is----------')
    for i in _map:
        for j in i:
            print(f'{j:3}', end = '  ')
        print()