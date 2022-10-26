import requests
import unittest
from starlette import status


class TestModel(unittest.TestCase):

    def test_get_status_code_equals_200(self):
        # docker run -p 80:80 tensor-prediction
        response = requests.get("http://localhost:80")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
