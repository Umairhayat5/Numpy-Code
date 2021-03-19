# import numpy
List = range(20000000)
%time for n in range(1,10): r=[num*5 for num in List]
print(n)
