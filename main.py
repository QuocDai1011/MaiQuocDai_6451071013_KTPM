"""Chạy toàn bộ test case trong App/tests."""

import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
TESTCASE_DIR = ROOT_DIR / "App" / "tests"


def main():
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(TESTCASE_DIR),
        pattern="test_*.py",
        top_level_dir=str(ROOT_DIR),
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())


if __name__ == "__main__":
    main()
