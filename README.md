# TaskSimplifier

This repository now includes a Flask-powered Three.js demo that renders a 3-axis robot arm with inverse kinematics and a pick-and-place state machine.

## Features

- 3-axis robot arm model (`base`, `shoulder`, `elbow`, and `gripper`) in a lit 3D scene.
- Inverse kinematics control of the end-effector target position.
- Eight floor cubes (4 blue / 4 orange) that are moved one-by-one to the opposite side.
- State machine: `idle → moving to pickup → lifting → moving to drop → dropping → idle`.
- HUD-style dark UI with orange accents:
  - Left: three joint angle gauges.
  - Right: end-effector speed graph + command log.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open your browser:
   ```
   http://127.0.0.1:5000/
   ```

## API endpoint

`POST /reply` is still available for the original automated reply demo.
