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
	def addUnit(self, unit):
		try:
			inp = int(self.ids.weightInput.text)

			self.ids.weightInput.text = f"{inp}{unit}"

		except Exception as e:
			print(e)

	def convert(self, to):
		inp = self.ids.weightInput.text
		signUsed = ""

		if "kg" in inp:
			inp = inp.replace("kg", "")
			signUsed = "kg"

		elif "g" in inp:
			inp = inp.replace("g", "")
			signUsed = "g"

		elif "lb" in inp:
			inp = inp.replace("lb", "")
			signUsed = "lb"

		else:
			inp = inp.replace("ounc", "")
			signUsed = "ounc"
		
		self.ids.weightInput.text = ""
		self.ids.weightAnswer.text = inp

		

class WindowsManager(ScreenManager):
	pass


class CalculatorApp(App):
	def build(self):
		return Builder.load_file('normal.kv')


if __name__ == '__main__':
	CalculatorApp().run()
