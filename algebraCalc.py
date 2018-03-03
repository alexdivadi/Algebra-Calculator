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
        array = [i.split(self.var)[0] for i in array]
        print(array)
        print(sum(float(i) for i in array))
        return sum(float(i) for i in array)
    
    def RejoinVar(self, coeff): #takes 10.0 and makes it 10.0x
        print str(coeff) + self.var


#------methods------

#Track variables -- ex. find x's
def trackVar(var, varObjects, testArray):
    for x in range(len(testArray)):
        print(testArray[x].isalpha())
        if testArray[x].isalpha(): #check if char is alphabetical
            if (testArray[x] in var) == False: #don't put same var in twice
	        print(testArray[x],'is a variable.')
                print(testArray[x])
                b = testArray[x] #store char as variable
                var.append(b)
                x = Variable(b) #add an object to reference var later
                varObjects.append(x)


def combineLikeTerms(test):
    xterm = []
    varObjects = []
    var = []

    #split up characters
    testArray = list(test)
    print(testArray)

    trackVar(var, varObjects, testArray)


    #get rid of spaces
    test = test.split(" ")
    print(test)

    #combine like terms
    for i in range(len(varObjects)):
        varObjects[i].RejoinVar(varObjects[i].combineTerms((varObjects[i].groupTerms(test, xterm))))

          

#------main------
#declare stuff
test = raw_input("Enter an expression: ")
print(test)
testArray = test.split(" = ")
print(testArray)

for i in range(len(testArray)):
    exp = testArray[i]
    combineLikeTerms(exp)



