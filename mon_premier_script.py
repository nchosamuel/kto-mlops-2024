import unittest

"""
Count names with more than seven letters
"""
def count_long_names(names_list: list[str]):
   
    long_names_count = 0
    for name in names_list:
        if len(name) > 7:
            long_names_count += 1
            print("Name longer than 7 characters: " + name)
        else:
            print("Name shorter or equal to 7 characters: " + name)
    return long_names_count

class TestCountLongNamesMethod(unittest.TestCase):
    def test_count_long_names(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_long_names(names_list=names_list)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
