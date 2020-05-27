
name="Dusty"
child="Pamela"
print(child)

##more examples of zip
midterm =[60,46,90,50,88]
endterm =[78,36,70,78,98]
students =["dan","arya","kimberly","anna","pam"]
#####returns dict with {student:highest score}#####using list comprehension
##final_grades = [pair for pair in zip(midterm,endterm)]###gives the pairs
final_grades = [max(pair) for pair in zip(midterm,endterm)]
print (final_grades)

# returns dict with {student:highest score}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterm, endterm)}
print(final_grades)
# returns dict with {student:highest score} USING MAP+LAMBDA
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterm, endterm)
		)
	)
)
print(final_grades)

# returns dict with student:average score

avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterm, endterm)
		)
	)
)
print(avg_grades)


