from unittest import TestCase
from unittest.mock import Mock, patch

import requests
from api_access import api


class TetsApi(TestCase):
    def test_api(self):
        with patch.object(requests, "get") as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert api() == 200
