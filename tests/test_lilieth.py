"""
LILIETH Kernel — Test Suite
============================
Tests for core algorithms, the extensible parser, the compiler,
biometric root auth, and the protocol files.
"""

from __future__ import annotations

import os
import sys

import pytest

# Ensure the repo root is on sys.path so that `core` and `biometrics` resolve.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.algorithms import calculate_sue_score, harvest_kinetic_energy, oush_handshake, calculate_psi_law
from core.interpreter import (
    ASTNode,
    AnimusInterpreter,
    EterniusInterpreter,
    KongInterpreter,
    LiliethParser,
    ParseError,
    VajraInterpreter,
)
from core.compiler import LiliethCompiler
from biometrics.root_auth import RootSession, authenticate


# ===========================================================================
# 1.  Algorithms
# ===========================================================================

class TestCalculateSueScore:
    def test_virtues_outweigh_sins_returns_above_one(self):
        virtues = {k: 0.9 for k in ("a", "b", "c", "d", "e", "f", "g")}
        sins = {k: 0.1 for k in ("a", "b", "c", "d", "e", "f", "g")}
        score = calculate_sue_score(virtues, sins)
        assert score > 1.0

    def test_equal_virtues_and_sins_returns_near_one(self):
        virtues = {k: 0.5 for k in range(7)}
        sins = {k: 0.5 for k in range(7)}
        score = calculate_sue_score(virtues, sins)
        # 3.5 / (3.5 + 0.0004) ≈ 0.9999  < 1.0  but very close
        assert 0.9 < score < 1.1

    def test_all_zeros_sins_does_not_raise(self):
        virtues = {k: 1.0 for k in range(7)}
        sins = {k: 0.0 for k in range(7)}
        score = calculate_sue_score(virtues, sins)
        assert score > 0  # guarded by 0.0004

    def test_all_max_sins_blocks_action(self):
        virtues = {k: 0.0 for k in range(7)}
        sins = {k: 1.0 for k in range(7)}
        score = calculate_sue_score(virtues, sins)
        assert score < 1.0


class TestHarvestKineticEnergy:
    def test_positive_values_return_joules(self):
        joules = harvest_kinetic_energy(100.0, 30.0)
        assert joules > 0

    def test_formula_correctness(self):
        # Phi = (100 * 30 * 0.98) - 0.02 = 2939.98
        assert harvest_kinetic_energy(100.0, 30.0) == pytest.approx(2939.98)

    def test_zero_traffic_returns_zero(self):
        assert harvest_kinetic_energy(0.0, 50.0) == 0.0

    def test_clamp_prevents_negative(self):
        assert harvest_kinetic_energy(0.0, 0.0) == 0.0


class TestOushHandshake:
    def test_valid_signature_returns_true(self, capsys):
        assert oush_handshake("NODE_1", "ARCHITECT_ALPHA") is True
        captured = capsys.readouterr()
        assert "SOVEREIGNTY LOCKED" in captured.out

    def test_invalid_signature_returns_false(self, capsys):
        assert oush_handshake("NODE_2", "WRONG") is False
        captured = capsys.readouterr()
        assert "FAILED" in captured.out


class TestCalculatePsiLaw:
    def setup_method(self):
        self._pillar_scores = {f"p{i}": 0.9 for i in range(1, 16)}   # 15 pillars at 0.9
        self._statute_scores = {f"s{i}": 0.05 for i in range(1, 6)}  # 5 statutes at 0.05

    def test_sovereign_shield_active_below_one(self):
        # Strong pillars + high 4D depth → Ψ_law < 1.0 (shield active)
        score = calculate_psi_law(self._pillar_scores, 4.0, 0.1, self._statute_scores)
        assert score < 1.0

    def test_static_court_dominates_above_one(self):
        # Weak pillars + low depth + high resistance → Ψ_law ≥ 1.0
        weak_pillars = {f"p{i}": 0.01 for i in range(1, 16)}
        heavy_statutes = {f"s{i}": 0.9 for i in range(1, 11)}
        score = calculate_psi_law(weak_pillars, 1.0, 1.0, heavy_statutes)
        assert score >= 1.0

    def test_zero_pillar_scores_does_not_raise(self):
        # Division-by-zero guard (SOVEREIGN_GUARD = 0.0004) must prevent crash
        score = calculate_psi_law({}, 0.0, 0.5, {"s1": 0.5})
        assert score > 0

    def test_formula_correctness(self):
        # Ψ = (0.1 + 0.25) / (13.5 * 2.0 + 0.0004)  ≈ 0.012963
        pillar_scores = {f"p{i}": 0.9 for i in range(1, 16)}  # sum = 13.5
        statute_scores = {f"s{i}": 0.05 for i in range(1, 6)}  # sum = 0.25
        expected = (0.1 + 0.25) / (13.5 * 2.0 + 0.0004)
        assert calculate_psi_law(pillar_scores, 2.0, 0.1, statute_scores) == pytest.approx(expected)


