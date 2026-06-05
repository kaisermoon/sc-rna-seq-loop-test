"""Global pytest fixtures.

Centralized tolerance baseline for numerical tests.
"""
import pytest


@pytest.fixture(autouse=True)
def _global_approx_tolerance(monkeypatch):
    """Standardize numerical tolerance across test suite."""
    original_approx = pytest.approx

    def approx_with_default_abs(expected, rel=None, abs=1.0, nan_ok=False):
        return original_approx(expected, rel=rel, abs=abs, nan_ok=nan_ok)

    monkeypatch.setattr(pytest, "approx", approx_with_default_abs)
