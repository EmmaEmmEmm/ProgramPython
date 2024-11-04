import function
#pi 跟 log 用到
import math 
A = [[2, -2], [3, -5]]
B = [[-2, 0], [0, 2]]
C = [[-1, 2, 0], [2, 0, 3]]
E = [[2, -1], [math.pi, math.log10(2)], [-2, 3]]
F = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#(a)
print('(a)')
print('A + 3B = ', function.add(A, function.double(3, B)))
print("C - B*Et = ", function.dec(C, function.plus(B, function.ThreeTwo_T(E))))
print("At = ", function.twoTwo_T(A))
#(b)
print("(b)")
M = function.plus(A, B)
N = function.plus(B, A)
print("M = ", M, ", N = ", N)
if M == N:
    print("equal")
else:
    print("not eaual")
#(c)
print("(c)")
P = function.plus(function.twoThree_T(C), function.twoTwo_T(B))
Q = function.twoThree_T(function.plus(B, C))
print("P = ", P, ", Q = ", Q)
if P == Q:
    print("equal")
else:
    print("not equal")
#(d)
print("(d)")
print("A-1 =>", function.invertible(A))
print("F-1 =>", function.invertible(F))
#(e)
print("(e)")
print("A=>", function.diagonal(A))
print("B=>", function.diagonal(B))
print("F=>", function.diagonal(F))
print("I=>", function.diagonal(I))
#(f)
print("(f)")
print("A=>", function.symmetric(A))
print("B=>", function.symmetric(B))
print("F=>", function.symmetric(F))
print("I=>", function.symmetric(I))