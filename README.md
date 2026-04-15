<div align="center">

<img src="https://img.shields.io/badge/GrokMind-AI%20Assistant-7C6FDE?style=for-the-badge&logo=python&logoColor=white" alt="GrokMind" height="40"/>

# 🤖 GrokMind — AI Assistant

### *A sleek, modern AI chat desktop app powered by xAI's Grok API*

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/CustomTkinter-5.2%2B-7C6FDE?style=flat-square&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/xAI%20Grok%20API-Powered-00C8FF?style=flat-square&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=flat-square"/>
</p>

</div>

---

## ✨ Overview

**GrokMind** is a polished, production-ready AI chat assistant desktop application built with Python and **CustomTkinter**. It connects to **xAI's Grok API** to provide intelligent, context-aware conversations right from your desktop — no browser needed.

Whether you want help with code, need a creative writing partner, want to explore complex topics, or simply want a smart conversational assistant, GrokMind has you covered.

---

## 🎨 Features

| Feature | Description |
|---|---|
| 🌑 **Dark Glassmorphism UI** | Stunning deep-navy dark theme with purple accents |
| 💬 **Multi-turn Conversations** | Full conversation context maintained throughout the session |
| ⚡ **Grok-3 Powered** | Uses xAI's most capable Grok model by default |
| 🔄 **Async Responses** | Non-blocking API calls — UI stays responsive while Grok thinks |
| ✍️ **Typing Indicator** | Animated "Grok is thinking…" indicator for better UX |
| 🗂️ **New Chat / Clear History** | Easily start fresh or reset context |
| 🏷️ **Quick Prompt Chips** | One-click starter prompts for common tasks |
| 📊 **Context Word Counter** | Live counter showing how many words are in the current context |
| 🔒 **Secure Config** | API key stored separately in `config.py`, excluded from git |
| 🖥️ **Cross-Platform** | Runs on Windows, macOS, and Linux |

---

## 🖼️ Screenshots

> 📸 *Screenshots will be added once the app is running with a live API key.*

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10** or higher
- A valid **xAI Grok API key** — get yours at [console.x.ai](https://console.x.ai/)

---

### 1. Clone the Repository

```bash
git clone https://github.com/qasim-safi/grokmind-ai-assistant.git
cd grokmind-ai-assistant
```

---

### 2. Create a Virtual Environment *(Recommended)*

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) — Modern Python GUI framework

> All HTTP calls use Python's built-in `urllib` — no extra HTTP library needed!

---

### 4. Add Your API Key

Open `config.py` and replace the placeholder with your real Grok API key:

```python
# config.py
GROK_API_KEY: str = "YOUR_GROK_API_KEY_HERE"   # ← Replace this!
```

> ⚠️ **Security Warning:** Never commit your real API key to a public repository.
> Add `config.py` to `.gitignore` if you want, or use environment variables.

---

### 5. Run the App

```bash
python app.py
```

The GrokMind window will launch instantly! 🎉

---

## ⚙️ Configuration

All settings live in **`config.py`**:

```python
# API Key — required
GROK_API_KEY = "xai-..."

# Model Selection
GROK_MODEL = "grok-3"          # Options: grok-3, grok-3-mini, grok-2-1212

# App Window Title
APP_TITLE = "GrokMind — AI Assistant"

# System Prompt — customize the assistant's personality
SYSTEM_PROMPT = "You are GrokMind, a highly intelligent and helpful AI assistant..."
```

---

## 📁 Project Structure

```
grokmind-ai-assistant/
│
├── app.py               # Main application — UI layout & logic
├── config.py            # API key, model, and system prompt settings
├── requirements.txt     # Python dependencies (customtkinter)
├── .gitignore           # Excludes API keys, venv, __pycache__, etc.
└── README.md            # This file
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core programming language |
| **CustomTkinter** | Modern, cross-platform GUI framework |
| **xAI Grok API** | AI intelligence layer (chat completions) |
| **urllib (stdlib)** | HTTP requests — no extra dependencies |
| **threading (stdlib)** | Non-blocking async API calls |

---

## 🧠 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        GrokMind App                             │
│                                                                 │
│  ┌──────────────┐    User types message                        │
│  │  Input Bar   │ ──────────────────────►  _send_message()     │
│  └──────────────┘                               │               │
│                                                 ▼               │
│                          Background thread: call_grok_api()     │
│                                                 │               │
│                          xAI Grok API (HTTPS)   │               │
│                                  ◄──────────────┘               │
│                                  │                              │
│                                  ▼                              │
│  ┌──────────────┐    Response bubble rendered                   │
│  │  Chat Pane   │ ◄────────────────────────────────────────     │
│  └──────────────┘                                               │
└─────────────────────────────────────────────────────────────────┘
```

1. **User sends a message** → added to conversation history
2. **Background thread** sends full history to Grok API (multi-turn context)
3. **Typing indicator** animates while waiting
4. **AI response** is received and rendered as a styled bubble
5. **Context counter** updates to reflect total words in memory

---

## 🎨 UI Design

| Element | Color |
|---|---|
| Background | `#0D0F1A` — Deep Navy |
| Sidebar | `#12152A` — Dark Navy |
| Accent / Purple | `#7C6FDE` — Grok Purple |
| User Bubbles | `#1E3A5F` — Blue-Navy |
| AI Bubbles | `#1A1D2E` — Dark Slate |
| Success Green | `#4CAF83` |
| Text | `#E8E8F0` |

---

## 🔒 Security Notes

- Your API key is **only stored in `config.py`** locally
- The `.gitignore` excludes sensitive files like `.env` and `secrets.py`
- **Never push your real API key** to GitHub — use environment variables for production:

```python
import os
GROK_API_KEY = os.environ.get("GROK_API_KEY", "YOUR_GROK_API_KEY_HERE")
```

---

## 🌱 Planned Features

- [ ] 📁 Export chat history as `.txt` or `.md`
- [ ] 🎨 Theme switcher (Light / Dark / Custom)
- [ ] 🔊 Text-to-speech responses
- [ ] 📌 Pin favourite messages
- [ ] 🌐 Multiple conversation tabs
- [ ] 🔐 API key entry dialog on first launch

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Qasim Safi**

[![GitHub](https://img.shields.io/badge/GitHub-qasim--safi-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/qasim-safi)

*BS Software Engineering Student | Python Developer | GUI & AI Enthusiast*

</div>

---

<div align="center">

⭐ **If you found this project useful, please give it a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C6FDE&height=80&section=footer" />

</div>
