def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

def appendItem(a):
    value = []
    if len(dim(a)) == 2:
        for i in range(0, len(a[0])):
            item = ''
            for j in range(0, len(a[1])):
                item = str(a[0][i]) + ' ' + str(a[1][j])
                value.append(item)
        return value
    else :
        return False
    
def generate(a):
    value = []
    if dim(a) == []:
        return 'Not a list'
    elif len(dim(a)) == 1:
        return a
    elif len(dim(a)) == 2:
        length = len(a[0])
        for i in range(0, len(a)):
            if len(a[i]) != length:
                return 'Not matched'
        if len(a) == 1:
            return a
        elif len(a) == 2:
            return appendItem(a)
        else:
            value = []
            value.append(a[0])
            if isinstance(a, list):
                a.pop(0)
            value.append(appendItem(a))
            return appendItem(value)
    else:
        for i in range(0, len(a)):
            value.append(generate(a[i]))
        return generate(value)

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [2,4,6],
        [3,6,9]
    ]
]
matrix3 = [
    [
        [
            [1, 2],
            [9, 8]
        ],
        [
            [2, 4],
            [9, 8]
        ]
    ],
    [
        [
            [1, 3],
            [2, 3]
        ],
        [
            [0, 1],
            [1, 1]
        ]
    ]
]

matrix4 = [
    'a', 'b'
]
matrix5 = [
    [1, 2],
    [1, 2, 3]
]

print(generate(matrix1))
print(generate(matrix2))
print(generate(matrix3))
print(generate(matrix4))
print(generate(matrix5))

input('Press any key to continue... ')