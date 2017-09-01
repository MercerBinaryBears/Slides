import math

class Point(object):
	def __init__(self, x=0, y=0, r=None, theta=None):
		self.x, self.y = x,y
		# convert from polar if necessary
		if r is not None and theta is not None:
			self.x = r * math.cos(theta)
			self.y = r * math.sin(theta)
	
	def __add__(self, other):
		return Point(x = self.x + other.x, y = self.y + other.y)

	def __sub__(self, other):
		return Point(x = self.x - other.x, y = self.y - other.y)

	def rotate(self, theta):
		X = self.x * math.cos(theta) - self.y * math.sin(theta)
		Y = self.x * math.sin(theta) + self.y * math.cos(theta)
		return Point(x = X, y = Y)

	def rotateAround(self, other_point, theta):
		return (self - other_point).rotate(theta) + other_point

	def __repr__(self):
		return "{0:.3f} {1:.3f}".format(self.x, self.y)

class ScheduleParser(object):
	def __init__(self, left_schedule_raw, right_schedule_raw):
		# since the total robot's mission can only be up to 100 seconds,
		# we'll just fill 100 slots
		self.left_schedule = self._parseSchedule(left_schedule_raw)
		self.right_schedule = self._parseSchedule(right_schedule_raw)

	def _parseSchedule(self, schedule_list):
		L = [0]*100
		current_block = 0
		for schedule_block in schedule_list:
			ang_velocity, duration = map(int, schedule_block.split('|'))
			L[current_block: current_block+duration] = [ang_velocity] * duration
			current_block += duration
		return L
	
	def at(self, k):
		return ( self.left_schedule[k], self.right_schedule[k] )

class Robot(object):
	def __init__(self):
		self.position = Point()
		self.heading = 0
	
	def processSchedule(self, schedule):
		for k in xrange(100):
			ang_vel_left, ang_vel_right = schedule.at(k)
			self.moveOneSecond(ang_vel_left, ang_vel_right)
		pass

	def moveOneSecond(self, ang_vel_left, ang_vel_right):
		duration = 1
		wheel_radius = 1
		wheel_base = 1
		
		# handle straight case
		if ang_vel_left == ang_vel_right:
			distance_to_travel = duration * ang_vel_left * wheel_radius
			self.position = self.position + Point(r = distance_to_travel, theta = self.heading)
			return
		
		# calculate radius of rotation (from left wheel)
		radius_of_rotation = wheel_base * ( ang_vel_right + ang_vel_left ) / 2.0 / ( ang_vel_right - ang_vel_left )

		# calculate angle of rotation (taking into account zeroes)
		rotating_around_right = ( 2 * radius_of_rotation == -wheel_base )
		angle_of_rotation = 0
		if rotating_around_right:
			angle_of_rotation = ang_vel_left * duration * wheel_radius / ( radius_of_rotation - wheel_base / 2.0 )
		else:
			angle_of_rotation = ang_vel_right * duration * wheel_radius / ( radius_of_rotation + wheel_base / 2.0 )

		# calculate center of rotation
		center_of_rotation = self.offsetAlongWheelBase(radius_of_rotation)

		# perform the rotation
		self.position = self.position.rotateAround(center_of_rotation, angle_of_rotation)
		self.heading += angle_of_rotation

	def offsetAlongWheelBase(self, offset_amount = 0):
		theta = self.heading + math.pi / 2
		return self.position + Point(r = offset_amount, theta = theta) 

	def __repr__(self):
		return repr(self.position)

# input parsing
case_count = int(raw_input())
for i in xrange(case_count):
	left_schedule_raw = raw_input().strip().split()
	right_schedule_raw = raw_input().strip().split()
	parser = ScheduleParser(left_schedule_raw, right_schedule_raw)

	r = Robot()
	r.processSchedule(parser)
	print r
