# tests/test_main.py

from src.main import load_file

def test_load_file():
    content = load_file("example.txt")
    assert len(content) > 0