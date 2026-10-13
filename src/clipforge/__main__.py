"""Bootstrap entry — `python -m clipforge` on Windows 10/11, Python 3.11+."""
from __future__ import annotations

import sys

from clipforge.bootstrap.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))