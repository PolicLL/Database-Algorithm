import model
import itertools


# main functions


def doThirdNormalForm(relation):
    ro = []

    for tempFunctionDep in relation.listOfFD:
        if isFunctionalDependencyInList(tempFunctionDep, ro) is False:
            ro.append(tempFunctionDep)

    for tempKey in relation.keys:
        if isKeyInList(tempKey, ro) is True:
            return ro
        
    ro.append(relation.keys[0])

    return ro


def doBCNormalForm(relation):
    ro = ''
    ro += relation.attributes
    RO_FO = []

    for tempFunctionDep in relation.listOfFD:
        if hasAllChars(ro, tempFunctionDep.left) and hasAllChars(ro, tempFunctionDep.right):
            if isSuperKey(relation.keys, tempFunctionDep) is False:
                for sign in tempFunctionDep.right:
                    ro = ro.replace(sign,'')
                RO_FO.append(tempFunctionDep)

    for element in relation.keys:
        if hasAllChars(ro,element) is True:
            ro = removeChars(ro,element)
            
            tempFO = model.FunctionalDependency(element,ro)
            RO_FO.append(tempFO) 
            return RO_FO
    
    
    tempFO = model.FunctionalDependency(relation.keys[0],ro)   
    RO_FO.append(tempFO)
    return RO_FO


# Help Functions


def isFunctionalDependencyInList(functionalDependency, list):
    for element in list:
        if element.left == functionalDependency.left and (functionalDependency.right in element.right):
            return True

    return False 


def isKeyInList(key, list):
    key = ''.join(sorted(str(key)))
    for element in list:
        temp = element.left + element.right
        temp = ''.join(sorted(str(temp)))

        if key in str(temp):
            return True

    return False


def hasAllChars(bigger, smaller):
    return all(char in bigger for char in smaller)


def isSuperKey(keys,FO):
    for key in keys:
        key = ''.join(sorted(str(key)))
        if hasAllChars(FO.left, key):
            return True
        
    return False


def removeChars(base, substring):
    for char in substring:
        base = base.replace(char, '')
    return base


