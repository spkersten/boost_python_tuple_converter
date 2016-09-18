from test_tuple_converter import test_tuple_int, test_tuple_int_string
import unittest


class TupleConverterTest(unittest.TestCase):
    def test_singlet_with_matching_types(self):
        assert test_tuple_int((42, )) == (42,)

    def test_doublet_with_matching_types(self):
        assert test_tuple_int_string((42, "Heart of Gold")) == (42, "Heart of Gold")

    def test_size_mismatch(self):
        with self.assertRaises(Exception):
            test_tuple_int((42, 0))
            
    def test_type_mismatch(self):
        with self.assertRaises(Exception):
            test_tuple_int_string((42, 0))


if __name__ == '__main__':
    unittest.main()
