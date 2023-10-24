class Window():
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size

	def proj(self):
		return [self.x * 16 + 94, 606 - self.y * 16 - self.size * 16, self.size * 16, self.size * 16]

	def frame_coord(self):
		return [self.x, self.x + self.size,  self.y, self.y + self.size]

	def coord(self):
		return [[self.x, self.y], [self.x, self.y + self.size], [self.x + self.size, self.y + self.size], [self.x + self.size, self.y]]

	def div(self):
		size = self.size / 2
		return [Window(self.x + size, self.y + size, size), Window(self.x, self.y + size, size), Window(self.x + size, self.y, size), Window(self.x, self.y, size)]


