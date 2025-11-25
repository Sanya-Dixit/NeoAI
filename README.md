```markdown
# 🚀 NeoAI — Your Voice Assistant (Online & Offline)

NeoAI is a small, friendly voice assistant you can run locally.  
It supports two modes:
- Online: conversational AI using OpenAI (gpt-3.5-turbo by default)
- Offline: simple rule-based replies and local actions (open websites, tell time, play music)

This README is short, practical, and easy to follow — get started in minutes.

---

✨ Key features
- Microphone input (speech_recognition)
- Text-to-speech (pyttsx3) — cross-platform
- Online chat via OpenAI Chat API
- Offline fallback with canned responses
- Windows-friendly helper scripts and PowerShell support
- Quick diagnostic scripts for the OpenAI connection

---

🛠️ Quick setup (copy & paste)

1. Create a virtual environment and activate it:
- Windows (PowerShell)
  ```
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- macOS / Linux
  ```
  python -m venv .venv
  source .venv/bin/activate
  ```

2. Install dependencies:
```
pip install -r requirements.txt
```

Note: pyaudio may require system libraries:
- Windows: use pipwin (pip install pipwin; pipwin install pyaudio)
- macOS: brew install portaudio
- Ubuntu/Debian: sudo apt-get install portaudio19-dev

---

⚙️ Configuration (safe & simple)

Recommended: use an environment variable.

1) Add your API key to your shell (example):
- Windows (PowerShell)
  ```
  $env:OPENAI_API_KEY="sk-..."
  ```
- macOS / Linux
  ```
  export OPENAI_API_KEY="sk-..."
  ```

2) Use config.py that reads the env var:
```python
# config.py
import os
apikey = os.getenv("OPENAI_API_KEY", "")
```

If you keep a local config.py with the key, NEVER commit it. .gitignore should block it.

---

▶️ How to run

- Online (ChatGPT-powered):
  ```
  python main.py
  ```
  Listens to your mic, sends chat to OpenAI, speaks the response.

- Offline (local responses only):
  ```
  python neo_offline.py
  ```
 
 - Quick OpenAI test:
  ```
  python quick_test.py
  ```

- Run the Windows menu (interactive):
  ```
  run_neo_menu.bat
  ```

- PowerShell helper:
  ```
  .\run_mode.ps1 -Mode online
  .\run_mode.ps1 -Mode offline
  .\run_mode.ps1 -Mode test
  ```

---

🧭 How the assistant behaves

- While listening, speech is transcribed with Google Speech Recognition (internet required for transcription).
- Online mode uses OpenAI Chat Completions via the OpenAI client.
- Offline mode matches simple phrases to canned replies (fast, no internet).
- Built-in actions: open YouTube / Google / Wikipedia, tell time, play a local music file (update the path in main.py / neo_offline.py).

---

⚠️ Troubleshooting (quick checks)

- "Authentication" or 401 errors:
  - Ensure OPENAI_API_KEY is set correctly and billing is enabled.
- "Quota" or 429 errors:
  - Check usage and billing at https://platform.openai.com/usage
- Microphone not working:
  - Confirm OS privacy settings allow mic access for Python/Terminal.
- PyAudio install fails:
  - Use pipwin on Windows or install portaudio dev headers on macOS/Linux.

Helpful diagnostics:
- Run: python test_import.py
- Run: python quick_test.py
- Run: python diagnose_openai.py (gives helpful hints)

---

🔧 Optional improvements (ideas)
- Move all secret handling to environment variables or a secrets manager
- Persist chat history (SQLite / Redis) for multi-session context
- Add a simple web UI to view streaming responses and transcripts
- Add adapters for other LLM providers or local model servers

---

🤝 Contributing
1. Fork the repo
2. Create a branch: git checkout -b feature/my-change
3. Make changes, add tests where useful
4. Open a PR with a clear description

Please avoid committing API keys or personal data.

---

📄 License
MIT — choose or update the license file as needed.

---

❤️ Thanks
Built with speech_recognition, pyttsx3, and the OpenAI Python SDK. Inspired by many open-source voice agents and LLM demos.

```
