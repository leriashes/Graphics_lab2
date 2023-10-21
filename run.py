import pygame as pg
class SoftwareRender:
	def __init__(self):
		pg.init()
		self.RES = self.WIDTH, self.HEIGHT = 1200, 900
		self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
		self.FPS = 60
		self.screen = pg.display.set_mode(self.RES)
		self.clock = pg.time.Clock()

		self.windows = []
		self.wind_size = [200, 50, 800, 800]
	   

	def draw(self):
		self.screen.fill(pg.Color('lightgrey'))
		pg.draw.rect(self.screen, (64, 128, 255), 
				 self.wind_size, 2)

		pg.draw.polygon(self.screen, 'black', [[350, 60], [380, 100], 
					 [290, 140], [230, 80]], 1)

		pg.draw.polygon(self.screen, 'black', [[350, 250], [780, 100], 
					 [730, 780]], 1)

		pg.draw.polygon(self.screen, 'black', [[220, 250], [220, 790], 
					 [830, 790], [830, 250]], 1)

		self.windows.append(self.wind_size);

	def control(self):
		key = pg.key.get_pressed()
		if (len(self.windows) != 0):
			curr_wind = self.windows.pop()

			if (curr_wind[3] > 1):
				w = curr_wind.copy()
				w[2] /= 2
				w[3] /=2
				pg.draw.rect(self.screen, (64, 128, 255), w, 1)
				self.windows.append(w.copy());

				w[0] += w[2]
				pg.draw.rect(self.screen, (64, 128, 255), w, 1)
				self.windows.append(w.copy());

				w[1] += w[3]
				pg.draw.rect(self.screen, (64, 128, 255), w, 1)
				self.windows.append(w.copy());

				w[0] -= w[2]
				pg.draw.rect(self.screen, (64, 128, 255), w, 1)
				self.windows.append(w.copy());
		#if key[pg.K_RIGHT]:
			


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
