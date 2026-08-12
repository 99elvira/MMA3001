# Sphero Monash Student

Monash University Student Project — Controlling and programming Sphero robots with Python.

## Overview

This repository contains the codebase for the Monash University Sphero robotics student project. It builds upon the [Sphero SDK](https://github.com/sphero-inc/sphero-sdk-raspberrypi-python) to control Sphero RVR robots and collect sensor data.

## Project Structure

```
sphero-monash-student/
├── src/
│   └── sphero_monash_student/   # Main Python package
│       ├── __init__.py
│       ├── robot.py             # Robot control module
│       ├── sensors.py           # Sensor data collection
│       └── utils.py             # Utility functions
├── data/                        # Data collected from experiments
├── examples/                    # Example scripts
├── tests/                       # Unit and integration tests
├── docs/                        # Documentation
├── tools/                       # Helper tools and scripts
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
├── LICENSE                      # License information
└── README.md                    # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- Sphero RVR robot
- Raspberry Pi (optional, for onboard deployment)

### Installation

```bash
pip install -r requirements.txt
pip install -e .
```

### Quick Start

```python
from sphero_monash_student import Robot

robot = Robot()
robot.connect()
robot.drive(0, 50)  # Drive forward at 50% speed
robot.disconnect()
```

## 🤖 AI Acknowledgment

This project makes use of generative AI tools in accordance with
[Monash University's guidelines on acknowledging the use of AI](https://www.monash.edu/student-academic-success/learning-with-ai/academic-integrity-and-ai/acknowledging-the-use-of-ai).

| Tool / Model | Purpose | Extent |
|---|---|---|
| Claude (Anthropic) | Project scaffolding, code structure, docstrings, tests, README formatting | Generated initial project layout, test cases, and documentation — all output critically reviewed and adapted by the author |
| GitHub Copilot | Inline code completions and suggestions | Assisted with boilerplate and repetitive patterns during development |
| Google Gemini | Notebook formatting and example generation | Used to format sections of workshop notebooks and generate initial code examples based on author-provided prompts |

All AI-generated content has been reviewed and validated by the author(s).
Final decisions on code inclusion, structure, and correctness remain the
responsibility of the human developer(s).

*This statement will be updated as the project evolves to reflect ongoing AI use.*

---

## License

MIT License — see [LICENSE](LICENSE) for details.
