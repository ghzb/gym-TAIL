import unittest
import gym_TAIL
import gym


class MyTestCase(unittest.TestCase):
    def test_import(self):
        try:
            gym.make('TAIL-v0')
            self.assertTrue(True)
        except:
            self.fail("May have to run `pip install -e .`")



if __name__ == '__main__':
    unittest.main()
