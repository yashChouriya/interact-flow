# InteractFlow

InteractFlow is a powerful Python-based tool that allows you to record and replay user interactions with high precision. It captures mouse movements, clicks, keyboard inputs, and scroll actions, making it perfect for creating automated workflows, testing scenarios, or demonstrating user interfaces.

## Features

- 🎥 **High-Precision Recording**: Captures mouse movements, clicks, keyboard inputs, and scroll actions
- ⏯️ **Flexible Playback**: Replay recorded actions with adjustable speed
- 🎮 **Multiple Recording Management**: Save and organize multiple recordings
- ⚡ **Performance Optimized**: Smart filtering of redundant mouse movements
- 🛡️ **Graceful Handling**: Clean shutdown and save functionality

## Installation

1. Clone the repository:

```bash
git clone git@github.com:yashChouriya/interact-flow.git
cd interact-flow
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Recording User Actions

To start recording your actions:

```bash
python main.py record
```

Press `Ctrl+C` to stop recording. The recording will be automatically saved in the `recordings` directory.

### Playing Back Recordings

To play a recorded session:

```bash
python main.py play recordings/your_recording.json
```

You can adjust playback speed using the `--speed` parameter:

```bash
python main.py play recordings/your_recording.json --speed 2.0  # Play at 2x speed
```

### Listing Available Recordings

To see all available recordings:

```bash
python main.py list
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
│   ├── recorder.py     # Handles recording of user actions
│   ├── player.py       # Manages playback of recorded actions
│   └── __init__.py
├── recordings/         # Directory for stored recordings
├── main.py            # Command-line interface
├── requirements.txt    # Project dependencies
└── README.md          # Documentation
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

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the `pynput` library for providing robust input device monitoring
- Inspired by the need for reliable UI automation tools
