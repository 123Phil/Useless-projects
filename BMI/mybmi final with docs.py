# BMI/BMR Calculator 1.1
# Modified by Phillip Stewart and Philip Tanwongprasert
# Originally by Ryan Fernando and Long Nguyen

class BMI:
	BMR = 0.0
	BMI = 0.0
	h = 0
	w = 0
	
	def __init__(self, sex, age, height, weight):
		is_male = (sex == 'm' or sex == 'male')
		self.h = height
		self.w = weight
		
		#calculate BMI in metrics
		self.BMI = ((self.w)/(self.h/100)**2)
		#calculate BMR in metrics
		if is_male:
			self.BMR = (((13.397*self.w)/1) + ((4.799*self.h)/1) - ((5.677 * age)/1) + 88.362)
		else:
			self.BMR = (((9.247*self.w)/1) + ((3.098*self.h)/1) - ((4.33 * age)/1) + 447.593)
	
	def print_data(self):
		# print current BMI
		print ("\nYour current BMR is {0:.2f}".format(self.BMR))
		print ("Your current BMI is {0:.2f}".format(self.BMI))
		# determine category name and set desire up and down
		if self.BMI < 16.00:
			catname, desiup, desidw = "Severe Thinness", 16, 0
		elif self.BMI < 16.99:
			catname, desiup, desidw = "Moderate Thinness", 17, 15.99
		elif self.BMI < 18.49:
			catname, desiup, desidw ="Mild Thinness", 18.5, 16.99
		elif self.BMI < 24.99:
			catname, desiup, desidw ="Normal Range", 25, 18.49
		elif self.BMI < 29.99:
			catname, desiup, desidw ="Overweight", 30, 24.99
		elif self.BMI < 34.99:
			catname, desiup, desidw ="Moderately Obese", 35, 29.99
		elif self.BMI < 39.99:
			catname, desiup, desidw ="Severely Obese", 40, 34.99
		elif self.BMI > 39.99:
			catname, desiup, desidw ="Very Severely Obese", 0, 39.99
		# print category name and how much calories to move up and down the categories
		print ("You are classified in the category '" + catname + "' .")
		if desiup != 0:
			desirewu = (desiup * ((self.h/100)**2))
			desirebu = (((desirewu - self.w) / 52) * 500) / .45
			print (" ")
			print ("In order to move the next greater BMI category over 52 weeks, you must eat an extra {0:.2f} calories per day.".format(desirebu))
		if desidw != 0:
			desirewd = (desidw * ((self.h/100)**2))
			desirebd = (((self.w - desirewd) / 52) * 500) / .45
			print (" ")
			print ("In order to move the next lesser BMI category over 52 weeks, you must eat {0:.2f} calories less per day".format(desirebd))


def print_info():
	print ("""
The body mass index (BMI) is a measure of relative weight based on an individual's mass and height.
Devised between 1830 and 1850 by the Belgian polymath Adolphe Quetelet during the course of developing "social physics", it is defined as the individual's body mass divided by the square of their height – with the value universally being given in units of kg/m2.
(http://en.wikipedia.org/wiki/Body_mass_index)

Basal metabolic rate (BMR), and the closely related resting metabolic rate (RMR), is the rate of energy expenditure by humans and other animals at rest, and is measured in kJ per hour per kg body mass. Rest is defined as existing in a neutrally temperate environment while in the post-absorptive state.
The release, and using, of energy in this state is sufficient only for the functioning of the vital organs: the heart, lungs, nervous system, kidneys, liver, intestine, sex organs, muscles, brain and skin.
(http://en.wikipedia.org/wiki/Basal_metabolic_rate)
		""")


def main():
	while True:
		selection = input("\nWould you like to:\n\tCalculate BMI/BMR  (c)\n\tRead BMI/BMR Info  (i)\n\tQuit               (q)\n").lower()
		
		if selection == 'q':
			break
		elif selection == 'i':
			print_info()
		elif selection == 'c':
			units_input = input("Would you like the report in Metrics (M) or U.S. Customary units (U)?  ").lower()
			is_metric = 'm' == units_input
			sex = input ("Enter your sex: ").lower()
			try:
				age = int (input ("Enter your age: "))
	
				if is_metric:
					height = float (input ("Enter your height in cm: "))
					weight = int (input ("Enter your weight in kg: "))
				else:
					height = float (input ("Enter your height in inches: ")) * 2.54
					weight = int (input ("Enter your weight in lbs: ")) / 2.2
			except ValueError:
				print ("\nInvalid input, please try again.")
				continue
			bmi = BMI(sex, age, height, weight)
			bmi.print_data()
		else:
			print ("Invalid selection, please try again.")


if __name__ == "__main__":
	main()
	

