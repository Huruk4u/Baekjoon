import sys
import math

dis = int(sys.stdin.readline().strip())
taxiwide = ((dis**2)*2)
print("{0:.6f}".format((dis**2)*math.pi))
print("{0:.6f}".format(taxiwide))