import json
from pathlib import Path
import sys


REPORT_PATH = Path("reports/report.json")
MIN_PASS_RATE = 0.9  # 90%


def run_quality_gate():
    data = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    total = data["summary"]["total"]
    passed = data["summary"]["passed"]

    pass_rate = passed / total

    print(f"Pass rate: {pass_rate:.2%}")

    if pass_rate < MIN_PASS_RATE:
        print("QUALITY GATE FAILED ❌")
        sys.exit(1)

    print("QUALITY GATE PASSED ✅")


if __name__ == "__main__":
    run_quality_gate()
