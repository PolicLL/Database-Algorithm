import itertools

class FunctionalDependency:
    def __init__(self, left,right):
        self.left = ''.join(sorted(str(left)))
        self.right = ''.join(sorted(str(right)))
    def __str__(self):
     return self.left + '->' + self.right

class Relation:
    def __init__(self, attributes, listOfFD):
        self.attributes = attributes
        self.listOfFD = listOfFD
        self.keys = findPrimaryKeys(listOfFD, attributes)
    def __str__(self):
        output = "Attributes : "
        output += str(self.attributes)
        output += "\nFunctional Dependencies :  "

        for element in self.listOfFD:
            output += str(element) + " "

        output += "\nKeys : "
        for element in self.keys:
            output += str(element) + " "
        return output
    
# PK - Primary Key
def findPrimaryKeys(listOfFD, attributes): 
    candidatesPK = [] 

    allPossiblePKCombinations = getAllPossibleCombinationsForPK(attributes)

    for tempPK in allPossiblePKCombinations:
        tempPK = ''.join(tempPK)
       
        if isThereSmallerKeyInTheList(candidatesPK, tempPK):
            break

        dependentAttributesOfPK = getDependentAttributesOfPK(listOfFD, tempPK)

        if dependentAttributesOfPK == "": 
            continue

        dependentAttributesOfPK = dependentAttributesOfPK + tempPK # adding left side to the right
        dependentAttributesOfPK = ''.join(set(dependentAttributesOfPK)) # removes duplicates from str
        dependentAttributesOfPK = checkForTransitivity(listOfFD, dependentAttributesOfPK)

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

def getDependentAttributesOfPK(listOfFD, tempPK):
    dependentAttributeOfPK = set()

    for tempFD in listOfFD: 
        if isFirstPartSubesetOfSecondPart(tempFD.left, set(tempPK)): 
            dependentAttributeOfPK = dependentAttributeOfPK.union(set(tempFD.right)) 

    dependentAttributeOfPK = ''.join(sorted(dependentAttributeOfPK)) 

    return dependentAttributeOfPK

def isFirstPartSubesetOfSecondPart(first, second):
    return set(first).issubset(set(second))

def checkForTransitivity(listOfFD, dependentAttributesOfPK):
    for tempFD in listOfFD:
            if isFirstPartSubesetOfSecondPart(tempFD.left, set(dependentAttributesOfPK)):
                dependentAttributesOfPK = dependentAttributesOfPK + tempFD.right
                dependentAttributesOfPK = ''.join(set(dependentAttributesOfPK))
    
    return dependentAttributesOfPK

def isPKValid(attributes, dependentAttributesOfPK):
    return set(attributes).issubset(set(dependentAttributesOfPK)) and len(attributes) == len(dependentAttributesOfPK)