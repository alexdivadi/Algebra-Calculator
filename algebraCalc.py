#------classes-------
class Variable():
    def __init__(self, var):
        self.var = var

    def groupTerms(self, test): #takes [6x, 4x, 6y] and makes it [6x, 4x]
        del xterm[:]
        for i in range(len(test)):
            if self.var in test[i]:
                xterm.append(test[i])
        return (xterm)
    
    def combineTerms(self, array): #takes [6x, 4x] and makes it 10.0
        array = [i.split(self.var)[0] for i in array]
        print(array)
        print(sum(float(i) for i in array))
        return sum(float(i) for i in array)
    
    def RejoinVar(self, coeff): #takes 10.0 and makes it 10.0x
        print str(coeff) + self.var


#------methods------
def trackVar(var, varObjects, testArray):
    for x in range(len(testArray)):
        if test[x].isalpha(): #check if char is alphabetical
            if len(varObjects) != 0:
                if (testArray[x] in var) == False: #don't put same var in twice
	            print(testArray[x],'is a variable.')
                    print(testArray[x])
                    b = testArray[x] #store char as variable
                    var.append(b)
                    x = Variable(b) #add an object to reference var later
                    varObjects.append(x)
            else: #same stuff
                print(testArray[x],'is a variable.')
                print(testArray[x])
                b = testArray[x]
                var.append(b)
                x = Variable(b)
                varObjects.append(x)
          

#------main------
#declare stuff
test = raw_input("Enter an expression: ")
print(test)
xterm = []
varObjects = []
var = []

#split up characters
testArray = list(test)
print(testArray)

trackVar(var, varObjects, testArray)

#Track variables -- ex. find x's

#get rid of spaces
test = test.split(" ")
print(test)

#combine like terms
for i in range(len(varObjects)):
    varObjects[i].RejoinVar(varObjects[i].combineTerms((varObjects[i].groupTerms(test))))

