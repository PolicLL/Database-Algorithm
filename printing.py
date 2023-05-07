import algorithm
import model

##############################################

def printValues(tempAttr, tempFO):
    tempRelation = model.Relation(tempAttr, tempFO)

    print(tempRelation)

    print()

    # 3. Normalna Forma

    print("3. N F : ")

    ro = algorithm.doThirdNormalForm(tempRelation)

    print("\nRO : ")

    for element in ro:
        print(element)

    # BCNF Normal Form

    print("BCNF N F : ")

    RO_FO = algorithm.doBCNormalForm(tempRelation)

    print("\nRO : ")

    for element in RO_FO:
        print(element)

# TEST 1

tempAttr = "ABCDEFGHIJ"

listOfFD = []
listOfFD.append(model.FunctionalDependency("A","B"))
listOfFD.append(model.FunctionalDependency("C","B"))
listOfFD.append(model.FunctionalDependency("B","E"))
listOfFD.append(model.FunctionalDependency("I","J"))
listOfFD.append(model.FunctionalDependency("H","G"))
listOfFD.append(model.FunctionalDependency("A","D"))
listOfFD.append(model.FunctionalDependency("D","F"))
listOfFD.append(model.FunctionalDependency("A","H"))

print("TEST 1 : ")
printValues(tempAttr, listOfFD)

# TEST 2

tempAttr = "ABCDEFGHIJ"

listOfFD = []
listOfFD.append(model.FunctionalDependency("A","B"))
listOfFD.append(model.FunctionalDependency("C","B"))
listOfFD.append(model.FunctionalDependency("B","E"))
listOfFD.append(model.FunctionalDependency("I","J"))
listOfFD.append(model.FunctionalDependency("H","G"))

print("TEST 2 : ")
printValues(tempAttr, listOfFD)

# TEST 3

tempAttr = "ABCDEFGHIJ"

listOfFD = []
listOfFD.append(model.FunctionalDependency("DI","B"))
listOfFD.append(model.FunctionalDependency("AJ","F"))
listOfFD.append(model.FunctionalDependency("GB","FJE"))
listOfFD.append(model.FunctionalDependency("AJ","HD"))
listOfFD.append(model.FunctionalDependency("I","CG"))

print("TEST 3 : ")
printValues(tempAttr, listOfFD)





