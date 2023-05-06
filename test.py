import unittest
import model

class TestFindPrimaryKeys(unittest.TestCase):
    def testFindPrimaryKeys(self, attributes, listOfFO, expectedPrimaryKeys):
        relation = model.Relation(attributes, listOfFO)
        primaryKeys = relation.keys

        self.assertCountEqual(primaryKeys, expectedPrimaryKeys, f"Primary keys for {attributes} and {listOfFO} are not as expected: {primaryKeys}")
        print(f"Primary keys found sucessfuly. Result : {primaryKeys}")

if __name__ == '__main__':
    
    testInputs = [
        ('ABCDEFGHIJ',
         [model.FunctionalDependency('A', 'B'), model.FunctionalDependency('C', 'B'), model.FunctionalDependency('B', 'E'),
          model.FunctionalDependency('I', 'J'), model.FunctionalDependency('H', 'G'), model.FunctionalDependency('A', 'D'),
          model.FunctionalDependency('D', 'F'), model.FunctionalDependency('A', 'H')],
         ['ACI']),

        ('ABCDEFGHIJ',
         [model.FunctionalDependency('A', 'B'), model.FunctionalDependency('C', 'B'), model.FunctionalDependency('B', 'E'),
          model.FunctionalDependency('I', 'J'), model.FunctionalDependency('H', 'G')],
         ['ACDFHI']),

        ('ABCDEFGHIJ',
         [model.FunctionalDependency('DI', 'B'), model.FunctionalDependency('AJ', 'F'), model.FunctionalDependency('GB', 'FJE'),
          model.FunctionalDependency('AJ', 'HD'), model.FunctionalDependency('I', 'CG')],
         ['ABI', 'ADI',  'AIJ'])

    ]


    for tempInput in testInputs:
        TestFindPrimaryKeys().testFindPrimaryKeys(tempInput[0], tempInput[1], tempInput[2])
