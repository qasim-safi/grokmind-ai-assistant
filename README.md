<div align="center">

<img src="https://img.shields.io/badge/GrokMind-AI%20Assistant-7C6FDE?style=for-the-badge&logo=python&logoColor=white" alt="GrokMind" height="40"/>

# 🤖 GrokMind — AI Assistant

### *A sleek, modern AI chat desktop app powered by Groq's FREE API + LLaMA 3.3 70B*

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/CustomTkinter-5.2%2B-7C6FDE?style=flat-square&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Groq%20API-FREE%20Tier-00C8FF?style=flat-square&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/LLaMA%203.3-70B-orange?style=flat-square"/>
  &nbsp;
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=flat-square"/>
</p>

</div>

---

## ✨ Overview

**GrokMind** is a polished, production-ready AI chat assistant desktop application built with Python and **CustomTkinter**. It connects to **Groq's FREE API** running **Meta's LLaMA 3.3 70B** model to provide lightning-fast, intelligent, context-aware conversations right from your desktop — no browser needed, no credit card required.

Whether you want help with code, need a creative writing partner, want to explore complex topics, or simply want a smart conversational AI, GrokMind has you covered — completely free.

---

## 🎨 Features

| Feature | Description |
|---|---|
| 🌑 **Dark Glassmorphism UI** | Stunning deep-navy dark theme with purple accents |
| 💬 **Multi-turn Conversations** | Full conversation context maintained throughout the session |
| ⚡ **Groq Free Tier** | Completely free — no credit card, no payment needed |
| 🦙 **LLaMA 3.3 70B** | Meta's powerful 70B model running on Groq's custom hardware |
| 🔄 **Async Responses** | Non-blocking API calls — UI stays responsive while AI thinks |
| ✍️ **Typing Indicator** | Animated "AI is thinking…" indicator for better UX |
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
- A **Groq API key** (100% FREE — no credit card needed!)
  - Sign up at [console.groq.com](https://console.groq.com/)
  - Go to **API Keys** → **Create API Key**
  - Your key will start with `gsk_...`

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

### 4. Add Your Free Groq API Key

Open `config.py` and replace the placeholder with your Groq key:

```python
# config.py
GROQ_API_KEY: str = "gsk_your_actual_key_here"   # ← paste your free key!
GROQ_MODEL:   str = "llama-3.3-70b-versatile"    # best free model
```

> ⚠️ **Security Warning:** Never commit your real API key to a public repository.
> The `.gitignore` already has instructions to protect `config.py`.

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
# Free Groq API Key (get it at console.groq.com)
GROQ_API_KEY = "gsk_..."          # your key here

# Model Selection (all FREE on Groq)
GROQ_MODEL = "llama-3.3-70b-versatile"   # recommended
# GROQ_MODEL = "llama-3.1-8b-instant"    # fastest
# GROQ_MODEL = "mixtral-8x7b-32768"      # longest context (32k)
# GROQ_MODEL = "gemma2-9b-it"            # Google's Gemma 2

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
| **Groq API (Free)** | AI inference — LLaMA 3.3 70B, ultra-fast |
| **LLaMA 3.3 70B** | Meta's powerful language model |
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
2. **Background thread** sends full history to Groq API (multi-turn context)
3. **Typing indicator** animates while waiting
4. **AI response** is received from LLaMA 3.3 70B and rendered as a styled bubble
5. **Context counter** updates to reflect total words in memory

> Groq's custom LPU hardware makes responses arrive in **under 1 second** on average!

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
