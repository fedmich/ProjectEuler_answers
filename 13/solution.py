def solution ( lines ):
	'''
	Using list comprehension, do a TRIM then convert each item into long type,
	'''
	s = sum( [ long( line.strip() ) for line in lines ] )
	
	'''
	convert s into a string then get the 1st 10 characters
	'''
	return str(s)[0:10]

'''
Open the DATA.txt file and then read contents into a list of strings
'''
f = open( 'DATA.txt', 'r')
lines = f.readlines()
f.close()
		
answer = solution( lines )
print ( answer )

# Expect answer = 5537376230