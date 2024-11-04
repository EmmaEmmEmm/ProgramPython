#2*2轉換
def twoTwo_T(s:list):
    a = [[s[0][0], s[1][0]], [s[0][1], s[1][1]]]
    return a
#2*3轉換
def twoThree_T(s:list):
    a = [[s[0][0], s[1][0]], [s[0][1], s[1][1]], [s[0][2], s[1][2]]]
    return a
#3*2轉換
def ThreeTwo_T(s:list):
    a = [[s[0][0], s[1][0], s[2][0]], [s[0][1], s[1][1], s[2][1]]]
    return a
#倍數乘
def double(a, b:list):
    z = []
    for i in range(len(b)):
        z.append([])
        for j in range(len(b[0])):
            z[i].append(a * b[i][j])
    return z
#乘法 3*3以下(不包含3*3)
def plus(a:list, b:list):
    z = []
    for i in range(len(a)):
        z.append([])
        for j in range(len(b[1])):
            z[i].append(a[i][0] * b[0][j] + a[i][1] * b[1][j])
    return z
# 加法
def add(a:list, b:list):
    z = []
    for i in range(len(a)):
        z.append([])
        for j in range(len(b[0])):
            z[i].append(a[i][j] + b[i][j])
    return z
# 減法
def dec(a:list, b:list):
    z = []
    for i in range(len(a)):
        z.append([])
        for j in range(len(b[0])):
            z[i].append(a[i][j] - b[i][j])
    return z
def invertible(a:list):
    if len(a) == 2:
        test = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        if test == 0:
            return "not invertible"
        else:
            print("is invertible")
            det = 1/test
            a_1 = [det * -a[0][0], det * a[1][0], det * a[0][1], det * -a[1][1]]
            return a_1
    else:
        test = a[0][0] * a[1][1] * a[2][2] + a[1][0] * a[2][1] * a[0][2] + a[2][0] * a[0][1] * a[1][2] - a[0][2] * a[1][1] * a[2][0] - a[1][2] * a[2][1] * a[0][0] - a[2][2] * a[0][1] * a[1][0]
        if test == 0:
            return "not invertible"
        else:
            print("is invertible")
            det = 1/test
            a_1 = [[det * (a[1][1] * a[2][2] - a[1][2] * a[2][1]), det * (a[1][2] * a[2][0] - a[1][0] * a[2][0]), det * (a[1][0] * a[2][1] - a[1][1] * a[2][0])] ]
            # return a_1
# 判斷 diagonal
def diagonal(a:list):
    if len(a) == 2:
        if a[0][1] == 0 & a[1][0] == 0:
            return "diagonal matrix"
        else:
            return "not diagonal matrix"
    else:
        if a[0][1] == 0 & a[1][0] == 0 & a[2][0] == 0 & a[0][2] == 0 & a[1][2] == 0 & a[2][1] == 0:
            return "diagonal matrix"
        else:
            return "not diagonal matrix"
# 判斷 symmetric
def symmetric(a:list):
    if len(a) == 2:
        if a[0][1] == a[1][0]:
            return "symmetric matrix"
        else:
            return "not symmetric matrix"
    else:
        if a[0][1] == a[1][0] & a[2][0] == a[0][2] & a[1][2] == a[2][1]:
            return "symmetric matrix"
        else:
            return "not symmetric matrix"
            