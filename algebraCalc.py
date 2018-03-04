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


#------methods------

#Track variables -- ex. find x's
def trackVar(var, varObjects, testArray, k):
    for x in range(len(testArray)):
        if testArray[x].isalpha(): #check if char is alphabetical
            if (testArray[x] in var) == False: #don't put same var in twice
	        print(testArray[x],'is a variable.')
                print(testArray[x])
                a = x
                b = testArray[x] #store char as variable
                var.append(b)
                a = Variable(b) #add an object to reference var later
                varObjects.append(a)
        if testArray[x].isdigit(): #check if char is constant
            print("There was a constant!")
            i = x
            print("i =",i)
            while i <= len(testArray):
                if testArray[i].isalpha():
                    break
                elif testArray[i].isdigit():
                    i = i + 1
                    try:
                        testArray[i].isdigit()
                    except IndexError:
                        print("".join(testArray[x:(i)]))
                        k.append("".join(testArray[x:(i)]))
                        print(k)
                        break
                else:
                    print("".join(testArray[x:(i)]))
                    k.append("".join(testArray[x:(i)]))
                    print(k)
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
    print(testArray)
    
    trackVar(var, varObjects, testArray, k)
    
    #get rid of spaces
    test = test.split(" ")
    print(test)
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
print(test)
testArray = test.split(" = ")
print(testArray)

exp = testArray[0]
combineLikeTerms(exp, leftcon, leftvar)
exp = testArray[1]
combineLikeTerms(exp, rightcon, rightvar)
print("Left side of equation:")
print("    Variables:", leftvar)
print("    Constants:", leftcon)
print("Right side of equation:")
print("    Variables:", rightvar)
print("    Constants:", rightcon)



