"""
Vercel Serverless Entrypoint Wrapper
Enables universal compatibility across Vercel Python runtime configurations.
"""

import sys
import os

# Ensure project root is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.server import app
