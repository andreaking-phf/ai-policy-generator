#!/usr/bin/env python3
"""
Run the AI Policy Generator Flask application
"""
import os
import sys

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

if __name__ == '__main__':
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))

    # Get debug mode from environment
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    print(f"""
    ================================================
    AI Policy Generator for Health Departments
    ================================================

    Starting server at: http://localhost:{port}

    Pages:
    - Dashboard:    http://localhost:{port}/
    - Prioritize:   http://localhost:{port}/prioritize
    - Generate:     http://localhost:{port}/generate
    - History:      http://localhost:{port}/history

    Press Ctrl+C to stop the server
    ================================================
    """)

    app.run(host='0.0.0.0', port=port, debug=debug)
