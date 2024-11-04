def func(a):
    for i in range(len(a)):
        h = int(a[i][0])/100
        w = int(a[i][1])*0.454
        bmi = w/(h*h)
        if h < 0.5 or h > 2.5:
            print("Input Height Error")
        elif w < 20 or w > 300:
            print("Input Weight Error")
        elif bmi < 18.5:
            print("BMI too low")
        elif bmi > 24:
            print("BMI too high")
        else:
            print("%.2f"%(bmi))
def main():
    array = []
    while 1:
        data = input()
        if data == '-1':
            break
        else:
            array.append(data.split())
    func(array)
main()
