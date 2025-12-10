# AI Story Builder — Hybrid Story Generation Engine

A modular, extensible story-generation system that combines deterministic template-based logic with optional transformer-based text expansion. The project demonstrates practical software engineering, AI integration, and clean modular design using Python, Flask, and HuggingFace Transformers.

The repository provides two interfaces:
i.Command-Line Interface (CLI)
ii.Web Application (Flask-based UI)

The core engine constructs coherent narratives using a structured plot framework, with optional transformer-based rewriting for creative enhancement.

# Key Features

## Hybrid Story Generation Pipeline
Combines rule-based plot construction with transformer-based narrative enrichment.
## Deterministic and AI-Augmented Modes
Deterministic mode offers consistent, logically structured stories.
AI expansion mode generates expressive, human-like narrative flow.
## Configurable Story Elements
Users specify prototype story inputs including protagonist, supporting characters, conflict, setting, themes, and ending style.
## Seven Complete Ending Styles
Supports: happy, sad, bittersweet, hopeful, tragic, poetic, and heroic.
## Clean Software Architecture
Clear separation of engine logic, user interfaces, and optional AI expansion layers.
## Graceful Fallback Behavior
If a transformer model is unavailable, the engine defaults to deterministic generation without errors.
## Implementation
This project is suitable for demonstrating AI integration, backend logic design, and model-based text generation.

# Project Structure

AI-STORY-BUILDER/
│
├── cli_app/
│   └── story_cli.py          # CLI interface
│
├── story_engine/
│   ├── __init__.py
│   └── engine.py             # Core hybrid story generator
│
├── web_app/
│   ├── app.py                # Flask web server
│   └── templates/
│       └── index.html        # Web interface
│
├── venv/                     # Virtual environment (ignored by Git)
│
├── requirements.txt
├── LICENSE
└── README.md

# Installation

1. Clone the repository
git clone https://github.com/YOUR-USERNAME/AI-Story-Builder.git
cd AI-Story-Builder
2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
3. Install dependencies
pip install -r requirements.txt

If PyTorch installation fails, refer to the official installation guide:
https://pytorch.org/get-started/locally/

# Usage
1. CLI Mode
Deterministic (template-only) story generation:
python -m cli_app.story_cli
Hybrid mode with transformer model expansion:
python -m cli_app.story_cli --expand --model distilgpt2
2. Web Application
Start the Flask application:
python web_app/app.py
Open the web interface in your browser:
http://127.0.0.1:5000/
## The web interface allows users to:
i.Input all story parameters
ii.Choose ending style
iii.Enable AI expansion
iv.Select transformer model (optional)

# Technical Overview

## Deterministic Story Layer
Constructs a narrative using a structured plot progression:
-Opening
-Rising action
-Conflict escalation
-Resolution
Ensures logical continuity and complete endings.

# AI Expansion Layer (Optional)

When enabled, a transformer model:
-Expands narrative detail
-Adds stylistic variation
-Enhances emotional depth
-Preserves original plot and ending constraints
The model layer is optional and automatically disabled if dependencies are missing.

# Requirements

-flask
-transformers
-torch
Torch installation size varies based on system; CPU-only versions are sufficient for this project.

# License

This project is released under the MIT License.
