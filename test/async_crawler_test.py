import unittest
from crawlers import AsyncCrawler


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.crawler = AsyncCrawler()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
