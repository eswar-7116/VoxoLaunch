# VoxoLaunch: Voice controlled app launcher

VoxoLaunch is a Python-based, voice-controlled app launcher that allows users to open applications, search Google, and play YouTube videos using voice commands. It leverages speech recognition and text-to-speech technologies to provide a hands-free experience.

### Features

- **Open Applications:** Launch installed applications by saying "open [app name]".
- **Google Search:** Perform Google searches with "search [query]".
- **YouTube Playback:** Play YouTube videos with "play [video name]".
- **Voice Interaction:** Uses a female voice by default for responses (configurable by changing the index of `voices` array).

### Prerequisites

- Python 3.8 or higher
- A microphone connected to your system
- Internet connection for Wit.ai speech recognition and web-based features
- A Wit.ai API key (sign up at [Wit.ai](https://wit.ai/apps) to obtain one)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/eswar-7116/VoxoLaunch.git
   cd voxolaunch
   ```

2. **Install Dependencies:** Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   - Create a .env file in the project root.
   - Add your Wit.ai API key:
     ```bash
     WIT_API_KEY=your_wit_ai_api_key_here
     ```
4. **Ensure Microphone Access:**
   - Ensure your system has a working microphone.
   - If needed, grant microphone access permissions to Python.

### Usage

To run the script:

```bash
python main.py
```

The assistant will start listening for voice commands

### Supported Commands:

- **Open an application:** Say "open [app name]" (e.g., "open notepad").
- **Search Google:** Say "search [query]" (e.g., "search Python tutorials").
- **Play YouTube video:** Say "play [video name]" (e.g., "play happy birthday song").
- **Exit:** Press `Ctrl+C` to stop the program.

### Configuration

- **Voice Settings:**

  - The assistant uses a female voice by default (`voices[1]`). To change to a male voice, modify the `engine.setProperty("voice", voices[0].id)` line in the code.

  - Adjust the speech rate by modifying `engine.setProperty("rate", 180)`.

- **Timeouts:**
  - The microphone listens for up to 7 seconds (`timeout=7`) with a 5-second phrase limit (`phrase_time_limit=5`). Adjust these in the `listen()` function if needed.

### Dependencies

- `speechrecognition`: For capturing and processing voice input via Wit.ai.

- `pyttsx4`: For text-to-speech output.

- `python-dotenv`: For loading environment variables from a `.env` file.

- `AppOpener`: For launching applications by name.

- `pywhatkit`: For Google searches and YouTube playback.

### Troubleshooting

- **"Didn't get that!":** Ensure your microphone is working and background noise is minimal.

- **"Could not find [app name]":** Verify the application is installed and try the exact name or a close match.

- **"VoxoLaunch can't connect to Wit.ai":** Check your internet connection and ensure the `WIT_API_KEY` is correctly set in the `.env` file.

## Grant this repo a star 🌟 if you like the project.
