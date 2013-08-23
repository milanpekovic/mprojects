from sys import argv
import math

script, decimals = argv
decimals = int(decimals)

if decimals < 256:
    print '{0:.{dec}f}'.format(math.pi, dec = decimals)
else:
	print 'Pick a number under 256!'