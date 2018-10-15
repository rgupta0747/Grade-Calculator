flag = True
while flag:
	name = input('Enter the name of the course: ')
	grading_categories = int(input('How many categories will be entered (Do NOT include the final): ')) #asks user number of cat.
	print()
	rubric = {}

	for i in range(grading_categories):							#gets the name/weight for each rubric
		category = input('Enter the name of the category that is graded: ')
		weight = float(input('What percentage of your grade is this category: '))
		print()
		rubric[category] = weight / 100							#converts to a decimal

	print()
	score_dict = {}
	for key in rubric:
		print('We will now enter scores for', key)					#asks the user for each score
		score_amount = int(input('How many scores would you like to enter: '))
		key_list = []
		for i in range(score_amount):
			score = float(input('Please enter the percentage you received: '))
			key_list.append(score)
		score_dict[key] = key_list

	sum = 0 				
	temp_score_dict = {}									#computes the sum of all scores 
	for key in score_dict:
		for i in range(len(score_dict[key])):
			sum += score_dict[key][i]
		temp_score_dict[key] = sum
		sum = 0

	average_score_dict = {}									#Finds the average score
	for key in score_dict:
		average_score = temp_score_dict[key] / len(score_dict[key])
		average_score_dict[key] = average_score / 100					#converts the average score to decimal

	your_grade = {}			
	percentage_list = []							
	for key in average_score_dict:								#Calculates user score for each rubric
		your_score = average_score_dict[key] * rubric[key]
		your_grade[key] = your_score
		percentage = your_grade[key] * 100						#converts number into 
		percentage_list.append(percentage)
		print()
		print('For ', key ,', you have received ', format(percentage, ',.2f'), '% out of ', format(rubric[key]*100, ',.0f'), '%', sep='')
	print()
	total_percent_before_final = 0								#This adds your percentage
	for i in percentage_list:
		total_percent_before_final += i

	weight_without_finals = 0								#This adds the percentage of each weight
	for key in rubric:
		weight_without_finals += rubric[key]

	print('Going into your final, you have ', format(total_percent_before_final, ',.2f'), '% out of a possible ', format(weight_without_finals * 100, ',.0f'), '%', sep='')
#This calculates what your final is worth
	percentage_of_final = 1 - weight_without_finals
	print('Your final is worth ', format(percentage_of_final * 100, ',.0f'), '% of your total grade.', sep='')
	while True:										#calculates final grade
		final_score = float(input('Please enter the final score you think you will receive: '))
		final_grade_weight = (final_score / 100) * percentage_of_final
		final_grade = (final_grade_weight * 100) + total_percent_before_final		
		if final_grade >= 90:								#checks final grade to breakdown
			grade_letter = 'A+'
			gpa = 6
		elif final_grade >= 85 and final_grade < 90:
			grade_letter = 'A' 
			gpa = 5.5
		elif final_grade >= 80 and final_grade < 85:
			grade_letter = 'A-'
			gpa = 5
		elif final_grade >= 77 and final_grade < 80:
			grade_letter = 'B+'
			gpa = 4.5
		elif final_grade >= 73 and final_grade < 77:
			grade_letter = 'B'
			gpa = 4
		elif final_grade >= 70 and final_grade < 73:
			grade_letter = 'B-'
			gpa = 3.5
		elif final_grade >= 67 and final_grade < 70:
			grade_letter = 'C+'
			gpa = 3
		elif final_grade >= 63 and final_grade < 67:
			grade_letter = 'C'
			gpa = 2.5
		elif final_grade >= 60 and final_grade < 63:
			grade_letter = 'C-'
			gpa= 2
		elif final_grade >= 57 and final_grade < 60:
			grade_letter = 'D+'
			gpa = 1.5
		elif final_grade >= 53 and final_grade < 57:
			grade_letter = 'D'
			gpa = 1
		elif final_grade >= 50 and final_grade < 53:
			grade_letter = 'D-'
			gpa = 0.5
		else:
			grade_letter = 'F'
			gpa = 0
		print()
		print('If you get a ', format(final_score, ',.2f'), '% on the final, then your final grade will be: ', format(final_grade, ',.2f'), '%', sep='')
		print('You will get a(n)', grade_letter, 'in this course.')
		print()
		quit = input('Would you like to quit (y/n): ').lower()		#asks user if they want to enter another final score
		if quit == 'y':
			break	
	more_courses = input('Do you want to enter more courses (y/n): ').lower()	#asks user if they want to enter another class
	if more_courses == 'n':	
		flag = False
