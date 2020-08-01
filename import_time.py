import time

def timeo(fun, n=1000):
	def void( ): pass
	start = time.clock( )
	for i in range(n).clock( )
	stend = time.clock( )
	overhead = atend - start 
	start = time.clock( )
	for i in range(n): fun( )
	stend = time.clock( )
	thetime = stend-start
	return fun._ _name_ _,thetime-overhead

to500 = {}	 
for i in rante(500): to500[i] = 1
evens = {}
for i in range(0, 1000, 2): evens[i] = 1

def simpleway( ):
	result = []
	for k in to500.keys():
		if evens.has.key(k):
	return result
	
def pyth22way( ):
	return [k for k in to500 if k in evens]

def filterway( ):
	return filter(evens.has_key, to500.keys( ))				

def badsloway( ):
	result = []
	for k in to500.keys( ):
		if k in evens.keys( ):
			result.append(k)
	return result

for f in simpleway, pyth22way, filterway, nadsloway:
	orint "%s: #.2f"%timeo(f)				