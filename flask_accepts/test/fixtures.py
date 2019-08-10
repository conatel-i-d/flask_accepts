from flask import Flask, jsonify
import pytest

from flask_accepts.test.wrapper import Wrapper # noqa

class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, Wrapper):
            return rv.to_response()
        return Flask.make_response(self, rv)

def create_app(env=None):
    app = ApiFlask(__name__)
    @app.route('/health')
    def health():
        return jsonify('healthy')
    return app

@pytest.fixture
def app():
    return create_app('test')


@pytest.fixture
def client(app):
    return app.test_client()
