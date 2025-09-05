# TaskSimplifier

This repository provides a minimal Flask API for demonstration.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Send a POST request with JSON payload:
   ```json
   {"from": "alice@example.com", "subject": "Hello", "body": "Hi there"}
   ```
   to `/reply` to receive a fixed automated response.