# ===========================================================================
# 2.  Parser
# ===========================================================================

class TestLiliethParser:
    def setup_method(self):
        self.parser = LiliethParser()

    def test_parse_valid_vajra_source(self):
        src = "ignite10000 spark\ntake50000\n"
        nodes = self.parser.parse_source(src, ".v")
        assert len(nodes) == 2
        assert nodes[0].action == "ignite"
        assert nodes[0].scale == "10000"
        assert nodes[1].action == "take"

    def test_parse_skips_comments_and_blanks(self):
        src = "# comment\n\nignite10000\n"
        nodes = self.parser.parse_source(src, ".v")
        assert len(nodes) == 1

    def test_parse_invalid_line_raises_error(self):
        with pytest.raises(ParseError):
            self.parser.parse_source("!!!bad", ".v")

    def test_strict_format_enforced_on_v(self):
        """Short tokens (< 3 letters or < 5 digits) must raise in strict .v files."""
        with pytest.raises(ParseError, match="abc12345 format"):
            self.parser.parse_source("ignite100 short_scale\n", ".v")

    def test_strict_format_enforced_on_ai(self):
        """Short tokens must raise in strict .ai files."""
        with pytest.raises(ParseError, match="abc12345 format"):
            self.parser.parse_source("give100 short\n", ".ai")

    def test_parse_and_execute_vajra(self):
        src = "ignite10000 spark\n"
        nodes = self.parser.parse_source(src, ".v")
        results = self.parser.execute(nodes)
        assert results[0]["vajra_induction"].startswith("logic_pulse:")

    def test_parse_and_execute_animus_give_permitted(self):
        src = "give10001 resource\n"
        nodes = self.parser.parse_source(src, ".ai")
        results = self.parser.execute(nodes)
        assert results[0]["animus_status"] == "GIVE_PERMITTED"
        assert results[0]["sue_score"] > 1.0

    def test_parse_and_execute_animus_give_blocked(self):
        animus = AnimusInterpreter()
        virtues = {k: 0.0 for k in ("a", "b", "c", "d", "e", "f", "g")}
        sins = {k: 1.0 for k in ("a", "b", "c", "d", "e", "f", "g")}
        animus.set_ethical_profile(virtues, sins)
        # Register overridden interpreter
        parser = LiliethParser()
        parser.register_interpreter(animus)
        nodes = parser.parse_source("give10001 resource\n", ".ai")
        results = parser.execute(nodes)
        assert results[0]["animus_status"] == "GIVE_BLOCKED"
        assert results[0]["sue_score"] <= 1.0

    def test_kong_take_triggers_kinetic_harvest(self):
        src = "take100 A56\n"
        nodes = self.parser.parse_source(src, ".kg")
        results = self.parser.execute(nodes)
        assert "sovereign_joules" in results[0]

    def test_eternius_lock_triggers_oush(self):
        src = "lock15000 audit_node\n"
        nodes = self.parser.parse_source(src, ".4d")
        results = self.parser.execute(nodes)
        assert results[0]["oush_locked"] is True

    def test_unknown_extension_raises(self):
        nodes = self.parser.parse_source("ignite100\n", ".xyz")
        with pytest.raises(ParseError):
            self.parser.execute(nodes, ".xyz")

    def test_register_custom_interpreter(self):
        from core.interpreter import BaseInterpreter
        class CustomInterp(BaseInterpreter):
            extension = ".custom"
            def execute_node(self, node):
                return {"custom": True}

        self.parser.register_interpreter(CustomInterp())
        nodes = self.parser.parse_source("do100\n", ".custom")
        results = self.parser.execute(nodes)
        assert results[0]["custom"] is True

    def test_parse_protocol_files(self):
        base = os.path.join(os.path.dirname(__file__), "..", "protocols")
        for fname in (
            "init_mesh.v",
            "stretford_audit.4d",
            "lilieth_core.ai",
            "me_lawworx.ai",
            "matrix_21x4d.4d",
        ):
            nodes = self.parser.parse_file(os.path.join(base, fname))
            assert len(nodes) > 0

    def test_vajra_take_hook_fires_kong_listener(self, capsys):
        """Verify the cross-module hook: Vajra 'take' triggers KONG harvester."""
        src = "take50000 sky_ionic\n"
        nodes = self.parser.parse_source(src, ".v")
        self.parser.execute(nodes)
        out = capsys.readouterr().out
        assert "KONG" in out


