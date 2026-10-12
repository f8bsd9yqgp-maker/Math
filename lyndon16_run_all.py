#!/usr/bin/env python3
"""Restore and independently verify the length-16 Lyndon superstring certificate.

Run: python3 lyndon16_run_all.py
This uses Python's standard library only; no NumPy, SciPy, or optimizer.
The restoration scripts check SHA-256 hashes of the embedded original files.
The verifier checks all 2,979,076 assignment dual inequalities and the witness.
"""
from pathlib import Path
import runpy

here = Path(__file__).resolve().parent
for filename in ("lyndon16_restore_dual.py", "lyndon16_restore_witness.py", "lyndon16_verify.py"):
    runpy.run_path(str(here / filename), run_name="__main__")
