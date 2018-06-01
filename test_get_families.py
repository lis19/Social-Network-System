import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
    def test_get_families_one_person_multiple_friends_same_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy', 'Alex Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Alex', 'Claire', 'Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    
    def test_get_families_one_person_multiple_friends_diff_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Luke'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_get_families_multiple_people_one_friend_same_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy'], 'Gloria Dunphy': ['Haley Gwendolyn Dunphy'], 'Jay Dunphy': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Gloria', 'Haley Gwendolyn', 'Jay', 'Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
        
    def test_get_families_multiple_people_one_friend_diff_family(self):
        param = {'Claire Dunphy': ['Manny Delgado'], 'Jay Pritchett': ['Dylan D-Money']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire'], 'Delgado': ['Manny'], 'Pritchett': ['Jay'], 'D-Money': ['Dylan']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)         
                
                
    def test_get_families_multiple_people_multiple_friend_same_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy', 'Alex Dunphy'], 'Phil Dunphy': ['Haley Gwendolyn Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn', 'Luke', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)                    
        
        
    def test_get_families_multiple_people_multiple_friend_diff_family(self):
        param = {'Claire Dunphy': ['Luke Dunphy', 'Manny Delgado'], 'Gloria Pritchett': ['Haley Gwendolyn Dunphy'], 'Jay Pritchett': ['Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Haley Gwendolyn', 'Luke'], 'Delgado': ['Manny'], 'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)      


if __name__ == '__main__':
    unittest.main(exit=False)