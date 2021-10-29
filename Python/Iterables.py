'''
Coded By Subhadeep Mandal
Dated:29.10.2021
Input Format:
4
a a c d
2
'''

import itertools

#Reading inputs
N=int(input())
str=input()
str1=str.replace(" ", "")
K=int(input())

#Magic
combi=list(itertools.combinations(str1,K))

a_count=0
for i in range(len(combi)):
    if 'a' in combi[i]:
        a_count+=1

Probability= a_count/len(combi)
print(Probability)
