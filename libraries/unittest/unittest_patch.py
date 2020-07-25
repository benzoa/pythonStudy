from unittest import TestCase, main
from unittest.mock import patch


def hello():
    return "Hello!"


class TestMe(TestCase):
    @patch("__main__.hello", return_value="Mock!")
    def test_hello(self, mock_hello):
        self.assertEqual(hello(), "Mock!")
        self.assertIs(hello, mock_hello)
        mock_hello.assert_called_once_with()


if __name__ == "__main__":
    main()
