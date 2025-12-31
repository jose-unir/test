import http.client
import unittest
from urllib.request import build_opener, HTTPHandler, HTTPSHandler
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

_ALLOWED_SCHEMES = {"http", "https"}
_opener = build_opener(HTTPHandler(), HTTPSHandler())

def _validated_url(url: str) -> str:
    """Validate URL scheme and structure to avoid file:/ or custom schemes."""
    parsed = urlparse(url)
    if parsed.scheme not in _ALLOWED_SCHEMES:
        raise ValueError(f"Unsupported URL scheme: {parsed.scheme!r}")
    if not parsed.netloc:
        # For http(s), require a host (e.g., localhost:5000)
        raise ValueError("URL must include a host (netloc)")
    return url


def _safe_urlopen(url: str, timeout: float = DEFAULT_TIMEOUT):
    """Open a URL safely after validating allowed schemes."""
    safe = _validated_url(url)
    return _opener.open(safe, timeout=timeout)


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        with _safe_urlopen(url) as response:
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )
            self.assertEqual(response.read().decode(), "3", "ERROR ADD")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/6/7"
        with _safe_urlopen(url) as response:
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )
            self.assertEqual(response.read().decode(), "42", "ERROR MULTIPLY")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        with _safe_urlopen(url) as response:
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )
            self.assertEqual(response.read().decode(), "5", "ERROR DIVIDE")
