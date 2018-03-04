import math
#------classes-------
class Variable():
    def __init__(self, var):
        self.var = var

    def groupTerms(self, test, xterm): #takes [6x, 4x, 6y] and makes it [6x, 4x]
        del xterm[:]
        for i in range(len(test)):
            if self.var in test[i]:
                xterm.append(test[i])
        return (xterm)
    
    def combineTerms(self, array): #takes [6x, 4x] and makes it 10.0
        array1 = [s.strip(self.var) for s in array] # seperate var from coeff
        array1 = [s.replace(self.var, '') for s in array] # remove var
        print(array1)
        x = 0
        for i in range(len(array1)):
            check = True
            try:
                x = x + float(array1[i])
            except ValueError:
                continue
        print(x)
        return x 

    def rejoin(self, total):
        return str(total) + self.var


#------methods------

#Track variables -- ex. find x's
def trackVar(var, varObjects, testArray, k):
    skip = 0
    for x in range(len(testArray)):
        if testArray[x].isalpha(): #check if char is alphabetical
            if skip != 0:
                skip = skip - 1 #The skip makes sure it doesn't count 12 as '12' and '2'
                continue
            else:
                i = x
                while i <= len(testArray):
                    if testArray[i] != " ":
                        i = i + 1
                        try:
                            testArray[i].isdigit()
                        except IndexError:
                            whole = "".join(testArray[x:i])                 
                            if (whole in var) == False:
                                a = x
                                b = whole
                                print(b)
                                var.append(b)
                                a = Variable(b)
                                varObjects.append(a)
                                skip = len("".join(testArray[x:(i-1)]))
                                break
                    else:    
                        whole = "".join(testArray[x:i])                 
                        if (whole in var) == False: #don't put same var in twice
                            a = x
                            b = whole #store char as variable
                            print(b)
                            var.append(b)
                            a = Variable(b) #add an object to reference var later
                            varObjects.append(a)
                            skip = len("".join(testArray[x:(i-1)]))
                            break
        if testArray[x].isdigit(): #check if char is constant
            if skip != 0:
                skip = skip - 1
                continue
            else: 
                i = x
                while i <= len(testArray):
                    if testArray[i].isalpha():
                        break
                    elif testArray[i].isdigit():
                        i = i + 1
                        try:
                            testArray[i].isdigit()
                        except IndexError:
                            k.append("".join(testArray[x:(i)]))
                            skip = len("".join(testArray[x:(i)]))
                            break
                    else:
                        k.append("".join(testArray[x:(i)]))
                        skip = len("".join(testArray[x:(i)]))
                        break
#Combine Constants             
def combineConstants(k):
    return (sum(float(i) for i in k))

def combineLikeTerms(test, con, variables):
    xterm = []
    varObjects = []
    var = []
    k = []
    
    #split up characters
    testArray = list(test)

    trackVar(var, varObjects, testArray, k)
    
    #get rid of spaces
    test = test.split(" ")

    #combine like terms
    con.append(combineConstants(k))
    for i in range(len(varObjects)):
        v = varObjects[i].combineTerms(varObjects[i].groupTerms(test, xterm))
        variables.append(v)
def OneEquation(Leftx, Leftc, Rightx, Rightc):
	Leftx[0] -= Rightx[0]
	Rightx[0] -= Rightx[0]
	Rightc[0] -= Leftc[0]
	Leftc[0] -= Leftc[0]
	Rightc[0] = Rightc[0]/Leftx[0]
	print("Answer is %s" % Rightc[0])
