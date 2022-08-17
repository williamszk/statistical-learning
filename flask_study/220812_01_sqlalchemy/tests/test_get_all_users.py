import pytest
from pathlib import Path  # noqa: E402

@pytest.fixture
def base_path() -> Path:
    """Get the current folder of the test"""
    return Path(__file__).parent


def test_main(base_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(base_path)
    import sqlite3
    connection = sqlite3.connect("../src/db.sqlite")
    cursor = connection.cursor()

    query = """--sql
    SELECT * FROM users;
    """

    for row in cursor.execute(query):
        print(row)

    connection.close()


if __name__ == "__main__":
    test_main()
