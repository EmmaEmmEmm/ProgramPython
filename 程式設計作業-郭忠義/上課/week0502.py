a = [2, 3, 3, 5, 7]
def Center(data:list):
    sorted(data)
    if len(data) % 2 == 0:
        i = len(data) // 2
        center = (data[i] + data[i+1])/2
    else:
         i = len(data) // 2
         center = data[i]
    return center
# def More(data:list):

print(Center(a))