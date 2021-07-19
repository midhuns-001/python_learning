"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.


"""

x=10
y=105
d=30

m = x
j=0
while m <=y:
    m = m+d
    j = j+1

print (j)
     
