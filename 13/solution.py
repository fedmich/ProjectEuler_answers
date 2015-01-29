def solution ( lines ):
	s = sum( [ long( line.strip() ) for line in lines ] )
	return str(s)[0:10]

f = open( 'DATA.txt', 'r')
lines = f.readlines()
f.close()
		
answer = solution( lines )
print ( answer )