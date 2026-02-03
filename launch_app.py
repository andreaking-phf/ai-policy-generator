#!/usr/bin/env python3
"""
AI Policy Generator - VS Code Launcher
=======================================
HOW TO USE:
  1. Open this file in VS Code
  2. Click the Run button (triangle) in the top right, or press F5
  3. Open your browser to http://localhost:5000
"""

import subprocess
import sys
import os
import webbrowser
import time

# Automatically find the app directory relative to this file
script_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(script_dir, 'app')

# Verify the app directory exists
if not os.path.isdir(app_dir):
    print("ERROR: Cannot find the 'app' folder.")
    print(f"Expected location: {app_dir}")
    print("Make sure launch_app.py is in the same folder as the 'app' directory.")
    input("\nPress Enter to exit...")
    sys.exit(1)

os.chdir(app_dir)

print("=" * 60)
print("  AI Policy Generator for Health Departments")
print("=" * 60)

# Step 1: Install dependencies
print("\n[1/2] Installing dependencies...")
try:
    subprocess.run(
        [sys.executable, '-m', 'pip', 'install', '-q',
         'Flask', 'Flask-SQLAlchemy'],
        check=True
    )
    print("      Done!")
except subprocess.CalledProcessError:
    print("      Warning: pip install had issues, trying anyway...")

# Step 2: Start the app
print("\n[2/2] Starting web server...\n")
print("=" * 60)
print("  App running at:  http://localhost:5000")
print("  Press Ctrl+C to stop the server")
print("=" * 60 + "\n")

# Open browser automatically after a short delay
def open_browser():
    time.sleep(1.5)
    webbrowser.open('http://localhost:5000')

import threading
threading.Thread(target=open_browser, daemon=True).start()

# Import and run
sys.path.insert(0, app_dir)
from app import app
app.run(host='127.0.0.1', port=5000, debug=False)