# ===========================================================================
# 3.  Compiler
# ===========================================================================

class TestLiliethCompiler:
    def setup_method(self):
        self.compiler = LiliethCompiler()

    def _make_nodes(self, src: str, ext: str) -> list:
        return LiliethParser().parse_source(src, ext)

    def test_compile_vajra(self):
        nodes = self._make_nodes("ignite10000 spark\ntake50000\n", ".v")
        bc = self.compiler.compile_nodes(nodes, "test_node")
        assert bc.oush_sealed is True
        assert bc.source_ext == ".v"
        assert len(bc.instructions) == 2
        assert bc.instructions[0].opcode == "VAJRA_IGNITE"

    def test_compile_ai(self):
        nodes = self._make_nodes("give10001 resources\n", ".ai")
        bc = self.compiler.compile_nodes(nodes, "ai_node")
        assert bc.instructions[0].opcode == "ANIMUS_GIVE"

    def test_empty_nodes_raises(self):
        with pytest.raises(ParseError):
            self.compiler.compile_nodes([])

    def test_noop_optimisation(self):
        # Use .kg (non-strict extension) so short tokens are valid
        nodes = self._make_nodes("noop00\nnoop00\nnoop00\n", ".kg")
        bc = self.compiler.compile_nodes(nodes)
        # Three consecutive noops should collapse to one
        assert len(bc.instructions) == 1

    def test_compile_file_protocols(self, tmp_path):
        """Compile a real protocol file end-to-end."""
        base = os.path.join(os.path.dirname(__file__), "..", "protocols")
        bc = self.compiler.compile_file(os.path.join(base, "lilieth_core.ai"))
        assert bc.oush_sealed is True


# ===========================================================================
# 4.  Biometric Root Auth
# ===========================================================================

class TestRootAuth:
    _VALID_BIO = "LILIETH_BIO_ROOT_v1"

    def test_valid_credentials_grant_access(self, capsys):
        result = authenticate("ARCHITECT_ALPHA", self._VALID_BIO, node_id="test")
        assert result is True
        assert "GRANTED" in capsys.readouterr().out

    def test_invalid_signature_denies(self, capsys):
        result = authenticate("WRONG_SIG", self._VALID_BIO, node_id="test")
        assert result is False

    def test_invalid_bio_token_denies(self, capsys):
        result = authenticate("ARCHITECT_ALPHA", "WRONG_TOKEN", node_id="test")
        assert result is False

    def test_root_session_context_manager_success(self):
        with RootSession("ARCHITECT_ALPHA", self._VALID_BIO, node_id="ctx_test") as s:
            assert s.node_id == "ctx_test"

    def test_root_session_raises_on_failure(self):
        with pytest.raises(PermissionError):
            with RootSession("BAD_SIG", "BAD_TOKEN"):
                pass
