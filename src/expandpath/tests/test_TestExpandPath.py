import unittest
from typing import *
from unittest.mock import patch

import expandpath.core  # adjust to your actual module name

__all__ = ["TestExpandPath"]


class TestExpandPath(unittest.TestCase):
    @patch("expandpath.core.os.path.expandvars")
    @patch("expandpath.core.os.path.expanduser")
    def test_expandpath_calls_expanduser_then_expandvars(
        self: Self,
        mock_expanduser: Any,
        mock_expandvars: Any,
    ) -> None:
        result: Any
        mock_expanduser.return_value = "/home/user/$FOO"
        mock_expandvars.return_value = "/home/user/bar"
        result = expandpath.core.expandpath("~/file")
        mock_expanduser.assert_called_once_with("~/file")
        mock_expandvars.assert_called_once_with("/home/user/$FOO")
        self.assertEqual(result, "/home/user/bar")

    def test_expandpath_no_special_chars_returns_same_string(self: Self) -> None:
        # This relies only on os.path behavior, but for a simple string
        # without ~ or env vars it should round-trip unchanged.
        result: Any
        value: str
        value = "/tmp/some/file.txt"
        result = expandpath.core.expandpath(value)
        self.assertEqual(result, value)


if __name__ == "__main__":
    unittest.main()
