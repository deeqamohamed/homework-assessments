"""Q4: Palindrome testing """
from unittest import mock
from unittest import TestCase, main
from Assessment import checkPalindrome


class Palindrome(TestCase):

    def test_palindrome(self):
        @mock.patch('builtins.input', return_value='deeqa')
        def checkPalindrome(self, mock_input):
            self.assertEqual(checkPalindrome(), True)


if __name__ == '__main__':
    main()