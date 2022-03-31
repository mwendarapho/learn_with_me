import unittest
import prime

class Prime(unittest.TestCase):

    def testPrime(self):
        self.assertEqual(prime.is_prime(2),True)
        self.assertEqual(prime.is_prime(1),False)
        self.assertEqual(prime.is_prime(79),True)
        self.assertEqual(prime.is_prime(100),False)
        self.assertEqual(prime.is_prime(101),True)
        self.assertEqual(prime.is_prime(1001),False)
        self.assertEqual(prime.is_prime(121),False)
        self.assertEqual(prime.is_prime(995477231),False)
        self.assertEqual(prime.is_prime(7919),True)
        self.assertEqual(prime.is_prime(-5),False)
        
    def testInteger(self):
        self.assertEqual(prime.is_prime(3.9),False)
        self.assertEqual(prime.is_prime(-11.7),False)
#run in editor        
if __name__ == '__main__':
    unittest.main()