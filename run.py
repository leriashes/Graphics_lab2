from asyncio.windows_events import NULL
from tabnanny import check
import pygame as pg
from figures import *
from window import *
import time

class SoftwareRender:
	def __init__(self):
		pg.init()
		self
		self.RES = self.WIDTH, self.HEIGHT = 700, 700
		self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
		self.FPS = 60
		self.screen = pg.display.set_mode(self.RES)
		self.clock = pg.time.Clock()

		self.windows = []
		self.wind = Window(0, 0, 512)

		self.figures = [
			Figure([[340, 90, 40], [40, 90, 40], [-10, 130, 4], [290, 130, 4]], 'yellow'),
			Figure([[100, 200, 15], [225, 200, 15], [300, 300, 15], [225, 400, 15],  [100, 400, 15], [25, 300, 15]], 'lightblue'),
			Figure([[160, 48, 20], [160, 448, 20], [352, 448, 20], [352, 48, 20]], 'orange'),
			Figure([[80, 192, 10], [80, 320, 10], [432, 320, 10], [432, 192, 10]], 'purple'),
			Figure([[240, 240, 25], [400, 400, 5], [480, 160, 5]], 'magenta'),
			Figure([[4, -7, 5], [50, 320, -5], [280, 551, 40]], 'violet')
			]
	   
	def depth(self, ohvat, check, win):
		ready  = True
		zmin, zmax = ohvat[0].getZ(win)
		n = 0

		for i in range(1, len(ohvat)):
			a, b = ohvat[i].getZ(win)
			
			if a > zmax:
				n = i
				zmax = b
				zmin = a

		if (win.size > 1):
			for i in range(len(ohvat)):
				if i != n:
					a, b = ohvat[i].getZ(win)
			
					if b > zmin:
						ready = False

			if ready and len(check) > 0:
				for i in range(len(check)):
					a, b = check[i].getZ(win)
					if b >= zmin:
						ready = False


		if ready:
			pg.draw.rect(self.screen, ohvat[n].color, win.proj())

		return ready

	def check_peresech(self, fig, win):
		fc = []
		peresech = False
		c = win.coord()

		for i in range(len(fig.vertexes)):
			fc.append([])
			fc[i].append(fig.vertexes[i])
			fc[i].append(fig.vertexes[(i + 1) % len(fig.vertexes)])
			
		i = 0
		while i < len(fc) and peresech == False:

			if not (fc[i][0][0] > c[2][0] and fc[i][1][0] > c[2][0] or fc[i][0][0] < c[0][0] and fc[i][1][0] < c[0][0] or fc[i][0][1] > c[2][1] and fc[i][1][1] > c[2][1] or fc[i][0][1] < c[0][1] and fc[i][1][1] < c[0][1]):
				xr = fc[i][1][0] - fc[i][0][0]
				yr = fc[i][1][1] - fc[i][0][1]
				if xr == 0:
					if (c[0][0] - fc[i][0][0]) * (c[2][0] - fc[i][0][0]) < 0:
						peresech = True
				elif yr == 0:
					if (c[0][1] - fc[i][1][1]) * (c[2][1] - fc[i][1][1]) < 0:
						peresech = True
				else:
					m = yr / xr
					b = fc[i][1][1] - m * fc[i][1][0]
					last = c[0][1] - m * c[0][0] - b
					for j in range(1, 4):
						n = c[j][1] - m * c[j][0] - b
						if last * n < 0:
							peresech = True
							break
						if last == 0:
							last = n
			i += 1
				
		return peresech

	def check_angle(self, vert, x1, x2, y1, y2):
		x = vert[0]
		y = vert[1]

		if x >= x2 and y >= y1 and y < y2:
			t = 0
		elif x > x2 and y >= y2:
			t = 1
		elif x > x1 and x <= x2 and y >= y2:
			t = 2
		elif x <= x1 and y > y2:
			t = 3
		elif x <= x1 and y > y1 and y <= y2:
			t = 4
		elif x < x1 and y <= y1:
			t = 5
		elif x >= x1 and x < x2 and y <= y1:
			t = 6
		else:
			t = 7

		return t


	def check_ohvat(self, fig, wind,r):
		fv = fig.vertexes
		ang = []

		x1 = wind.x
		x2 = wind.x + wind.size

		y1 = wind.y
		y2 = wind.y + wind.size

		for vert in fv:
			ang.append(self.check_angle(vert, x1, x2, y1, y2))

		s = 0

		for i in range(len(ang)):
			a = ang[(i + 1) % len(ang)] - ang[i]

			if a > 4:
				a -= 8
			elif a < -4:
				a += 8
			elif abs(a) == 4:
				tx1 = fv[i][0]
				tx2 = fv[(i + 1) % len(fv)][0]

				ty1 = fv[i][1]
				ty2 = fv[(i + 1) % len(fv)][1]
				
				f = Figure(fig.vertexes.copy(), fig.color)

				d = [tx1 + (y1 - ty1) * (tx2 - tx1) / (ty2 -ty1), y1]
				t = self.check_angle(d, x1, x2, y1, y2)

				if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
					d = [tx1 + (y2 - ty1) * (tx2 - tx1) / (ty2 -ty1), y2]
					t = self.check_angle(d, x1, x2, y1, y2)

					if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
						d = [x1, ty1 + (ty2 - ty1) * (x1 - tx1) / (tx2 - tx1)]
						t = self.check_angle(d, x1, x2, y1, y2)

						if (t == ang[i] or t == ang[(i + 1) % len(ang)]):
							d = [x2, ty1 + (ty2 - ty1) * (x2 - tx1) / (tx2 - tx1)]
							t = self.check_angle(d, x1, x2, y1, y2)
				
				f.vertexes.insert(i + 1, d)
				return self.check_ohvat(f, wind, r + 1)

			s += a

		return s % 8 == 0 and s != 0

	def draw(self):
		self.screen.fill(pg.Color('lightgrey'))

		pg.draw.rect(self.screen, (64, 128, 255), 
				 [92, 92, 516, 516], 2)

		for figure in self.figures:
			pg.draw.polygon(self.screen, 'black', figure.proj(), 1)

		self.windows.append(self.wind);

	def control(self):
		key = pg.key.get_pressed()
		inside = []
		out = []
		ohvat = []
		peresech = []
		
		if key[pg.K_RIGHT]:
			if (len(self.windows) != 0):
				curr_wind = self.windows.pop()
				n = 0
				i = 0

				while (i < len(self.figures)):
					fig = self.figures[i]
					coord = fig.max_min()
					wcoord = curr_wind.frame_coord()

					if coord[0] >= wcoord[1] or coord[1] <= wcoord[0] or coord[2] >= wcoord[3] or coord[3] <= wcoord[2]:	#многоугольник внешний
						n += 1
						out.append(fig)
					elif coord[0] >= wcoord[0] and coord[1] <= wcoord[1] and coord[2] >= wcoord[2] and coord[3] <= wcoord[3]: #многоугольник внутренний
						inside.append(fig)
					elif self.check_peresech(fig, curr_wind): #многоугольник пересекает окно
						peresech.append(fig)
					elif self.check_ohvat(fig, curr_wind, 1):
						ohvat.append(fig)
					else:
						n += 1
						out.append(fig)
						
					i += 1
				
				
				print('\nКоординаты окна: ', curr_wind.coord())
				print('\nВнешние: ', len(out), out)
				print('\nВнутренние: ', len(inside), inside)
				print('\nПересекающие: ', len(peresech), peresech)
				print('\nОхватывающие: ', len(ohvat), ohvat)
				print('\n')

				if n == len(self.figures):
					pg.draw.rect(self.screen, 'white', curr_wind.proj())
				else:
					if n == len(self.figures) - 1 and len(ohvat) == 1:
						pg.draw.rect(self.screen, ohvat[0].color, curr_wind.proj())
					elif len(ohvat) != 0 and not self.depth(ohvat, inside + peresech, curr_wind) or len(ohvat) == 0:
						if (curr_wind.size > 1):
							for wind in curr_wind.div():
								pg.draw.rect(self.screen, (64, 128, 255), wind.proj(), 1)
								self.windows.append(wind);
						else:
							self.depth(ohvat + inside + peresech, NULL,  curr_wind)
							
					
					
						
				if (curr_wind.size > 16):
					time.sleep(0.1)
					

	def run(self):
		pg.display.set_caption('Лабораторная работа 2')
		self.draw()
		while True:
			self.control();
			[exit() for i in pg.event.get() if i.type == pg.QUIT]
			pg.display.flip()


if __name__ == '__main__':
	app = SoftwareRender()
	app.run()
