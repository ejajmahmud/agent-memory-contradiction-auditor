"""CLI for agent-memory-contradiction-auditor."""
import sys
import argparse
from .auditor import MemoryContradictionAuditor, Directive

def main():
    parser = argparse.ArgumentParser(description="Agent Memory Contradiction Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run memory contradiction audit demo")
    args = parser.parse_args()

    if args.demo:
        auditor = MemoryContradictionAuditor()
        ok1, err1 = auditor.audit_and_add(Directive("db_engine", "sqlite", "MUST"))
        print(f"[+] Directive 1 added: ok={ok1}")
        ok2, err2 = auditor.audit_and_add(Directive("db_engine", "postgres", "MUST"))
        print(f"[!] Directive 2 audited: ok={ok2}, reason='{err2}'")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
