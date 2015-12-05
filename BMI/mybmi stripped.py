
class BMI(sex, age, height, weight, is_metric):
	is_male = (sex == 'm' or sex == 'male')
	BMR = 0.0
	BMI = 0.0
	h = height
	w = weight
	
	#convert weight and height to metric
	if !is_metric:
			h *= 2.54
			w *= 2.2
	
	#calculate BMI in metrics
	BMI = ((w)/(h/100)**2)
	
	#calculate BMR in metrics
	if is_male:
		BMR = (((13.397*w)/1) + ((4.799*h)/1) - ((5.677 * age)/1) + 88.362)
	else:
		BMR = (((9.247*w)/1) + ((3.098*h)/1) - ((4.33 * age)/1) + 447.593)
	
	def print_info():
		# print current BMI
		print ("Your current BMR is " + str (BMR) + '.')
		print (" ")
		print ("Your current BMI is " + str (BMI) + ".")
		# determine category name and set desire up and down
		if BMI < 16.00:
			catname, desiup, desidw = "Severe Thinness", 16, 0
		elif BMI < 16.99:
			catname, desiup, desidw = "Moderate Thinness", 17, 15.99
		elif BMI < 18.49:
			catname, desiup, desidw ="Mild Thinness", 18.5, 16.99
		elif BMI < 24.99:
			catname, desiup, desidw ="Normal Range", 25, 18.49
		elif BMI < 29.99:
			catname, desiup, desidw ="Overweight", 30, 24.99
		elif BMI < 34.99:
			catname, desiup, desidw ="Moderately Obese", 35, 29.99
		elif BMI < 39.99:
			catname, desiup, desidw ="Severely Obese", 40, 34.99
		elif BMI > 39.99:
			catname, desiup, desidw ="Very Severely Obese", 0, 39.99
		# print category name and how much calories to move up and down the categories
		print "You are classified in the category '" + catname + "' ."
		if desiup != 0:
			desirewu = (desiup * ((h/100)**2))
			desirebu = (((desirewu - w) / 52) * 500) / .45
			print (" ")
			print ("In order to move the next greater BMI category over 52 weeks, you must eat an extra " + str (desirebu) + " calories per day.")
		if desidw != 0:
			desirewd = (desidw * ((h/100)**2))
			desirebd = (((w - desirewd) / 52) * 500) / .45
			print (" ")
			print ("In order to move the next lesser BMI category over 52 weeks, you must eat " + str (desirebd) + " calories less per day")
		
def main():
	user_input = input("Would you like the report in Metrics (M) or U.S. Customary units (U)?  ").lower()
	is_metric = ('m' = user_input)
	
#todo: validate input
	sex = input ("Enter your sex: ").lower()	
	age = int (input ("Enter your age: "))
	height = float (input ("Enter your height in cm: "))
	weight = int (input ("Enter your weight in kg: "))
	
	bmi = BMI(sex, age, height, weight, is_metric)
	bmi.print_info()
	
main()
	

