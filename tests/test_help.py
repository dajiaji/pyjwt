import base64
import json
import platform

import pytest

from jwt.help import info
from jwt import __version__

class TestHelp:

    def test_info(self):
        data = info()
        assert isinstance(data, dict)
        assert isinstance(data["platform"], dict)
        assert data["platform"]["system"] == platform.system()
        assert data["platform"]["release"] == platform.release()
        assert isinstance(data["implementation"], dict)
        assert data["implementation"]["name"] == platform.python_implementation()
        assert isinstance(data["implementation"]["name"], str)
        assert isinstance(data["implementation"]["version"], str)
        assert isinstance(data["cryptography"], dict)
        assert isinstance(data["cryptography"]["version"], str)
        assert isinstance(data["pyjwt"], dict)
        assert data["pyjwt"]["version"] == __version__
