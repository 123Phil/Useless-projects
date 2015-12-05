
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
	#Done in US.
	sex = input ("Enter your sex: ").lower()
	age = int (input ("Enter your age: "))
	heightin = float (input ("Enter your height in inches: "))
	weightlb = float (input ("Enter your weight in pounds: "))
	
	#convert from US to metrics
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
	
def bmical(catname, desiup=0, desidw=0):
	print ("You are classified in the catergory '" + catname + "' .")
	if desiup != 0:
		desirewu = (desiup * ((height/100)**2))
		desirebu = (((desirewu - weight) / 52) * 500) / .45
		print (" ")
		print ("In order to move the next greater BMI category over 52 weeks, you must eat an extra " + str (desirebu) + " calories/day.")
	if desidw != 0:
		desirewd = (desidw * ((height/100)**2))
		desirebd = (((weight - desirewd) / 52) * 500) / .45
		print (" ")
		print ("In order to move the next lesser BMI category over 52 weeks, you must eat " + str (desirebd) + " calories less per day")
	
	
#if statements to print out bmi report	
if BMImet < 16.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Severe Thinness", desiup = 16)
elif BMImet < 16.99 and BMImet > 16.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Moderate Thinness", desiup = 17, desidw = 15.99)
elif BMImet < 18.49 and BMImet > 17.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Mild Thinness", desiup = 18.5, desidw = 16.99)
elif BMImet < 24.99 and BMImet > 18.50:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Normal Range", desiup = 25, desidw = 18.49)
elif BMImet < 29.99 and BMImet > 25.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Overweight", desiup = 30, desidw = 24.99)
elif BMImet < 34.99 and BMImet > 30.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Moderately Obese", desiup = 35, desidw = 29.99)
elif BMImet < 39.99 and BMImet > 35.00:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Severely Obese", desiup = 40, desidw = 34.99)
elif BMImet > 39.99:
	print ("Your current BMI is " + str (BMImet) + ".")
	bmical ("Very Severely Obese", desidw = 39.99)
