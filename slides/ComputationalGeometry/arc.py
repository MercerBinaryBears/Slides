from math import cos, sin, pi

def distance(p1, p2):
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	return (dx * dx + dy * dy)**0.5

def equals(p1, p2, epsilon=0.001):
	return distance(p1, p2) <= epsilon

def add(p1, p2):
	return p1[0] + p2[0], p1[1] + p2[1]

def subtract(p1, p2):
	return p1[0] - p2[0], p1[1] - p2[1]

def scale(point, factor):
	return vector[0] * factor, vector[1] * factor

memo = {}
def hash_key(currentLocation, phi, theta, arcsAvailable):
	return '{0:0.5f},{1:0.5f},{2:0.5f},{3:0.5f},{4:d}'.format(currentLocation[0], currentLocation[1], phi, theta, arcsAvailable)

def memoize(currentLocation, phi, theta, arcsAvailable, value):
	global memo
	memo[hash_key(currentLocation, phi, theta, arcsAvailable)] = value
	return value

###
# phi = current direction
###
def findPoint(point, currentLocation, phi, theta, arcsAvailable):
	# Check if we've already calculated this value
	global memo
	key = hash_key(currentLocation, phi, theta, arcsAvailable)
	if key in memo:
		return memo[key]

	# If we're out of moves, but we landed at the start, we've got a match
	if arcsAvailable == 0 and equals(point, currentLocation):
		return 1
	# We're stil out of moves but not close by. Not a match
	elif arcsAvailable == 0:
		return 0
	
	# Do some "pruning" to stop chasing paths that are too far away: If we're further away than we have steps left
	# it's impossible to finish, so we're wasting our time
	if distance(point, currentLocation) > theta * arcsAvailable:
		return 0

	# try both a left and right turn. These are essentially a closed form of a rotation matrix. I think you're just
	# going to have to do the algebra...
	leftDirection = cos(phi) * sin(theta) - sin(phi) * (1 - cos(theta)), sin(phi) * sin(theta) + cos(phi) * (1 - cos(theta))
	leftLocation = add(currentLocation, leftDirection)
	totalFromLeft = findPoint(point, leftLocation, phi + theta, theta, arcsAvailable - 1)

	rightDirection = cos(phi) * sin(theta) - sin(phi) * (cos(theta) - 1), sin(phi) * sin(theta) + cos(phi) * (cos(theta) - 1)
	rightLocation = add(currentLocation, rightDirection)
	totalFromRight = findPoint(point, rightLocation, phi - theta, theta, arcsAvailable - 1)

	#return totalFromLeft + totalFromRight
	return memoize(currentLocation, phi, theta, arcsAvailable, totalFromLeft + totalFromRight)

# read the number of cases (at most 15)
N = int(raw_input().strip())

for i in range(N):
	# read in input (at most 30 steps, with 7th of circle division)
	stepCount, arcDistance = map(int, raw_input().strip().split())

	# calculate the "rotation angle" for a single turn
	theta = 2 * pi / arcDistance

	print findPoint((0, 0), (0, 0), 0, theta, stepCount)
