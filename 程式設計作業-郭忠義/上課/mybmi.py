def computeBMI(kg, M):
    if kg>200 and M >2.5:
        return -1
    if kg<=1 or M<=0.05:
        return -1
    BMI = ((100*kg/(M*M))//1)/100
    return BMI