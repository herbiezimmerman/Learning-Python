score = input('What is the score: ')

try:

	def compute_grade(score):

		if float(score) <= 0.0:
    			print('Bad score. Please enter a score within the range of 0.1 - 0.99')
		elif  float(score) >= 1.0:
			print('Bad score. Please enter a score within the range of 0.1 - 0.99')
		elif float(score) >= 0.9:
    			print('A')
		elif float(score) >= 0.8:
			print('B')
		elif float(score) >= 0.7:
			print('C')
		elif float(score) >= 0.6:
    			print('D')
		else:
    			print('F')

	compute_grade(score)

except:
	print('Bad score. Try again.')