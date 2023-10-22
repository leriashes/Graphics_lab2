class Figure:
	def __init__(self, vertexes, color):
		self.vertexes = vertexes
		self.color = color

	def proj(self):
		res = []
		v = []

		for i in range(len(self.vertexes)):
			res.append([])
			
			res[i].append(self.vertexes[i][0] + 94)
			res[i].append(605 - self.vertexes[i][1])

			v.append(res[i].copy())
			

		for k in range(1, len(res) - 1):
			if v[k][0] > v[k - 1][0] or v[k][0] > v[k + 1][0]:
					res[k][0] -= 1;	
			if v[k][1] < v[k - 1][1] or v[k][1] < v[k + 1][1]:
					res[k][1] += 1;	

		if v[0][0] > v[len(res) - 1][0] or v[0][0] > v[1][0]:
				res[0][0] -= 1;	
		if v[0][1] < v[len(res) - 1][1] or v[0][1] < v[1][1]:
				res[0][1] += 1;	

		if v[len(res) - 1][0] > v[len(res) - 2][0] or v[len(res) - 1][0] > v[0][0]:
				res[len(res) - 1][0] -= 1;	
		if v[len(res) - 1][1] < v[len(res) - 2][1] or v[len(res) - 1][1] < v[0][1]:
				res[len(res) - 1][1] += 1;	

		return res

	def max_min(self):
		#coord = self.proj()

		#x_min = coord[0][0]
		#x_max = coord[0][0]
		#y_min = coord[0][1]
		#y_max = coord[0][1]

		#for i in range(len(coord)):
		#	if (coord[i][0] < x_min):
		#		x_min = coord[i][0]
		#	if (coord[i][0] > x_max):
		#		x_max = coord[i][0]
		#	if (coord[i][1] < y_min):
		#		y_min = coord[i][1]
		#	if (coord[i][1] > y_max):
		#		y_max = coord[i][1]

		x_min = self.vertexes[0][0]
		x_max = self.vertexes[0][0]
		y_min = self.vertexes[0][1]
		y_max = self.vertexes[0][1]

		for i in range(len(self.vertexes)):
			if (self.vertexes[i][0] < x_min):
				x_min = self.vertexes[i][0]
			if (self.vertexes[i][0] > x_max):
				x_max = self.vertexes[i][0]
			if (self.vertexes[i][1] < y_min):
				y_min = self.vertexes[i][1]
			if (self.vertexes[i][1] > y_max):
				y_max = self.vertexes[i][1]

		return [x_min, x_max, y_min, y_max]