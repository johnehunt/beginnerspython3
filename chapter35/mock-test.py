import external_module

from unittest.mock import *
from unittest import TestCase
from unittest import main
import json


def some_func():
    response = external_module.api_call()
    return response


class test_api(TestCase):

    @patch('external_module.api_call')
    def test_some_func(self, mock_api_call):
        mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'key':'value'}))
        result = some_func()
        print(result.response)
        self.assertEqual(result.status_code, 200, "returned status code is not 200")
        self.assertEquals(result.response, '{"key": "value"}', "response JSON incorrect")


if __name__ == '__main__':
    main()