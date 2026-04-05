"""
LILIETH Kernel — Biometric Root Authentication (The Cyan-on-Black Lock)
========================================================================
Provides a two-factor access gate that must be cleared before any privileged
kernel operation is permitted:

  1. **Pulse Signature** — a cryptographic token issued by the Architect.
  2. **Biometric Token** — a hardware-derived identifier unique to the node.

The module deliberately avoids storing raw credentials in memory; only
salted hashes are compared.

Usage
-----
::

    from biometrics.root_auth import authenticate, RootSession

    # Quick gate check
    if authenticate(pulse_signature="ARCHITECT_ALPHA", biometric_token="<token>"):
        # proceed with privileged operations
        ...

    # Context-manager variant (raises PermissionError on failure)
    with RootSession(pulse_signature="ARCHITECT_ALPHA", biometric_token="<token>") as session:
        print(session.node_id)
"""

from __future__ import annotations

import hashlib
import os
from typing import Optional


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------

_SOVEREIGN_SIGNATURE = "ARCHITECT_ALPHA"

# Salt is fixed per-deployment; in production this would be loaded from a
# hardware security module (HSM) or environment variable.
_SALT = os.environ.get("LILIETH_AUTH_SALT", "LILIETH_SOVEREIGN_SALT_v1")


def _hash_token(token: str) -> str:
    """Return a hex digest of *token* mixed with the deployment salt."""
    payload = f"{_SALT}:{token}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# Pre-computed hash of the default biometric anchor token (used in dev/test).
# Override via the ``LILIETH_BIO_HASH`` environment variable in production.
_DEFAULT_BIO_HASH = _hash_token("LILIETH_BIO_ROOT_v1")
_BIO_HASH = os.environ.get("LILIETH_BIO_HASH", _DEFAULT_BIO_HASH)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def authenticate(
    pulse_signature: str,
    biometric_token: str,
    *,
    node_id: Optional[str] = None,
) -> bool:
    """Authenticate a root access attempt.

    Parameters
    ----------
    pulse_signature:
        The Architect's pulse signature string.  Must equal the sovereign
        signature constant for authentication to succeed.
    biometric_token:
        A hardware-derived biometric identifier supplied by the node.  Its
        SHA-256 hash (salted) is compared against the registered anchor hash.
    node_id:
        Optional human-readable node identifier used in log output.

    Returns
    -------
    bool
        ``True`` if both factors are valid; ``False`` otherwise.
    """
    label = node_id or "UNKNOWN"

    sig_ok = pulse_signature == _SOVEREIGN_SIGNATURE
    bio_ok = _hash_token(biometric_token) == _BIO_HASH

    if sig_ok and bio_ok:
        print(f"[ROOT_AUTH] Node {label!r}: ACCESS GRANTED — Sovereignty confirmed.")
        return True

    reasons = []
    if not sig_ok:
        reasons.append("invalid pulse signature")
    if not bio_ok:
        reasons.append("biometric mismatch")
    print(f"[ROOT_AUTH] Node {label!r}: ACCESS DENIED — {'; '.join(reasons)}.")
    return False


class RootSession:
    """Context manager that enforces biometric root authentication.

    Raises :class:`PermissionError` if authentication fails on entry.

    Parameters
    ----------
    pulse_signature:
        Architect's pulse signature.
    biometric_token:
        Hardware biometric token.
    node_id:
        Optional node label for logging.
    """

    def __init__(
        self,
        pulse_signature: str,
        biometric_token: str,
        node_id: Optional[str] = None,
    ) -> None:
        self._pulse = pulse_signature
        self._bio = biometric_token
        self.node_id = node_id or "session_node"

    def __enter__(self) -> "RootSession":
        if not authenticate(self._pulse, self._bio, node_id=self.node_id):
            raise PermissionError(
                f"Root authentication failed for node {self.node_id!r}. "
                "Sovereign access denied."
            )
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        print(f"[ROOT_AUTH] Node {self.node_id!r}: session closed.")
