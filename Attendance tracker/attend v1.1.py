# Phillip Stewart & Philip Tanwongprasert
# version 1.1
# Attendance tracker in python
# open source
# Runs with python 2.7
#
# If run without saved data file, you will be prompted for data.
# A new list of students can be input from a text file or entered manually.
#
# Program tracks attendance for a class for a given semester.
# Students may be added and dropped as necessary
# and there are options for creating reports.


import datetime
import os


SAVED_DATA = 'saved_attendance_data.txt'
ROLL_SHEET = 'student_names.txt'


def menu():
	print 'Make a selection:'
	print '  1. Mark attendance'
	print '  2. Reports'
	print '  3. Set course details'
	print '  4. Add/Drop students'
	print '  5. Quit'
	try:
		n = int(raw_input())
	except ValueError:
		print 'Invalid selection, choices are 1-5'
		n = 0
	return n

class Attendance:	
	def __init__(self):
		self.students = []
		self.course_name = ''
		self.start_date = 0
		self.end_date = 0
		self.weekdays = []
		self.dates = []
		#self.drops = []
		
	def clear_students(self):
		students = []
	
	def clear_attendance(self):
		dashes = []
		for _ in xrange(len(self.dates)):
			dashes.append('-')
		new_students = []
		for student in self.students:
			new_students.append( (student[0], student[1], dashes[:]) )
		self.students = new_students
	
	# Load previously saved data
	def load_data(self, infile):
		try:
			with open(infile, "r") as file:
				for line in file:
					if line[0] == '1':
						one,start,end,days = line.split()
						y,m,d = (int(x) for x in start.split('-'))
						self.start_date = datetime.date(y,m,d)
						y,m,d = (int(x) for x in end.split('-'))
						self.end_date = datetime.date(y,m,d)
						self.set_dates(days)
					else:
						f_name, l_name, attend = line.strip().split(', ')
						self.students.append( (f_name, l_name, list(attend)) )
			self.students.sort()
			return True
		except:
			print 'Saved data corrupted.'
			return False
			
			
	# Save data
	def save_data(self, outfile):
		with open(outfile, "w") as file:
			line = '1 ' + self.start_date.isoformat() + ' '
			line += self.end_date.isoformat() + ' '+ ','.join(self.weekdays) + '\n'
			file.write(line)
			for student in self.students:
				line = student[0] + ', ' + student[1] + ', ' + ''.join(student[2]) + '\n'
				file.write(line)

	# Read in set of students from roll-sheet file
	def set_students(self, infile):
		self.students = []
		with open(infile, 'r') as file:
			for line in file:
				l_name, f_name = line.strip().split(', ')
				self.students.append( (l_name, f_name, []) )
		self.students.sort()

	# Read in set of students from stdin
	def input_students(self):
		while True:
			print "Enter student name: (last, first) 'q' to finish"
			name = raw_input()
			if name == 'q':
				break
			l_name, f_name = name.split(', ')
			self.students.append( (l_name, f_name, []) )
		self.students.sort()
	
	# Set dates and course info
	def set_details(self, prog_start=False):
		if not prog_start:
			print 'Entering new course details will reset attendance information'
			print '  Continue: (y/n)',
			choice = raw_input()
			if choice == 'n':
				return
			if choice != 'y':
				print 'Invalid input\n'
				return
		print 'Enter the course start date: YYYY/MM/DD'
		try:
			y,m,d = (int(x) for x in raw_input().split('/'))
			self.start_date = datetime.date(y,m,d)
			print 'Enter the course end date: YYYY/MM/DD'
			y,m,d = (int(x) for x in raw_input().split('/'))
			self.end_date = datetime.date(y,m,d)
			if self.start_date >= self.end_date:
				print 'Start date cannot be later than End date. Try again.'
				self.set_details(True)
				return
		except ValueError:
			print 'Unable to read dates, try again'
			self.set_details(True)
			return
		print 'What days does the class meet?'
		print 'Enter days as "sun,mon,tue,wed,thu,fri,sat"'
		print '  ex:  mon,wed'
		days = raw_input()
		if self.set_dates(days):
			self.clear_attendance()
		else:
			self.set_details(True)
		
	def set_dates(self, days):
		try:
			days = days.split(',')
			days1 = []
			for day in days:
				if day not in days1:
					days1.append(day)
			self.weekdays = days1
			days2 = []
			day_dict = {'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}
			for day in days1:
				days2.append(day_dict[day])
			one_day = datetime.timedelta(days=1)
			day = datetime.date(self.start_date.year, self.start_date.month, self.start_date.day)
			self.dates = []
		except:
			print 'Error reading weekdays, try again.'
			return False
		while day <= self.end_date:
			if day.weekday() in days2:
				self.dates.append(day)
			day += one_day
		return True

	# Give options for marking attendance
	def mark(self):
		print 'Make a selection:'
		print '  1. Mark by date'
		print '  2. Mark by student'
		print '  3. Return to main menu'
		try:
			n = int(raw_input())
		except ValueError:
			print 'Invalid selection, choices are 1,2'
			n = 0
		if n == 0:
			pass
		elif n == 1:
			self.show_dates()
			print 'Input number: ',
			date_num = 0
			try:
				date_num = int(raw_input())
			except ValueError:
				print 'Invalid selection'
				return
			if date_num < 1 or date_num > len(self.dates):
				print 'Invalid selection'
				return
			self.show_students()
			for i in xrange(len(self.students)):
			#	if i not in self.drops:
				self.students[i][2][date_num-1] = 'O'
			print 'Mark attendance for ' + self.dates[date_num-1].isoformat()
			print 'Separate numbers by comma (ex: 3,7,11,...)'
			print '  Enter #s for students absent: ',
			absents = raw_input()
			if len(absents) > 0:
				try:
					absents = [int(x) for x in absents.split(',')]
				except ValueError:
					print 'Invalid input. Try again.'
					self.mark()
					return
			for i in absents:
				if i < 1 or i > len(self.students)+1:
					print 'Invalid input. Try again'
					self.mark()
					return
			for i in absents:
				self.students[i-1][2][date_num-1] = 'X'
			print '  Enter #s for students tardy: ',
			tardies = raw_input()
			if len(tardies) > 0:
				try:
					tardies = [int(x) for x in tardies.split(',')]
				except ValueError:
					print 'Invalid input. Try again.'
					self.mark()
					return
				for i in tardies:
					if i in absents or i < 1 or i > len(self.students)+1:
						print 'Invalid input. Dates are being marked as absent. Try again'
						self.mark()
						return
			for i in tardies:
				self.students[i-1][2][date_num-1] = 'T'
		elif n == 2:
			self.show_students()
			print 'Input number: ',
			stud_num = 0
			try:
				stud_num = int(raw_input())
			except ValueError:
				print 'Invalid selection. Try again'
				self.mark()
				return
			if stud_num < 1 or stud_num > len(self.students):
				print 'Invalid selection. Try again'
				self.mark()
				return
			for i in xrange(len(self.dates)):
				self.students[stud_num-1][2][i] = 'O'
			self.show_dates()
			print 'Mark attendance for ' + self.students[stud_num-1][0]
			print 'Separate numbers by comma (ex: 3,7,11,...)'
			print '  Enter #s for dates absent: ',
			absents = raw_input()
			if len(absents) > 0:
				try:
					absents = [int(x) for x in absents.split(',')]
				except ValueError:
					print 'Invalid selection. Try again'
					self.mark()
					return
			else:
				absents = []
			for i in absents:
				if i < 1 or i > len(self.students)+1:
					print 'Invalid input. Try again'
					self.mark()
					return
			for i in absents:
				self.students[stud_num-1][2][i-1] = 'X'
			print '  Enter #s for dates tardy: ',
			tardies = raw_input()
			if len(tardies) > 0:
				try:
					tardies = [int(x) for x in tardies.split(',')]
				except ValueError:
					print 'Invalid input. Try again.'
					self.mark()
					return
				for i in tardies:
					if i in absents or i < 1 or i > len(self.students)+1:
						print 'Invalid input. Dates are being marked as absent. Try again'
						self.mark()
						return
			else:
				tardies = []
			for i in tardies:
				self.students[stud_num-1][2][i-1] = 'T'
			today = datetime.date.today()
			d_num = 0
			while today >= self.dates[d_num]:
				d_num += 1
			for i in xrange(d_num,len(self.dates)):
				self.students[stud_num-1][2][i] = '-'
		elif n == 3:
			return
		else:
			print 'Input not recognized'
	
	# Give options for reports
	def reports(self):
		print 'Make a selection:'
		print '  1. Full attendance chart'
		print '  2. Students'
		print '  3. Course dates'
		print '  4. Return to main menu'
		try:
			n = int(raw_input())
		except ValueError:
			print 'Invalid selection, choices are 1-3'
			n = 0
		if n == 0:
			pass
		elif n == 1:
			self.show_full()
		elif n == 2:
			self.show_students()
		elif n == 3:
			self.show_dates()
		elif n == 4:
			return
		else:
			print 'Input not recognized'
	
	def add(self):
		print 'Enter student name: (last, first)'
		try:
			last, first = raw_input().split(', ')
		except ValueError:
			print 'Invalid input. Try again'
			self.add()
			return
		self.students.append( (last, first, []) )
		for _ in xrange(len(self.dates)):
			self.students[-1][2].append('-')
		self.students.sort()
		
	def drop(self):
		self.show_students()
		print 'Enter student #:'
		n = 0
		try:
			n = int(raw_input()) - 1
		except ValueError:
			print 'Invalid input'
			return
		if n < 0 or n > len(self.students) + 1:
			print 'Invalid input'
			return
		print 'Mark as drop or remove from roll? (m/r)'
		drop_type = raw_input()
		if drop_type == 'm':
			#self.drops.append(n)
			print 'Enter date dropped: (YYYY/MM/DD)'
			try:
				y,m,d = (int(x) for x in raw_input().split('/'))
				drop_date = datetime.date(y,m,d)
			except:
				print 'Date not recognized. Try again'
				self.drop()
				return
			d_num = 0
			while drop_date > self.dates[d_num] and d_num < len(self.dates):
				d_num += 1
			self.students[n][2][d_num] = 'D'
			for i in xrange(d_num+1,len(self.dates)):
				self.students[n][2][i] = '-'
		elif drop_type == 'r':
			del self.students[n]
		else:
			print 'Input not recognized'
	
	# Show full attendance chart
	def show_full(self):
		print '\nAttendance sheet:'
		nums = range(1, len(self.dates)+1)
		numstring = ''
		for i in nums:
			if i < 10:
				numstring += '_' + str(i) + '_'
			else:
				numstring += str(i) + '_'
		print 'Last,_First_________|' + numstring
		for student in self.students:
			ll = len(student[0])
			if ll > 11:
				ll = 11
			remain = 14 - ll
			print student[0][:11] + ', ' + student[1][0] + '.',
			print ' ' * remain, '|',
			for letter in student[2]:
				print letter + ' ',
			print ''
		print ''
	
	# List and enumerate students
	def show_students(self):
		print '\nAll students in course:'
		for s in enumerate(self.students):
			if s[0] < 9:
				print s[0]+1,' :',
			else:
				print s[0]+1,':',
			print s[1][0] + ', ' + s[1][1]
		print ''

	# List and enumerate meeting dates
	def show_dates(self):
		print '\nDates of course:'
		print 'Start: ', self.start_date.isoformat()
		print 'End:   ', self.end_date.isoformat()
		for d in enumerate(self.dates):
			if d[0] < 9:
				print d[0]+1, ' :', d[1].year,'/',d[1].month,'/',d[1].day
			else:
				print d[0]+1, ':',  d[1].year,'/',d[1].month,'/',d[1].day
		print ''


def main():
	A = Attendance()
	
	#try to open saved data
	print 'Searching for saved attendance data'
	if os.path.isfile(SAVED_DATA) and A.load_data(SAVED_DATA):
		print 'Attendance data loaded successfully'
	else:
		print 'Searching for roll-sheet'
		if os.path.isfile(ROLL_SHEET):
			print 'Loading student names'
			A.set_students(ROLL_SHEET)
			print 'Students successfully loaded'
		else:
			print 'No data found, please enter manually'
			A.input_students()
		A.set_details(True)
		
	while(1):
		selection = menu()
		if selection == 0:
			pass
		elif selection == 1:	#mark
			A.mark()
		elif selection == 2:	#report
			A.reports()
		elif selection == 3:	#set_details
			A.set_details()
		elif selection == 4:	#add/drop
			print 'Add or drop: (a/d)'
			add_or_drop = raw_input()
			if 'a' == add_or_drop:
				A.add()
			elif 'd' == add_or_drop:
				A.drop()
			else:
				print 'Input not recognized'
		elif selection == 5:
			break
		else:
			print 'Input not recognized'
	
	print 'Saving data and exiting program.'
	A.save_data(SAVED_DATA)


if __name__ == "__main__":
	main()
