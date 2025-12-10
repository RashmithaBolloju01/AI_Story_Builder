# AI Story Builder

AI Story Builder is a modular hybrid story-generation system that produces coherent narrative structures based on user input, with optional enhancement through transformer-based language models. Designed with clarity, extensibility, and practical AI integration in mind, it demonstrates how deterministic logic and machine-learning models can be combined in a single workflow.

# Project Overview

This project provides a complete story-generation pipeline implemented in Python.
It includes:
A deterministic template-based story engine
Optional transformer model expansion (e.g., DistilGPT-2) for narrative enrichment
A command-line interface for structured input
A lightweight Flask web interface for interactive story creation
The system is structured for clear maintainability and is suitable for academic demos, portfolio showcases, and integration into larger creative-writing or content-generation platforms.

# Features

User-defined story components (protagonist, characters, conflict, setting, themes)
Seven complete ending styles (happy, sad, bittersweet, hopeful, tragic, poetic, heroic)
Deterministic story generation using structured logic
Optional AI rewriting using HuggingFace Transformers
Flask-based web interface for interactive usage
Robust CLI interface for local or automated use
Graceful fallback when model expansion is not available
Fully modular engine suitable for future upgrades

# Technologies Used

| Category     | Tools and Libraries               |
| ------------ | --------------------------------- |
| Language     | Python 3.10+                      |
| Framework    | Flask                             |
| AI/ML        | HuggingFace Transformers, PyTorch |
| Architecture | Modular engine + CLI + Web UI     |
| Utilities    | Textwrap, argparse                |


# Project Structure

AI-STORY-BUILDER/
├── story_engine/           # Core narrative engine
│   ├── __init__.py
│   └── engine.py
│
├── cli_app/                # Command-line interface
│   └── story_cli.py
│
├── web_app/                # Web application (Flask)
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── venv/                   # Virtual environment (excluded from Git)
├── requirements.txt
├── LICENSE
└── README.md


# How to Run

## Clone the repository
git clone https://github.com/YOUR-USERNAME/AI-Story-Builder.git
cd AI-Story-Builder
## Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
## Install dependencies
pip install -r requirements.txt
## Run the CLI application
Template-only mode:
python -m cli_app.story_cli
With AI expansion:
python -m cli_app.story_cli --expand --model distilgpt2
## Run the Web Application
python web_app/app.py
## The application will be available at:
http://127.0.0.1:5000/

# Sample Use Case

A user provides the following inputs:
Protagonist: "Elian"
Supporting character: "Mira"
Antagonist: "Varek"
Setting: "an abandoned research facility"
Conflict: "a discovery that challenges their understanding of reality"
Object: "a fragmented data core"
Theme: "identity"
Ending: "bittersweet"
The system generates a complete narrative with structured progression.
If AI expansion is enabled, the transformer model refines the text to produce a more natural, expressive version while preserving plot integrity.

# Future Enhancements

Multi-chapter story generation
Genre-specific story frameworks
Detailed character personality modeling
Advanced transformer tuning or fine-tuning
API layer for integration with external applications
Cloud deployment options (Render, Railway, HuggingFace Spaces)

# License

This project is licensed under the MIT License.
