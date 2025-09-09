# TTS Notifications for Claude Code - DRAG & DROP READY

This folder contains **pre-generated TTS audio files** for instant Claude Code notifications. Perfect for sharing with friends and teammates! No API keys or setup required!

## What's Included

- **11 Pre-Generated MP3 Files**: Generic notification sounds ready to use
- **Instant Playback**: Zero latency audio feedback
- **Share-Friendly**: No personal names, perfect for teams
- **No API Costs**: Completely offline operation
- **Drag & Drop Ready**: Copy directly to any project

## Files

```
TTS_Notifications/
├── .claude/                      # Complete Claude Code hook configuration
│   ├── settings.json            # Hook configuration for all 3 TTS hooks
│   └── hooks/                   # Hook scripts (API-free)
│       ├── notification.py      # "Agent needs input" TTS (cached only)
│       ├── stop.py              # "Work complete" TTS (cached only)
│       └── subagent_stop.py     # "Subagent complete" TTS (cached only)
├── tts_cache/                   # 11 pre-generated MP3 files (generic)
│   ├── notification*.mp3        # 3 notification variations (no names)
│   ├── work_complete*.mp3       # 5 completion variations  
│   └── subagent_*.mp3           # 3 subagent variations (no names)
└── README.md                    # This file
```

## System Requirements

**Before using this TTS system, ensure you have:**

### Required Software
1. **Python 3.11 or newer**
   - Windows: Download from [python.org](https://python.org/downloads/)
   - Mac: `brew install python` or download from python.org
   - Linux: `sudo apt install python3.11` (Ubuntu/Debian)

2. **uv package manager** (handles dependencies automatically)
   - Install: `curl -LsSf https://astral.sh/uv/install.sh | sh` (Mac/Linux)
   - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - Or: `pip install uv`

3. **System Audio Support**
   - **Windows**: Audio drivers (usually pre-installed)
   - **Mac**: Core Audio (built-in)
   - **Linux**: ALSA/PulseAudio (`sudo apt install python3-dev libasound2-dev`)

### Auto-Installed Dependencies
- `pygame` - Handles MP3 playback (installed automatically by uv)

## Setup Instructions

### ✅ Quick Verification Test
```bash
# Test if your system is ready
python3 --version  # Should show 3.11+
uv --version       # Should show uv version
```

### Per-Project Setup (Recommended)
1. **Install system requirements** (see above)
2. Copy the entire `TTS_Notifications/` folder contents to your Claude Code project root
3. **That's it!** All TTS hooks will work automatically

### Global Setup (All Projects)
1. **Install system requirements** (see above)
2. Copy `.claude/` folder to your global Claude directory: `~/.claude/`
3. Copy `tts_cache/` folder to your global Claude directory: `~/.claude/tts_cache/`  
4. TTS will work across **ALL** Claude Code projects

## 🎵 TTS Messages (11 Generic Variations)

**Notification Sounds (3 variations):**
- "Your agent needs your input"
- "Waiting for your input"
- "Please provide your next instruction"

**Work Complete Sounds (5 variations):**
- "Work complete!"
- "All done!"
- "Task finished!"
- "Job complete!" 
- "Ready for next task!"

**Subagent Complete Sounds (3 variations):**
- "Subagent Complete"
- "Subagent Finished"
- "Subagent Done"

## Key Advantages

### ✅ **Instant Playback**
- **0ms API delay** - sounds play immediately
- **Cached audio files** - no network dependency
- **Smooth workflow** - no interruptions

### ✅ **Zero Cost Operation**
- **No API calls** during normal use
- **Unlimited usage** - cached files never expire
- **Offline capable** - works without internet

### ✅ **Plug & Play**
- **No configuration** required
- **No API keys** needed
- **No dependencies** to install

### ✅ **Professional Quality**
- **ElevenLabs voice** - high-quality synthesis
- **Multiple variations** - prevents notification fatigue
- **Optimal file sizes** - 14-35KB per file

## How It Works

1. **User asks question** → Claude Code processes
2. **Agent needs input** → Plays random notification sound
3. **User provides input** → Claude Code continues
4. **Work completes** → Plays random completion sound
5. **Subagent finishes** → Plays random subagent sound

## File Details

**Total Size**: ~280KB (extremely lightweight)
**Audio Quality**: High-quality ElevenLabs synthesis
**Format**: MP3 (universal compatibility)
**Voice**: Consistent professional voice across all files

## Troubleshooting

### No Audio?
1. **Check system requirements**: Ensure Python 3.11+ and uv are installed
2. **Check file location**: Files must be in `tts_cache/` (relative to project root)
3. **Check speakers**: Ensure audio output is working and volume is up
4. **Check permissions**: Files must be readable by Claude Code
5. **Test manually**: 
   ```bash
   # Test if pygame can play MP3s
   uv run .claude/hooks/notification.py --notify <<< '{"test":"data"}'
   ```

### Linux Audio Issues?
```bash
# Install audio development packages
sudo apt install python3-dev libasound2-dev
# For Ubuntu: may also need
sudo apt install portaudio19-dev
```

### Windows/Mac Audio Issues?
- **Windows**: Ensure audio drivers are installed and working
- **Mac**: Should work out of the box with Core Audio

### uv Not Found?
```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh   # Mac/Linux
# Windows PowerShell:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Want Different Messages or Personal Names?
- This is the **generic sharing version** - messages cannot be changed
- For custom messages or personal names, you'll need the full generation setup
- Requires API keys and regeneration scripts

## Compatibility

**✅ Supported Systems:**
- **Windows 10/11** - With Python 3.11+ and audio drivers
- **macOS 10.15+** - With Python 3.11+ (Homebrew recommended)  
- **Linux (Ubuntu/Debian)** - With Python 3.11+ and audio packages
- **All Claude Code versions** - Works with any hooks setup
- **All project types** - Drag & drop into any codebase

**❌ Not Supported:**
- Python versions < 3.11
- Systems without audio output capability
- Environments where uv/pip cannot install packages

## Performance

- **Playback latency**: <100ms
- **Memory usage**: Minimal (files loaded on demand)
- **CPU usage**: Nearly zero
- **Disk space**: 280KB total

This share-friendly version provides **professional TTS notifications** with **zero setup complexity** and **maximum convenience** for instant deployment across any Claude Code project. Perfect for sharing with friends, teammates, or the community!