"""Unit tests for agent-memory-contradiction-auditor."""
import unittest
from agent_memory_contradiction_auditor.auditor import MemoryContradictionAuditor, Directive

class TestContradictionAuditor(unittest.TestCase):
    def setUp(self):
        self.auditor = MemoryContradictionAuditor()

    def test_add_compatible(self):
        ok, err = self.auditor.audit_and_add(Directive("k1", "v1", "MUST"))
        self.assertTrue(ok)
        self.assertIsNone(err)

    def test_modality_conflict(self):
        self.auditor.audit_and_add(Directive("feature_x", "enabled", "MUST"))
        ok, err = self.auditor.audit_and_add(Directive("feature_x", "enabled", "MUST_NOT"))
        self.assertFalse(ok)
        self.assertIn("contradiction", err)

    def test_value_conflict_under_must(self):
        self.auditor.audit_and_add(Directive("auth_provider", "auth0", "MUST"))
        ok, err = self.auditor.audit_and_add(Directive("auth_provider", "firebase", "MUST"))
        self.assertFalse(ok)
        self.assertIn("Value conflict", err)

if __name__ == "__main__":
    unittest.main()
