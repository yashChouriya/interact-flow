import json
import time
from pathlib import Path
from pynput import mouse, keyboard
import logging
from pynput.keyboard import Key, KeyCode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActivityPlayer:
    def __init__(self):
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        self.events = []
        self.start_time = None
        self.playing = False

    def load_recording(self, filepath):
        """Load a recording from a file"""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"Recording file not found: {filepath}")
            
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        if 'version' not in data or 'events' not in data:
            raise ValueError("Invalid recording file format")
            
        self.events = data['events']
        logger.info(f"Loaded {len(self.events)} events from {filepath}")

    def _parse_key(self, key_str):
        """Parse key string into a Key object"""
        # Handle special keys
        if key_str.startswith('Key.'):
            key_name = key_str.split('.')[1]
            return getattr(Key, key_name, None)
        # Handle regular characters
        else:
            # Remove quotes from the string
            char = key_str.strip("'")
            return KeyCode.from_char(char)

    def play(self, speed_multiplier=1.0):
        """Play back the recorded events"""
        if not self.events:
            logger.warning("No events to play")
            return
            
        self.playing = True
        self.start_time = time.time()
        last_event_time = 0
        
        try:
            for event in self.events:
                if not self.playing:
                    break
                    
                # Calculate and apply delay
                event_time = event['timestamp']
                delay = (event_time - last_event_time) / speed_multiplier
                if delay > 0:
                    time.sleep(delay)
                last_event_time = event_time
                
                # Handle different event types
                try:
                    if event['type'] == 'mouse_move':
                        self.mouse_controller.position = (event['x'], event['y'])
                        
                    elif event['type'] == 'mouse_click':
                        self.mouse_controller.position = (event['x'], event['y'])
                        button = getattr(mouse.Button, event['button'].split('.')[-1])
                        if event['pressed']:
                            self.mouse_controller.press(button)
                        else:
                            self.mouse_controller.release(button)
                            
                    elif event['type'] == 'mouse_scroll':
                        self.mouse_controller.scroll(event['dx'], event['dy'])
                        
                    elif event['type'] == 'keyboard_press':
                        key = self._parse_key(event['key'])
                        if key:
                            self.keyboard_controller.press(key)
                            
                    elif event['type'] == 'keyboard_release':
                        key = self._parse_key(event['key'])
                        if key:
                            self.keyboard_controller.release(key)
                            
                except Exception as e:
                    logger.error(f"Error playing event {event}: {str(e)}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error during playback: {str(e)}")
        finally:
            self.playing = False
            logger.info("Playback finished")

    def stop(self):
        """Stop the playback"""
        self.playing = False
        logger.info("Playback stopped")