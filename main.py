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
	mathSignUsed = None

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
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + "e"
			self.signUsed = "e"

	def pie(self):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + "pie"
			self.signUsed = "pie"

	def squareroot(self):
		self.scientificSign = "Used"

		prior = self.ids.calc_input.text

		if self.signUsed:
			pass
		else:
			self.ids.calc_input.text = prior + "sqrt"
			self.signUsed = "sqrt"

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
	pass


class Converters(Screen):
	pass
		

sm = ScreenManager()
sm.add_widget(NormalCalculator(name='normalcalculator'))
sm.add_widget(ScientificCalculator(name='scientificcalculator'))
sm.add_widget(UnitConverter(name='unitconverter'))
sm.add_widget(Converters(name='converters'))


class CalculatorApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return Builder.load_file('normal.kv')


if __name__ == '__main__':
	CalculatorApp().run()
