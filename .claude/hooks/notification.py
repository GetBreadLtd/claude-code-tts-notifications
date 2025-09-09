#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pygame",
# ]
# ///

import argparse
import json
import os
import sys
import random
from pathlib import Path


def announce_notification():
    """Announce that the agent needs user input using cached MP3s."""
    try:
        import pygame
        
        # Define available cached MP3 files for notifications  
        cache_dir = Path("tts_cache")
        notification_files = [
            "notification.mp3",         # "Your agent needs your input"
            "notification_waiting.mp3", # "Waiting for your input"
            "notification_ready.mp3"    # "Please provide your next instruction"
        ]
        
        # Randomly select a notification MP3
        selected_file = random.choice(notification_files)
        mp3_path = cache_dir / selected_file
        
        # Play cached MP3 if it exists
        if mp3_path.exists():
            pygame.mixer.init()
            pygame.mixer.music.load(str(mp3_path))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            pygame.mixer.quit()
            return
        
    except Exception:
        # Silent fail if pygame or file issues
        pass


def main():
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--notify', action='store_true', help='Enable TTS notifications')
        args = parser.parse_args()
        
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Ensure log directory exists
        log_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'notification.json')
        
        # Read existing log data or initialize empty list
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                try:
                    log_data = json.load(f)
                except (json.JSONDecodeError, ValueError):
                    log_data = []
        else:
            log_data = []
        
        # Append new data
        log_data.append(input_data)
        
        # Write back to file with formatting
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        # Announce notification via TTS only if --notify flag is set
        if args.notify:
            announce_notification()
        
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)

if __name__ == '__main__':
    main()