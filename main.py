#!/usr/bin/env python3
import argparse
import sys
import signal
from src.recorder import ActivityRecorder
from src.player import ActivityPlayer
import logging
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def signal_handler(signum, frame):
    """Handle interrupt signal"""
    logger.info("\nReceived interrupt signal. Stopping...")
    if recorder and hasattr(recorder, "recording") and recorder.recording:
        recorder.stop_recording()
        filepath = recorder.save_recording()
        if filepath:
            logger.info(f"Recording saved to: {filepath}")
    sys.exit(0)


def record_activity():
    """Record user activity until interrupted"""
    global recorder
    recorder = ActivityRecorder()

    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    logger.info("Starting recording... Press Ctrl+C to stop.")
    recorder.start_recording()

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)


def play_recording(filepath, speed=1.0):
    """Play back a recorded activity"""
    player = ActivityPlayer()

    try:
        player.load_recording(filepath)
        logger.info(f"Playing recording at {speed}x speed...")
        player.play(speed_multiplier=speed)
    except FileNotFoundError:
        logger.error(f"Recording file not found: {filepath}")
    except Exception as e:
        logger.error(f"Error during playback: {str(e)}")


def list_recordings():
    """List all available recordings"""
    recordings_dir = Path(__file__).parent / "recordings"
    if not recordings_dir.exists():
        logger.info("No recordings directory found.")
        return

    recordings = list(recordings_dir.glob("*.json"))
    if not recordings:
        logger.info("No recordings found.")
        return

    logger.info("\nAvailable recordings:")
    for recording in recordings:
        logger.info(f"- {recording.name}")


def main():
    parser = argparse.ArgumentParser(description="Record and play back user activity")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Record command
    record_parser = subparsers.add_parser("record", help="Record user activity")

    # Play command
    play_parser = subparsers.add_parser("play", help="Play back a recording")
    play_parser.add_argument("file", help="Recording file to play")
    play_parser.add_argument(
        "--speed",
        type=float,
        default=1.0,
        help="Playback speed multiplier (default: 1.0)",
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List available recordings")

    args = parser.parse_args()

    if args.command == "record":
        record_activity()
    elif args.command == "play":
        play_recording(args.file, args.speed)
    elif args.command == "list":
        list_recordings()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
