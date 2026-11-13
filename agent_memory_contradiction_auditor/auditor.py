"""Memory contradiction auditor for agent belief stores."""
from typing import Dict, List, Optional, Tuple, Any

class Directive:
    def __init__(self, key: str, value: str, modality: str = "MUST"):
        self.key = key.lower().strip()
        self.value = value.lower().strip()
        self.modality = modality.upper().strip()  # MUST, MUST_NOT, ALLOW

class MemoryContradictionAuditor:
    """Identifies mutual exclusion and modal contradictions in agent memory."""

    def __init__(self):
        self.directives: Dict[str, Directive] = {}

    def audit_and_add(self, directive: Directive) -> Tuple[bool, Optional[str]]:
        existing = self.directives.get(directive.key)
        if not existing:
            self.directives[directive.key] = directive
            return True, None

        # Check contradiction: same key, conflicting modality or differing values under MUST
        if existing.modality == "MUST" and directive.modality == "MUST_NOT":
            return False, f"Direct contradiction for '{directive.key}': existing MUST vs new MUST_NOT"

        if existing.modality == "MUST_NOT" and directive.modality == "MUST":
            return False, f"Direct contradiction for '{directive.key}': existing MUST_NOT vs new MUST"

        if existing.modality == "MUST" and directive.modality == "MUST" and existing.value != directive.value:
            return False, f"Value conflict for '{directive.key}': '{existing.value}' vs '{directive.value}'"

        self.directives[directive.key] = directive
        return True, None
