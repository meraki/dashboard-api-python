def pytest_addoption(parser):
    parser.addoption("--apikey", action="store", default="")
    parser.addoption("--o", action="store", default="")
