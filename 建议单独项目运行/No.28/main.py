import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./scripts')

    runner = unittest.TextTestRunner()
    runner.run(suite)