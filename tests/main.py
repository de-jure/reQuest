import unittest
import os

from src import jobs, saves


class TestStringMethods(unittest.TestCase):

    def test_savefile_created(self):
        saves.delete_savefile()
        saves.create_savefile()
        self.assertTrue(os.path.exists('savefile.json'))

    def test_work1(self):
        self.assertEqual(jobs.work1(), {'message': 'Earned 10 ED'})
        self.assertEqual(jobs.work1(), {'message': 'You can\'t work that often. Try again later.'})


if __name__ == '__main__':
    unittest.main()
