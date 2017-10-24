"""
There are 3 members, Alice, Bob, and Charlie

There are 4 days with 4 shifts every day
[[*,*,*,*],[*,*,*,*],[*,*,*,*],[*,*,*,*]]

 - Alice wants to work 30h
 - Alice can work o shifts and cannot work x shifts: [[x,x,x,x],[x,o,o,o],[o,o,x,x],[o,o,o,o]]

 ... (Bob, Charlie)

"""

class Member(object):
	"""A member of the organization"""
	def __init__(self, name):
		super(Member, self).__init__()
		self.name = name
		self.schedule = Schedule()

class Schedule(object):
	"""Describes availability and desires of a Member"""
	def __init__(self, ):
		super(Schedule, self).__init__()
		self.desiredHours = desiredHours
		