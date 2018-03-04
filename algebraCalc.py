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
        return sum(float(i) for i in array)

    def rejoin(self, total):
        return str(total) + self.var


#------methods------

#Track variables -- ex. find x's
def trackVar(var, varObjects, testArray, k):
    skip = 0
    for x in range(len(testArray)):
        if testArray[x].isalpha(): #check if char is alphabetical
            if (testArray[x] in var) == False: #don't put same var in twice
                a = x
                b = testArray[x] #store char as variable
                var.append(b)
                a = Variable(b) #add an object to reference var later
                varObjects.append(a)
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


#------main------
#declare stuff
leftcon = []
leftvar = []
rightcon = []
rightvar = []
test = raw_input("Enter an equation: ")
testArray = test.split(" = ")

exp = testArray[0]
combineLikeTerms(exp, leftcon, leftvar)
exp = testArray[1]
combineLikeTerms(exp, rightcon, rightvar)
print("Left side of equation:")
print("    Variables: %s" % leftvar)
print("    Constants: %s" % leftcon)
print("Right side of equation:")
print("    Variables: %s" % rightvar)
print("    Constants: %s" % rightcon)



