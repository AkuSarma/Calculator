from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import calculations

Window.size = (500, 600)


class NormalCalculator(Screen):
	def clear(self):
		self.ids.calc_input.text = '0'

	def button_press(self, button):
		prior = self.ids.calc_input.text

		if prior == "0" or prior == "error":
			self.ids.calc_input.text = ""
			self.ids.calc_input.text = f"{button}"

		else:
			self.ids.calc_input.text = prior + f"{button}"

	def math_sign(self, sign):
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = prior + sign

	def percent(self):
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = prior + "*" + "0.01"

	def dot(self):
		prior = self.ids.calc_input.text
		
		if "." in prior:
			pass
		
		else:
			self.ids.calc_input.text = prior + "."

	def remove(self):
		prior = self.ids.calc_input.text
		prior = prior[:-1]
		self.ids.calc_input.text = prior

	def pos_neg(self):
		prior = self.ids.calc_input.text

		if prior[0] == "-":
			self.ids.calc_input.text = prior.replace("-", "")

		else:
			self.ids.calc_input.text = "-" + prior

	def equals(self):
		prior = self.ids.calc_input.text

		try:
			answer = eval(prior)
		except Exception as e:
			print(e)
			answer = "error"
		
		answer = str(answer)

		if "." in answer:
			result = answer.split(".")
			check = int(result[1])
			if check == 0:
				self.ids.calc_input.text = result[0]
			else:
				self.ids.calc_input.text = answer

		else:
			self.ids.calc_input.text = answer


class ScientificCalculator(Screen):
	scientificSign = None # To check if there is any scientific sign used
	signUsed = None # Keep the record of the sign used
	mathSignUsed = None # keep the record of the math sign used

	def clear(self):
		NormalCalculator.clear(self)
		self.signUsed = None
		self.scientificSign = None
		self.mathSignUsed = None

	def button_press(self, button):
		NormalCalculator.button_press(self, button)

	def math_sign(self, sign):
		if self.mathSignUsed:
			self.equals()
		else:
			NormalCalculator.math_sign(self, sign)
			self.mathSignUsed = sign

	def percent(self):
		NormalCalculator.percent(self)

	def dot(self):
		NormalCalculator.dot(self)

	def remove(self):
		NormalCalculator.remove(self)

	def pos_neg(self):
		NormalCalculator.pos_neg(self)

	# New functions

	def bracket(self, bracket):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		self.ids.calc_input.text = prior + bracket

	def factorial(self):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + "!"
			self.signUsed = "!"

	def xtothepower(self):
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = prior + "**"

	def eularsNo(self):
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = prior + "*2.7182"

	def pie(self):
		prior = self.ids.calc_input.text
		self.ids.calc_input.text = prior + "*3.1416"

	def squareroot(self):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + "√"
			self.signUsed = "√"

	def trigonmetryFunction(self, func):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + func
			self.signUsed = func


	def equals(self):
		prior = self.ids.calc_input.text
		answer = ""
		try:
			answer = eval(prior)
		except Exception as e:
			print(e)
			answer = "error"

		if self.scientificSign:
			# Runs if any scientific sign is used
			answer = calculations.Cal(prior, self.signUsed, self.mathSignUsed).result()
			


			self.signUsed = None
			self.scientificSign = None
			self.mathSignUsed = None
		
		answer = str(answer)
		self.ids.calc_input.text = answer


