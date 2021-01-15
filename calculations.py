class Cal:
    """
    it takes the prior text in it and also the scientific sign used 
    and the math sign used then separates the prior text with the math sign used
    and does the calculations on both the sides according to the scientific sign used
    and then returns the answer or if it can't do the calculations then returns a
    'error' as an anwer.
    """
    import math

    def __init__(self, prior, signUsed, mathSignUsed):
        self.prior = prior
        self.signUsed = signUsed
        self.mathSignUsed = mathSignUsed
        self.answer = None
        self.lis = []

    def separator(self):
        separatedList = self.prior.split(self.mathSignUsed)
        if self.signUsed in separatedList[0]:
            if self.signUsed == "!":
                separateditem = separatedList[0][:-1]
                
                self.lis.append(self.math.factorial(int(separateditem)))

            elif self.signUsed == "√":
                separateditem = separatedList[0][1:]

                self.lis.append(self.math.sqrt(int(separateditem)))

            elif self.signUsed == "sin":
                separateditem = separatedList[0].replace("sin","")

                self.lis.append(self.math.sin(int(separateditem)))

            elif self.signUsed == "cos":
                separateditem = separatedList[0].replace("cos","")

                self.lis.append(self.math.cos(int(separateditem)))

            elif self.signUsed == "tan":
                separateditem = separatedList[0].replace("tan","")

                self.lis.append(self.math.tan(int(separateditem)))

        if self.signUsed in separatedList[1]:
            if self.signUsed == "!":
                separateditem = separatedList[0][:-1]
                
                self.lis.append(self.math.factorial(int(separateditem)))

            elif self.signUsed == "√":
                separateditem = separatedList[1][1:]

                self.lis.append(self.math.sqrt(int(separateditem)))

            elif self.signUsed == "sin":
                separateditem = separatedList[0].replace("sin","")

                self.lis.append(self.math.sin(int(separateditem)))

            elif self.signUsed == "cos":
                separateditem = separatedList[0].replace("cos","")

                self.lis.append(self.math.cos(int(separateditem)))

            elif self.signUsed == "tan":
                separateditem = separatedList[0].replace("tan","")

                self.lis.append(self.math.tan(int(separateditem)))

        if self.signUsed not in separatedList[0]:
            self.lis.append(separatedList[0])

        if self.signUsed not in separatedList[1]:
            self.lis.append(separatedList[1])

    def calculator(self):
        if self.mathSignUsed == "+":
            self.answer = int(self.lis[0]) + int(self.lis[1])

        elif self.mathSignUsed == "-":
            self.answer = int(self.lis[0]) - int(self.lis[1])

        elif self.mathSignUsed == "*":
            self.answer = int(self.lis[0]) * int(self.lis[1])

        else:
            self.answer = int(self.lis[0]) / int(self.lis[1])


    def result(self):
        try:
            self.separator()
            self.calculator()
        except Exception as e:
            return "error"
        else:
            return self.answer