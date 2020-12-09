import datetime as dt
from math import log

class Calculate:

	def __init__(self,rr, money, split_value):
		self.rr = rr
		self.money = money
		self.split_value = split_value # optimal split value for position size
		self.now = dt.datetime.now()
		self.output_dict = {}

		self._run()

	def _calculateOptimal(self, rr_ratio):
		self.optimal_value = rr_ratio ** log(rr_ratio, self.money)

		return self.optimal_value

	def _run(self):

		temp_money = self.money
		# bol =	temp_money / len(self.dict)
		bol =	temp_money / self.split_value 

		if (self.money >= 0):
			
			value = self._calculateOptimal(self.rr) * bol / 2
			temp_money -= value

			# self.output_dict[self.name] = {
			# "rr": self.num,
			# "optimal":round(value, 2),
			# }

			self.output_dict = round(value, 2)

			return self.output_dict

		else:
			print("Paranız bitti.")

if __name__ == "__main__":

	degerler = {
		"AYEN":5.87,
		"FONET":9.5,
		"DZGYO":7.87,

	}

	sorted_degerler = dict(sorted(degerler.items(), key = lambda x: x[1], reverse = True))

	for i, j  in zip(sorted_degerler, sorted_degerler.keys()):
		c = Calculate(sorted_degerler[i], j, 3500, 4)
		print(c._run())

# split_value 
# 4 -> Aggresive
# 5 -> Semi - Agresive
# 6 -> Defensive