def TwoEquation(Leftx, Leftc, Rightx, Rightc, Leftx2, Leftc2, Rightx2, Rightc2):
	Leftx[0] -= Rightx[0]  
	Leftx[1] -= Rightx[1] 	#Leftx[0] + Leftx[1] = Rightc[0]
	Rightc[0] -= Leftc[0]  	#Leftx2[0] + Leftx2[1] = Rightc2[0]
	Leftx2[0] -= Rightx2[0]
	Leftx2[1] -= Rightx2[1]
	Rightc2[0] -= Leftc2[0]
	CoeffMatrix = Leftx[0] * Leftx2[1] - Leftx[1] * Leftx2[0]
	X_Matrix = Rightc[0] * Leftx2[1] - Leftx[1] * Rightc2[0]
	Y_Matrix = Leftx[0] * Rightc2[0] - Rightc[0] * Leftx2[0]
	print("X value is: " + str(X_Matrix/CoeffMatrix) +" Y value is: " + str(Y_Matrix/CoeffMatrix))
def	Qudratic(Leftx, Leftc, Rightx, Rightc):
	Leftx[0] -= Rightx[0]
	Leftx[1] -= Rightx[1]
	Leftc[0] -=  Rightc[0]
	print(Leftx[0], Leftx[1], Leftc[0])
	if math.sqrt(Leftx[1] * Leftx[1] - 4 * Leftx[0] * Leftc[0]) > 0:
		if math.sqrt(Leftx[1] * Leftx[1] - 4 * Leftx[0] * Leftc[0]).is_integer():
			Root = math.sqrt(Leftx[1] * Leftx[1] - 4 * Leftx[0] * Leftc[0])
		print(str(Root) +" is root")
		print("Answer is " + str((((-1 * Leftx[1]) + Root) / 2 * Leftx[0])) + " and")
		print(((-1 * Leftx[1]) - Root) / 2 * Leftx[0])
	else:
		print("No real solutions")
#------main------
#declare stuff
leftcon = []
leftvar = []
rightcon = []
rightvar = []
leftcon2 = []
leftvar2 = []
rightcon2 = []
rightvar2 = []
Num = raw_input("How many equations:  ")

if Num == "1":
	Degree = raw_input("Is it quadratic? Y/N:  ")
	if Degree == "N":
		test = raw_input("Enter an equation: ")
		testArray = test.split(" = ")

		exp = testArray[0]
		combineLikeTerms(exp, leftcon, leftvar)
		exp = testArray[1]
		combineLikeTerms(exp, rightcon, rightvar)
		if rightvar == []:
			rightvar = [0]
		if leftvar == []:
			leftvar = [0]
		OneEquation(leftvar, leftcon, rightvar, rightcon)
	elif Degree == "Y":
		test = raw_input("Enter an equation:  ")
		testArray = test.split(" = ")

		exp = testArray[0]
		combineLikeTerms(exp, leftcon, leftvar)
		exp = testArray[1]
		combineLikeTerms(exp, rightcon, rightvar)
		if rightvar == []:
			rightvar = [0, 0]
		if leftvar == []:
			leftvar = [0, 0]
		Qudratic(leftvar, leftcon, rightvar, rightcon)
	else: 
		print("Invalid input")
elif Num == "2":
	#First Equation
	test = raw_input("Enter an equation: ")
	testArray = test.split(" = ")

	exp = testArray[0]
	combineLikeTerms(exp, leftcon, leftvar)
	exp = testArray[1]
	combineLikeTerms(exp, rightcon, rightvar)
	if rightvar == []:
		rightvar = [0, 0]
	if leftvar == []:
		leftvar = [0, 0]
	print("1st equation", leftvar, leftcon, rightvar, rightcon)
	#Second Equation
	test2 = raw_input("Enter another equation:  ")
	testArray2 = test2.split(" = ")

	exp2 = testArray2[0]
	combineLikeTerms(exp2, leftcon2, leftvar2)
	exp2 = testArray2[1]
	combineLikeTerms(exp2, rightcon2, rightvar2)
	if rightvar2 == []:
		rightvar2 = [0, 0]
	if leftvar2 == []:
		leftvar2 = [0, 0]
	print(leftvar, leftcon, rightvar, rightcon, leftvar2, leftcon2, rightvar2, rightcon2)
	TwoEquation(leftvar, leftcon, rightvar, rightcon, leftvar2, leftcon2, rightvar2, rightcon2)
else: 
	print("Invalid input")
	
    






