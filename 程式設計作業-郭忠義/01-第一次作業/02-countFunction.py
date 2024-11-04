# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    import math
    a = int(input())
    b = int(input())
    c = int(input())
    
    
    if (b*b-4*a*c) >= 0:
        x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
        
        if x1 == x2:
            print(x1)
        else:
            print('%.1f'%(x1))
            print('%.1f'%(x2))
    else:
        x1Small = abs(math.sqrt(abs(b*b-4*a*c))/(2*a))
        x1 = -b/(2*a)
        
        x2Small = abs(math.sqrt(abs(b*b-4*a*c))/(2*a))
        x2 = -b/(2*a)
        print('%.1f+%.1fi'%(x1, x1Small))
        print('%.1f-%.1fi'%(x2, x2Small))
        