# InteractFlow

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/interactflow.svg)](https://badge.fury.io/py/interactflow)
[![Upload Python Package](https://github.com/yashChouriya/interactflow/actions/workflows/python-publish.yml/badge.svg)](https://github.com/yashChouriya/interactflow/actions/workflows/python-publish.yml)

InteractFlow is a powerful Python tool designed to record and replay user interactions with high precision. Perfect for creating automated workflows, testing scenarios, or demonstrating user interfaces, it captures every detail of user interaction including mouse movements, clicks, keyboard inputs, and scroll actions.

## Features

- 🎥 **High-Precision Recording**: Captures mouse movements, clicks, keyboard inputs, and scroll actions
- ⏯️ **Flexible Playback**: Replay recorded actions with adjustable speed
- 🎮 **Multiple Recording Management**: Save and organize multiple recordings
- ⚡ **Performance Optimized**: Smart filtering of redundant mouse movements
- 🛡️ **Graceful Handling**: Clean shutdown and save functionality

## Quick Start

### Installation

```bash
pip install interactflow
```

### Alternative: Install from Source

1. Clone the repository:
```bash
git clone git@github.com:yashChouriya/interactflow.git
cd interactflow
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

## Basic Usage

### Recording User Actions

Start recording your actions:
```bash
interactflow record
```
Press `Ctrl+C` to stop recording. The recording will be automatically saved in the `recordings` directory.

### Playing Back Recordings

Play a recorded session:
```bash
interactflow play recordings/your_recording.json
```

Adjust playback speed:
```bash
interactflow play recordings/your_recording.json --speed 2.0  # Play at 2x speed
```

### Listing Available Recordings

View all recordings:
```bash
interactflow list
```

## Advanced Usage

### Recording Module

```python
from interactflow.src.recorder import ActivityRecorder

# Initialize recorder
recorder = ActivityRecorder()

# Start recording
recorder.start_recording()

# Stop recording
recorder.stop_recording()

# Save recording
recorder.save_recording('my_recording.json')
```

### Playback Module

```python
from interactflow.src.player import ActivityPlayer

# Initialize player
player = ActivityPlayer()

# Load and play recording
player.load_recording('my_recording.json')
player.play(speed_multiplier=1.5)  # Play at 1.5x speed
```

## Technical Details

### Dependencies

- Python 3.6+
- pynput >= 1.7.6
- python-xlib >= 0.33

### Project Structure

```
interactflow/
├── src/
│   ├── __init__.py
│   ├── main.py        # CLI interface
│   ├── recorder.py    # Recording functionality
│   └── player.py      # Playback functionality
├── recordings/        # Stored recordings directory
├── .github/          # GitHub configuration
│   └── workflows/    # GitHub Actions
├── requirements.txt  # Project dependencies
├── setup.py         # Package configuration
├── LICENSE          # MIT License
├── CONTRIBUTING.md  # Contribution guidelines
└── README.md        # This file
```

### Recording Format

Recordings are stored in JSON format with the following structure:

```json
{
  "version": "1.0",
  "timestamp": "2024-10-31T12:00:00",
  "events": [
    {
      "type": "mouse_move",
      "timestamp": 1.234,
      "x": 100,
      "y": 200
    }
    // ... more events
  ]
}
```

### Platform Support

- Linux (Full support)
- Windows (Full support)
- macOS (Basic support)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:

- Report bugs
- Suggest enhancements
- Submit pull requests
- Set up development environment

## Support

For support, questions, or feature requests:
1. Check the [issues](https://github.com/yashChouriya/interactflow/issues) page
2. Create a new issue if needed
3. Join our discussions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the `pynput` library for providing robust input device monitoring
- Inspired by the need for reliable UI automation tools

---

Made with ❤️ 
