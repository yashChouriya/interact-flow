import time
from pynput import mouse, keyboard
import json
from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActivityRecorder:
    def __init__(self):
        self.events = []
        self.start_time = None
        self.recording = False
        self.mouse_listener = None
        self.keyboard_listener = None
        self.last_mouse_position = None
        
    def start_recording(self):
        """Start recording user activity"""
        if self.recording:
            logger.warning("Recording is already in progress")
            return
            
        self.events = []
        self.start_time = time.time()
        self.recording = True
        
        # Start mouse listener
        self.mouse_listener = mouse.Listener(
            on_move=self._on_mouse_move,
            on_click=self._on_mouse_click,
            on_scroll=self._on_mouse_scroll
        )
        
        # Start keyboard listener
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_keyboard_press,
            on_release=self._on_keyboard_release
        )
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        logger.info("Recording started...")

    def stop_recording(self):
        """Stop recording user activity"""
        if not self.recording:
            logger.warning("No recording in progress")
            return
            
        self.recording = False
        
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            
        logger.info("Recording stopped...")

    def _get_timestamp(self):
        """Get timestamp relative to recording start time"""
        return time.time() - self.start_time

    def _on_mouse_move(self, x, y):
        """Handle mouse movement events"""
        if not self.recording:
            return
            
        # Only record if position has changed significantly (5 pixels threshold)
        if self.last_mouse_position:
            last_x, last_y = self.last_mouse_position
            if abs(x - last_x) < 5 and abs(y - last_y) < 5:
                return
                
        self.last_mouse_position = (x, y)
        
        event = {
            'type': 'mouse_move',
            'timestamp': self._get_timestamp(),
            'x': x,
            'y': y
        }
        self.events.append(event)

    def _on_mouse_click(self, x, y, button, pressed):
        """Handle mouse click events"""
        if not self.recording:
            return
            
        event = {
            'type': 'mouse_click',
            'timestamp': self._get_timestamp(),
            'x': x,
            'y': y,
            'button': str(button),
            'pressed': pressed
        }
        self.events.append(event)

    def _on_mouse_scroll(self, x, y, dx, dy):
        """Handle mouse scroll events"""
        if not self.recording:
            return
            
        event = {
            'type': 'mouse_scroll',
            'timestamp': self._get_timestamp(),
            'x': x,
            'y': y,
            'dx': dx,
            'dy': dy
        }
        self.events.append(event)

    def _on_keyboard_press(self, key):
        """Handle keyboard press events"""
        if not self.recording:
            return
            
        event = {
            'type': 'keyboard_press',
            'timestamp': self._get_timestamp(),
            'key': str(key)
        }
        self.events.append(event)

    def _on_keyboard_release(self, key):
        """Handle keyboard release events"""
        if not self.recording:
            return
            
        event = {
            'type': 'keyboard_release',
            'timestamp': self._get_timestamp(),
            'key': str(key)
        }
        self.events.append(event)

    def save_recording(self, filename=None):
        """Save recorded events to a file"""
        if not self.events:
            logger.warning("No events to save")
            return None
            
        if filename is None:
            # Generate filename based on current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.json"
            
        recordings_dir = Path(__file__).parent.parent / "recordings"
        recordings_dir.mkdir(exist_ok=True)
        filepath = recordings_dir / filename
        
        recording_data = {
            'version': '1.0',
            'timestamp': datetime.now().isoformat(),
            'events': self.events
        }
        
        with open(filepath, 'w') as f:
            json.dump(recording_data, f, indent=2)
            
        logger.info(f"Recording saved to {filepath}")
        return filepath