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

tempFO = []
tempFO.append(model.FunctionalDependency("A","B"))
tempFO.append(model.FunctionalDependency("C","B"))
tempFO.append(model.FunctionalDependency("B","E"))
tempFO.append(model.FunctionalDependency("I","J"))
tempFO.append(model.FunctionalDependency("H","G"))
tempFO.append(model.FunctionalDependency("A","D"))
tempFO.append(model.FunctionalDependency("D","F"))
tempFO.append(model.FunctionalDependency("A","H"))

print("TEST 1 : ")
printValues(tempAttr, tempFO)

# TEST 2

tempAttr = "ABCDEFGHIJ"

tempFO = []
tempFO.append(model.FunctionalDependency("A","B"))
tempFO.append(model.FunctionalDependency("C","B"))
tempFO.append(model.FunctionalDependency("B","E"))
tempFO.append(model.FunctionalDependency("I","J"))
tempFO.append(model.FunctionalDependency("H","G"))

print("TEST 2 : ")
printValues(tempAttr, tempFO)

# TEST 3

tempAttr = "ABCDEFGHIJ"

tempFO = []
tempFO.append(model.FunctionalDependency("DI","B"))
tempFO.append(model.FunctionalDependency("AJ","F"))
tempFO.append(model.FunctionalDependency("GB","FJE"))
tempFO.append(model.FunctionalDependency("AJ","HD"))
tempFO.append(model.FunctionalDependency("I","CG"))

print("TEST 3 : ")
printValues(tempAttr, tempFO)