class UnitConverter(Screen):
	def addUnit(self, unit, id):
		try:
			
			if id == "weight":
				inp = self.ids.weightInput.text
				self.ids.weightInput.text = f"{inp}{unit}"

			elif id == "length":
				inp = self.ids.lengthInput.text
				self.ids.lengthInput.text = f"{inp}{unit}"

			elif id == "time":
				inp = self.ids.timeInput.text
				self.ids.timeInput.text = f"{inp}{unit}"

			elif id == "distance":
				inp = self.ids.distanceInput.text
				self.ids.distanceInput.text = f"{inp}{unit}"

		except Exception as e:
			print(e)

	# converter for weight
	def weightConvert(self, to):
		inp = self.ids.weightInput.text

		if "kg" in inp:
			inp = inp.replace("kg", "")

			if to == "kg":
				inp = str(inp) + "kg"
				pass

			elif to == "g":
				inp = int(inp) * 1000
				inp = str(inp) + "g"

			elif to == "lbs":
				inp = int(inp) * 2.205
				inp = str(inp) + "lbs"
			else:
				inp = int(inp) * 35.274
				inp = str(inp) + "oz"

		elif "g" in inp:
			inp = inp.replace("g", "")

			if to == "kg":
				inp = int(inp) / 1000
				inp = str(inp) + "kg"

			elif to == "g":
				inp = str(inp) + "g"

			elif to == "lbs":
				inp = int(inp) / 454
				inp = str(inp) + "lbs"
			else:
				inp = int(inp) / 28.35
				inp = str(inp) + "oz"

		elif "lbs" in inp:
			inp = inp.replace("lbs", "")

			if to == "kg":
				inp = int(inp) / 2.205
				inp = str(inp) + "kg"

			elif to == "g":
				inp = int(inp) * 454
				inp = str(inp) + "g"

			elif to == "lbs":
				inp = str(inp) + "lbs"

			else:
				inp = int(inp) * 16
				inp = str(inp) + "oz"

		else:
			inp = inp.replace("oz", "")

			if to == "kg":
				inp = int(inp) * 35.274
				inp = str(inp) + "kg"

			elif to == "g":
				inp = int(inp) * 28.35
				inp = str(inp) + "g"

			elif to == "lbs":
				inp = int(inp) / 16
				inp = str(inp) + "lbs"

			else:
				inp = str(inp) + "oz"
		
		self.ids.weightInput.text = ""
		self.ids.weightAnswer.text = inp

	# Converter for length
	def lengthConvert(self, to):
		inp = self.ids.lengthInput.text

		if "km" in inp:
			inp = inp.replace("km", "")

			if to == "m":
				inp = int(inp) * 1000
				inp = str(inp) + "m"

			elif to == "km":
				inp = str(inp) + "km"

			elif to == "mi":
				inp = int(inp) / 1.609
				inp = str(inp) + "mi"
			else:
				inp = int(inp) * 1094
				inp = str(inp) + "yd"

		elif "m" in inp:
			inp = inp.replace("m", "")

			if to == "m":
				inp = str(inp) + "m"

			elif to == "km":
				inp = int(inp) / 1000
				inp = str(inp) + "km"

			elif to == "mi":
				inp = int(inp) / 1609
				inp = str(inp) + "mi"
			else:
				inp = int(inp) * 1.094
				inp = str(inp) + "yd"

		elif "mi" in inp:
			inp = inp.replace("mi", "")

			if to == "m":
				inp = int(inp) * 1609
				inp = str(inp) + "m"

			elif to == "km":
				inp = int(inp) * 1.609
				inp = str(inp) + "km"

			elif to == "mi":
				inp = str(inp) + "mi"

			else:
				inp = int(inp) * 1760
				inp = str(inp) + "yd"

		else:
			inp = inp.replace("yd", "")

			if to == "m":
				inp = int(inp) / 1.094
				inp = str(inp) + "m"

			elif to == "km":
				inp = int(inp) / 1094
				inp = str(inp) + "km"

			elif to == "mi":
				inp = int(inp) / 1760
				inp = str(inp) + "mi"

			else:
				inp = str(inp) + "yd"

		self.ids.lengthInput.text = ""
		self.ids.lengthAnswer.text = inp

	# converter for time
	def timeConvert(self, to):
		inp = self.ids.timeInput.text

		if "s" in inp:
			inp = inp.replace("s", "")

			if to == "s":
				inp = str(inp) + "s"

			elif to == "m":
				inp = int(inp) / 60
				inp = str(inp) + "m"

			elif to == "ms":
				inp = int(inp) * 1000
				inp = str(inp) + "ms"
			else:
				inp = int(inp) / 3600
				inp = str(inp) + "h"

		elif "m" in inp:
			inp = inp.replace("m", "")

			if to == "s":
				inp = int(inp) * 60
				inp = str(inp) + "s"

			elif to == "m":
				inp = str(inp) + "m"

			elif to == "ms":
				inp = int(inp) * 60000
				inp = str(inp) + "ms"
			else:
				inp = int(inp) / 60
				inp = str(inp) + "h"

		elif "ms" in inp:
			inp = inp.replace("ms", "")

			if to == "s":
				inp = int(inp) / 1000
				inp = str(inp) + "s"

			elif to == "m":
				inp = int(inp) / 60000
				inp = str(inp) + "m"

			elif to == "ms":
				inp = str(inp) + "ms"
			else:
				inp = int(inp) / 3600000
				inp = str(inp) + "h"

		else:
			inp = inp.replace("h", "")

			if to == "s":
				inp = int(inp) * 3600
				inp = str(inp) + "s"

			elif to == "m":
				inp = int(inp) * 60
				inp = str(inp) + "m"

			elif to == "ms":
				inp = int(inp) * 3600000
				inp = str(inp) + "ms"
			else:
				inp = str(inp) + "h"

		self.ids.timeInput.text = ""
		self.ids.timeAnswer.text = inp

	def distanceConvert(self, to):
		inp = self.ids.distanceInput.text

		if "m" in inp:
			inp = inp.replace("m", "")

			if to == "m":
				inp = str(inp) + "m"

			elif to == "cm":
				inp = int(inp)
				inp = str(inp) + "cm"

			elif to == "mm":
				inp = int(inp)
				inp = str(inp) + "mm"
			else:
				inp = int(inp)
				inp = str(inp) + "km"

		elif "cm" in inp:
			inp = inp.replace("cm", "")

			if to == "m":
				inp = int(inp)
				inp = str(inp) + "m"

			elif to == "cm":
				inp = str(inp) + "cm"

			elif to == "mm":
				inp = int(inp)
				inp = str(inp) + "mm"
			else:
				inp = int(inp)
				inp = str(inp) + "km"

		elif "mm" in inp:
			inp = inp.replace("mm", "")

			if to == "m":
				inp = int(inp)
				inp = str(inp) + "m"

			elif to == "cm":
				inp = int(inp)
				inp = str(inp) + "cm"

			elif to == "mm":
				inp = str(inp) + "mm"
			else:
				inp = int(inp)
				inp = str(inp) + "km"
		else:
			inp = inp.replace("km", "")

			if to == "m":
				inp = int(inp)
				inp = str(inp) + "m"

			elif to == "cm":
				inp = int(inp)
				inp = str(inp) + "cm"

			elif to == "mm":
				inp = int(inp)
				inp = str(inp) + "mm"
			else:
				inp = str(inp) + "km"

		self.ids.distanceInput.text = ""
		self.ids.distanceAnswer.text = inp

	def dataConvert(self, to):
		inp = self.ids.dataInput.text

		if "b" in inp:
			inp = inp.replace("b", "")

			if to == "b":
				inp = str(inp) + "b"

			elif to == "kb":
				inp = int(inp)
				inp = str(inp) + "kb"

			elif to == "mb":
				inp = int(inp)
				inp = str(inp) + "mb"
			else:
				inp = int(inp)
				inp = str(inp) + "gb"

		elif "kb" in inp:
			inp = inp.replace("kb", "")

			if to == "b":
				inp = int(inp)
				inp = str(inp) + "b"

			elif to == "kb":
				inp = str(inp) + "kb"

			elif to == "mb":
				inp = int(inp)
				inp = str(inp) + "mb"
			else:
				inp = int(inp)
				inp = str(inp) + "gb"

		elif "mb" in inp:
			inp = inp.replace("mb", "")

			if to == "b":
				inp = int(inp)
				inp = str(inp) + "b"

			elif to == "kb":
				inp = int(inp)
				inp = str(inp) + "kb"

			elif to == "mb":
				inp = str(inp) + "mb"
			else:
				inp = int(inp)
				inp = str(inp) + "gb"
		else:
			inp = inp.replace("gb", "")

			if to == "b":
				inp = int(inp)
				inp = str(inp) + "b"

			elif to == "kb":
				inp = int(inp)
				inp = str(inp) + "kb"

			elif to == "mb":
				inp = int(inp)
				inp = str(inp) + "mb"
			else:
				inp = str(inp) + "gb"

		self.ids.distanceInput.text = ""
		self.ids.distanceAnswer.text = inp


		

class WindowsManager(ScreenManager):
	pass


class CalculatorApp(App):
	def build(self):
		return Builder.load_file('normal.kv')


if __name__ == '__main__':
	CalculatorApp().run()
