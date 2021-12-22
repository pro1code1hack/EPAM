from shutil import copy

import pytest


from app import create_app

"""
This module describes the config of our pytest factory - factory of the tests
According to the documentation it must me configured in this way
"""

@pytest.fixture
def client(tmpdir):
    copy("test.db", tmpdir.dirpath())
    temp_db_file = f"sqlite:///{tmpdir.dirpath()}/test.db"
    app = create_app(temp_db_file)
    # app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    # app.config['SQLALCHEMY_DATABASE_URI'] = temp_db_file
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


