# Wrap up into main()

#ask for preferred units
YorN = input("Would you like the report in Metrics (M) or U.S. Customary units (U)?  ").lower()

#if statement to use either metrics or US customary units
if YorN == 'm':
	#Done in metrics
	
	#enter info in metrics
	sex = input ("Enter your sex: ").lower()	
	age = int (input ("Enter your age: "))
	height = float (input ("Enter your height in cm: "))
	weight = int (input ("Enter your weight in kg: "))
	print (" ")
	
else:
	#Done in US customary.
	sex = input ("Enter your sex: ").lower()
	age = int (input ("Enter your age: "))
	heightin = float (input ("Enter your height in in: "))
	weightlb = float (input ("Enter your weight in lb: "))
	
	#convert from US customary to metrics
	height = heightin * 2.54
	weight = weightlb / 2.2
	
	
#calculate BMI in metrics
BMImet = ((weight)/(height/100)**2)
	
#calculate BMR in metrics
if sex == "male" or sex == 'm':
	BMRmetm = (((13.397*weight)/1) + ((4.799*height)/1) - ((5.677 * age)/1) + 88.362)
	print ("Your current BMR is " + str (BMRmetm) + '.')
	print (" ")
else:
	BMRmetf = (((9.247*weight)/1) + ((3.098*height)/1) - ((4.33 * age)/1) + 447.593)
	print ("Your current BMR is " + str (BMRmetf) + '.')
	print (" ")
	
# catname = category name
# desiup = desire up
# desidw = desire down
# desirewu = desire weight up
# desirebu = desire body up 
# desirewd = desire weight down 
# desirebd = desire body down
def BMIreport(catname, desiup=0, desidw=0):
	# print current BMI
	print ("Your current BMI is " + str (BMImet) + ".")
	# determine category name and set desire up and down
	if BMImet < 16.00:
		catname, desiup, desidw = "Severe Thinness", 16, 0
	elif BMImet < 16.99:
		catname, desiup, desidw = "Moderate Thinness", 17, 15.99
	elif BMImet < 18.49:
		catname, desiup, desidw ="Mild Thinness", 18.5, 16.99
	elif BMImet < 24.99:
		catname, desiup, desidw ="Normal Range", 25, 18.49
	elif BMImet < 29.99:
		catname, desiup, desidw ="Overweight", 30, 24.99
	elif BMImet < 34.99:
		catname, desiup, desidw ="Moderately Obese", 35, 29.99
	elif BMImet < 39.99:
		catname, desiup, desidw ="Severely Obese", 40, 34.99
	elif BMImet > 39.99:
		catname, desiup, desidw ="Very Severely Obese", 0, 39.99
	# print category name and how much calories to move up and down the categories
	print "You are classified in the category '" + catname + "' ."
	if desiup != 0:
		desirewu = (desiup * ((height/100)**2))
		desirebu = (((desirewu - weight) / 52) * 500) / .45
		print " "
		print "In order to move the next greater BMI category over 52 weeks, you must eat an extra " + str (desirebu) + " calories per day."
	if desidw != 0:
		desirewd = (desidw * ((height/100)**2))
		desirebd = (((weight - desirewd) / 52) * 500) / .45
		print " "
		print "In order to move the next lesser BMI category over 52 weeks, you must eat " + str (desirebd) + " calories less per day"
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	