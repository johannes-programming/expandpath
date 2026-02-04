import unittest
from typing import *
from unittest.mock import patch

from click.testing import CliRunner

import expandpath.core

__all__ = ["TestMainCLI"]


class TestMainCLI(unittest.TestCase):
    def setUp(self: Self) -> None:
        self.runner = CliRunner()

    @patch("expandpath.core.expandpath", return_value="/expanded/path")
    def test_main_expands_and_prints_path(
        self: Self,
        mock_expandpath: Any,
    ) -> None:
        result: Any
        result = self.runner.invoke(expandpath.core.main, ["~/test"])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), "/expanded/path")
        mock_expandpath.assert_called_once_with("~/test")

    def test_main_help_option(self: Self) -> None:
        result: Any
        result = self.runner.invoke(expandpath.core.main, ["-h"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("This command expands the given path.", result.output)

    def test_main_version_option(self: Self) -> None:
        result: Any
        result = self.runner.invoke(expandpath.core.main, ["-V"])
        # version is None, but Click still prints something like "main, version"
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(result.output.strip())  # just ensure something is printed


if __name__ == "__main__":
    unittest.main()
