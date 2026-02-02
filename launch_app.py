#!/usr/bin/env python3
"""
AI Policy Generator - VS Code Launcher
Just click "Run" in VS Code or press F5 to start the application.
"""

import subprocess
import sys
import os

# Change to the app directory
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')
os.chdir(app_dir)

print("=" * 60)
print("  AI Policy Generator - Starting...")
print("=" * 60)

# Install dependencies
print("\n[1/2] Installing dependencies...")
subprocess.run([sys.executable, '-m', 'pip', 'install', '-q',
                'Flask', 'Flask-SQLAlchemy'], check=True)
print("      Dependencies installed!")

# Start the application
print("\n[2/2] Starting Flask server...")
print("\n" + "=" * 60)
print("  Open your browser to: http://localhost:5000")
print("  Press Ctrl+C to stop the server")
print("=" * 60 + "\n")

# Import and run the app
sys.path.insert(0, app_dir)
from app import app
app.run(host='127.0.0.1', port=5000, debug=True)
