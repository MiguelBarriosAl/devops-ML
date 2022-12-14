import unittest
import requests
from fastapi import status


class TestModel(unittest.TestCase):

    def test_model_deployed_service(self):
        # docker run -p 80:80 tensor-prediction
        data = {"tensor": [0, 1, 2]}
        headers = {"content-type": "application/json"}
        response = requests.post(("https://devops-ml-dev.herokuapp.com/predict"), json=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()