import unittest
import unittest.mock
import control

class TestControl(unittest.TestCase):

    mock_player_create_request_success = {"name": "Gandalf the Grey"}
    mock_player_create_request_fail = {"name": "Saruman of Many Colours"}

    def test_create_player(self):
        control.player_creation_validity = unittest.mock.Mock(return_value=True)
        msg, status = control.create_player(self.mock_player_create_request_success)
        self.assertEqual(status, 201)

        control.player_creation_validity = unittest.mock.Mock(return_value=False)
        msg, status = control.create_player(self.mock_player_create_request_fail)
        self.assertEqual(status, 400)