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
    allPossiblePKCombinations = [] 
    candidatesPK = [] 

    MIN_PK_LENGTH = 1
    MAX_PK_LENGTH = len(attributes)

    for primaryKeyLength in range(MIN_PK_LENGTH, MAX_PK_LENGTH):
        tempListPossiblePKs = itertools.combinations(attributes, primaryKeyLength)
        allPossiblePKCombinations += tempListPossiblePKs

    for tempPK in allPossiblePKCombinations:
        tempPK = ''.join(tempPK)
       
        if(candidatesPK and len(candidatesPK[0]) < len(tempPK)):
            break

        primaryKeyRightSide = set() # create temp set

        for tempFD in listOfFO: 
            if set(tempFD.left).issubset(set(tempPK)): # add right side if left side is in the key
                primaryKeyRightSide = primaryKeyRightSide.union(set(tempFD.right)) # makes union between two right sides

        primaryKeyRightSide = ''.join(sorted(primaryKeyRightSide)) # values of the right side getted using list of FD

        if primaryKeyRightSide == "": # if empty skip other code
            continue

        expdandedPKRightSide = primaryKeyRightSide + tempPK # adding left side to the right
        expdandedPKRightSide = ''.join(set(expdandedPKRightSide)) # removes duplicates from str
        count = 0

        while count < 100:
            for tempFD in listOfFO:
                if set(tempFD.left).issubset(set(expdandedPKRightSide)):
                    expdandedPKRightSide = expdandedPKRightSide + tempFD.right
                    expdandedPKRightSide = ''.join(set(expdandedPKRightSide))
            count += 1

        if set(attributes).issubset(set(expdandedPKRightSide)) and len(attributes) == len(expdandedPKRightSide): # if this is primary key, add it to list candidates
            candidatesPK.append(tempPK)

    return candidatesPK
