# TaskSimplifier

This repository provides a minimal Flask API for demonstrating a "one-shot" task
automation flow.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Send a POST request to `/one-shot-plan` with a JSON payload such as:
   ```json
   {
     "scenario": "Need help with UCLA post-arrival orientation",
     "preferred_name": "Alex",
     "term": "Fall 2024"
   }
   ```
   The API responds with a single confirmation sheet that summarizes assumptions,
   required inputs, proposed automations, and reference links for the UCLA
   post-arrival orientation flow.

4. Provide any other scenario description to receive a placeholder response that
   explains what extra detail the agent still needs before it can build a
   confirmation sheet.
