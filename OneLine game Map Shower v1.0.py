# OneLine game Map Shower
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
elements = ['▓' , '▢']

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