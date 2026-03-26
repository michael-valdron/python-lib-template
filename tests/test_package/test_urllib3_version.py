import unittest
import importlib


class TestUrllib3Version(unittest.TestCase):
    """Tests verifying urllib3 is upgraded to v2 as specified in requirements.txt."""

    def test_urllib3_is_installed(self):
        """urllib3 must be importable."""
        import urllib3
        self.assertIsNotNone(urllib3)

    def test_urllib3_exact_version(self):
        """urllib3 must be pinned to exactly 2.6.3 as specified in requirements.txt."""
        import urllib3
        self.assertEqual(urllib3.__version__, "2.6.3")

    def test_urllib3_major_version_is_2(self):
        """urllib3 major version must be 2 (upgraded from 1.x)."""
        import urllib3
        major = int(urllib3.__version__.split(".")[0])
        self.assertEqual(major, 2)

    def test_urllib3_not_v1(self):
        """urllib3 must not be the old v1.x that was replaced by this PR."""
        import urllib3
        major = int(urllib3.__version__.split(".")[0])
        self.assertGreaterEqual(major, 2, "urllib3 must be v2 or later, not v1.x")

    def test_urllib3_version_at_least_2_6_3(self):
        """urllib3 version must be at least 2.6.3 (regression guard)."""
        import urllib3
        parts = [int(x) for x in urllib3.__version__.split(".")]
        required = [2, 6, 3]
        self.assertGreaterEqual(parts, required)

    def test_urllib3_pool_manager_importable(self):
        """PoolManager must be available at the top-level namespace."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "PoolManager"))

    def test_urllib3_pool_manager_instantiable(self):
        """PoolManager must be instantiable without errors."""
        import urllib3
        pm = urllib3.PoolManager()
        self.assertIsNotNone(pm)

    def test_urllib3_http_connection_pool_available(self):
        """HTTPConnectionPool must be present in the urllib3 namespace."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "HTTPConnectionPool"))

    def test_urllib3_https_connection_pool_available(self):
        """HTTPSConnectionPool must be present in the urllib3 namespace."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "HTTPSConnectionPool"))

    def test_urllib3_proxy_manager_available(self):
        """ProxyManager must be present in the urllib3 namespace."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "ProxyManager"))

    def test_urllib3_base_http_response_available(self):
        """BaseHTTPResponse is a v2 addition and must exist."""
        import urllib3
        self.assertTrue(
            hasattr(urllib3, "BaseHTTPResponse"),
            "BaseHTTPResponse was added in urllib3 v2 and must be present",
        )

    def test_urllib3_http_header_dict_available(self):
        """HTTPHeaderDict must be present in the urllib3 namespace."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "HTTPHeaderDict"))

    def test_urllib3_http_header_dict_case_insensitive(self):
        """HTTPHeaderDict must handle headers case-insensitively (v2 behaviour)."""
        import urllib3
        headers = urllib3.HTTPHeaderDict()
        headers["Content-Type"] = "application/json"
        self.assertEqual(headers["content-type"], "application/json")
        self.assertEqual(headers["CONTENT-TYPE"], "application/json")

    def test_urllib3_retry_available(self):
        """Retry must be importable from urllib3."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "Retry"))

    def test_urllib3_retry_configuration(self):
        """Retry object must be configurable with standard parameters."""
        import urllib3
        retry = urllib3.Retry(total=5, backoff_factor=0.5, status_forcelist={500, 503})
        self.assertEqual(retry.total, 5)

    def test_urllib3_timeout_available(self):
        """Timeout must be importable from urllib3."""
        import urllib3
        self.assertTrue(hasattr(urllib3, "Timeout"))

    def test_urllib3_timeout_configuration(self):
        """Timeout must accept connect and read parameters."""
        import urllib3
        timeout = urllib3.Timeout(connect=3.0, read=10.0)
        self.assertEqual(timeout.connect_timeout, 3.0)
        self.assertEqual(timeout.read_timeout, 10.0)

    def test_urllib3_exceptions_module_importable(self):
        """urllib3.exceptions module must be importable."""
        import urllib3.exceptions
        self.assertIsNotNone(urllib3.exceptions)

    def test_urllib3_core_exceptions_present(self):
        """Essential exception classes must exist in urllib3.exceptions."""
        import urllib3.exceptions
        required_exceptions = [
            "MaxRetryError",
            "NewConnectionError",
            "ConnectTimeoutError",
            "ReadTimeoutError",
            "SSLError",
            "ProxyError",
            "PoolError",
            "LocationParseError",
            "InsecureRequestWarning",
        ]
        for name in required_exceptions:
            self.assertTrue(
                hasattr(urllib3.exceptions, name),
                f"urllib3.exceptions.{name} must exist",
            )

    def test_urllib3_parse_url_importable(self):
        """parse_url must be available via urllib3.util."""
        import urllib3.util
        self.assertTrue(hasattr(urllib3.util, "parse_url"))

    def test_urllib3_parse_url_functionality(self):
        """parse_url must correctly decompose a URL."""
        from urllib3.util.url import parse_url
        result = parse_url("https://example.com:8080/path?q=test#frag")
        self.assertEqual(result.scheme, "https")
        self.assertEqual(result.host, "example.com")
        self.assertEqual(result.port, 8080)
        self.assertEqual(result.path, "/path")
        self.assertEqual(result.query, "q=test")

    def test_urllib3_parse_url_handles_http(self):
        """parse_url must handle plain HTTP URLs without raising."""
        from urllib3.util.url import parse_url
        result = parse_url("http://localhost/api")
        self.assertEqual(result.scheme, "http")
        self.assertEqual(result.host, "localhost")

    def test_urllib3_connection_from_url(self):
        """connection_from_url must return an HTTPConnectionPool for http:// URLs."""
        import urllib3
        pool = urllib3.connection_from_url("http://example.com")
        self.assertIsInstance(pool, urllib3.HTTPConnectionPool)

    def test_urllib3_contrib_namespace_absent(self):
        """urllib3.contrib is not a top-level attribute in v2 (removed from v1)."""
        import urllib3
        self.assertFalse(
            hasattr(urllib3, "contrib"),
            "urllib3.contrib top-level attribute was removed in v2",
        )

    def test_urllib3_util_retry_importable(self):
        """urllib3.util.retry.Retry must be importable."""
        from urllib3.util.retry import Retry
        self.assertIsNotNone(Retry)

    def test_urllib3_util_ssl_importable(self):
        """urllib3.util.ssl_ must be importable."""
        import urllib3.util.ssl_ as ssl_util
        self.assertIsNotNone(ssl_util)


if __name__ == "__main__":
    unittest.main()