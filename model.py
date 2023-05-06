import itertools

class FunctionalDependency:
    def __init__(self, left,right):
        self.left = ''.join(sorted(str(left)))
        self.right = ''.join(sorted(str(right)))
    def __str__(self):
     return self.left + '->' + self.right

class Relation:
    def __init__(self, attributes, listOfFO):
        self.attributes = attributes
        self.listOfFO = listOfFO
        self.keys = findPrimaryKeys(listOfFO, attributes)
    def __str__(self):
        output = "Attributes : "
        output += str(self.attributes)
        output += "\nFunctional Dependencies :  "

        for element in self.listOfFO:
            output += str(element) + " "

        output += "\nKeys : "
        for element in self.keys:
            output += str(element) + " "
        return output
    
# PK - Primary Key
def findPrimaryKeys(listOfFO, attributes): 
    candidatesPK = [] 

    allPossiblePKCombinations = getAllPossibleCombinationsForPK(attributes)

    for tempPK in allPossiblePKCombinations:
        tempPK = ''.join(tempPK)
       
        if isThereSmallerKeyInTheList(candidatesPK, tempPK):
            break

        dependentAttributesOfPK = getDependentAttributesOfPK(listOfFO, tempPK)

        if dependentAttributesOfPK == "": 
            continue

        dependentAttributesOfPK = dependentAttributesOfPK + tempPK # adding left side to the right
        dependentAttributesOfPK = ''.join(set(dependentAttributesOfPK)) # removes duplicates from str
        dependentAttributesOfPK = checkForTransitivity(listOfFO, dependentAttributesOfPK)

        # if this is primary key, add it to list candidates
        if isPKValid(attributes, dependentAttributesOfPK): 
            candidatesPK.append(tempPK)

    return candidatesPK

def getAllPossibleCombinationsForPK(attributes):
    allPossiblePKCombinations = [] 

    MIN_PK_LENGTH = 1
    MAX_PK_LENGTH = len(attributes)

    for primaryKeyLength in range(MIN_PK_LENGTH, MAX_PK_LENGTH):
        tempListPossiblePKs = itertools.combinations(attributes, primaryKeyLength)
        allPossiblePKCombinations += tempListPossiblePKs

    return allPossiblePKCombinations

def isThereSmallerKeyInTheList(candidatesPK, tempPK):
    return candidatesPK and len(candidatesPK[0]) < len(tempPK)

def getDependentAttributesOfPK(listOfFO, tempPK):
    dependentAttributeOfPK = set()

    for tempFD in listOfFO: 
        if isFirstPartSubesetOfSecondPart(tempFD.left, set(tempPK)): 
            dependentAttributeOfPK = dependentAttributeOfPK.union(set(tempFD.right)) 

    dependentAttributeOfPK = ''.join(sorted(dependentAttributeOfPK)) 

    return dependentAttributeOfPK

def isFirstPartSubesetOfSecondPart(first, second):
    return set(first).issubset(set(second))

def checkForTransitivity(listOfFO, dependentAttributesOfPK):
    count = 0
    while count < 100:
        for tempFD in listOfFO:
            if isFirstPartSubesetOfSecondPart(tempFD.left, set(dependentAttributesOfPK)): # checking for transitivity
                dependentAttributesOfPK = dependentAttributesOfPK + tempFD.right
                dependentAttributesOfPK = ''.join(set(dependentAttributesOfPK))
        count += 1
    
    return dependentAttributesOfPK

def isPKValid(attributes, dependentAttributesOfPK):
    return set(attributes).issubset(set(dependentAttributesOfPK)) and len(attributes) == len(dependentAttributesOfPK)