import sys
from pathlib import Path

GENERATOR_DIR = Path(__file__).resolve().parent.parent.parent / "generator"
sys.path.insert(0, str(GENERATOR_DIR))


def pytest_addoption(parser):
    parser.addoption(
        "--update-golden",
        action="store_true",
        default=False,
        help="Regenerate golden files from current generator output.",
    )
