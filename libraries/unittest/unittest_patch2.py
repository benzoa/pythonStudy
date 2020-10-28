from unittest import TestCase
from unittest.mock import patch

import user_manager


class TestUserManger(TestCase):
    @patch("requests.post")
    def test_create_user(self, mock_post):
        response = mock_post.return_value
        response.status_code = 201
        response.json.return_value = {"id": 99}

        user = user_manager.create_user(
            {"name": "Test User", "email": "user@test.com", }
        )

        self.assertEqual(user["id"], 99)
        mock_post.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users",
            data={"name": "Test User", "email": "user@test.com", },
        )
