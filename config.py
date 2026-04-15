"""
config.py  —  GrokMind AI Assistant Configuration
===================================================
⚠️  IMPORTANT: Replace 'YOUR_GROK_API_KEY_HERE' with your real xAI Grok API key.
    Get your key at: https://console.x.ai/
    Never commit your real API key to a public repository!
"""

# ── xAI Grok API ────────────────────────────────────────────────────────────
#  Replace the placeholder below with your actual API key.
GROK_API_KEY: str = "YOUR_GROK_API_KEY_HERE"

# Available Grok models (choose one):
#   "grok-3"          — latest, most capable
#   "grok-3-mini"     — faster, cheaper
#   "grok-2-1212"     — previous generation
GROK_MODEL: str = "grok-3"

# ── App Metadata ─────────────────────────────────────────────────────────────
APP_TITLE: str = "GrokMind — AI Assistant"

# ── System Prompt ────────────────────────────────────────────────────────────
# Customise the assistant's personality / focus area here.
SYSTEM_PROMPT: str = (
    "You are GrokMind, a highly intelligent and helpful AI assistant powered by xAI's Grok model. "
    "You are running inside a sleek desktop application built with CustomTkinter. "
    "Be concise but thorough in your answers. When writing code, always include comments. "
    "You can answer questions on any topic: programming, science, creativity, analysis, and more. "
    "Maintain a friendly, professional tone."
)
