import algorithm
import model

##############################################

# TEST

tempFO = []
tempFO.append(model.FunctionalDependency("A","B"))
tempFO.append(model.FunctionalDependency("C","B"))
tempFO.append(model.FunctionalDependency("B","E"))
tempFO.append(model.FunctionalDependency("I","J"))
tempFO.append(model.FunctionalDependency("H","G")) 
tempFO.append(model.FunctionalDependency("A","D"))
tempFO.append(model.FunctionalDependency("D","F"))
tempFO.append(model.FunctionalDependency("A","H")) 


tempAttr = "ABCDEFGHIJ"


relacija1 = model.Relation(tempAttr, tempFO)

print(relacija1)
print()

print("3. N F : ")
ro = algorithm.doThirdNormalForm(relacija1)
print("\nRO : ")
for element in ro:
    print(element)

print("BCNF N F : ")

RO_FO = algorithm.doBCNormalForm(relacija1)
print("\nRO : ")
for element in RO_FO:
    print(element)






