"""
config.py  —  GrokMind AI Assistant Configuration
===================================================
Powered by Groq's FREE API — sign up at https://console.groq.com/
No credit card required. Get your free API key in 2 minutes!

⚠️  SECURITY: Add your real key below locally. NEVER push this file
    to GitHub once it contains a real key.
"""

# ── Groq API (FREE tier) ─────────────────────────────────────────────────────
#  1. Sign up free at: https://console.groq.com/
#  2. Go to API Keys → Create API Key
#  3. Paste your key below (starts with "gsk_...")
GROQ_API_KEY: str = "YOUR_GROQ_API_KEY_HERE"

# ── Model Selection ───────────────────────────────────────────────────────────
# All models below are FREE on Groq's free tier:
#
#   "llama-3.3-70b-versatile"   ← Recommended: smart & fast (6000 tok/min)
#   "llama-3.1-8b-instant"      ← Fastest, lower limits
#   "mixtral-8x7b-32768"        ← Long context (32k tokens)
#   "gemma2-9b-it"              ← Google's Gemma 2
GROQ_MODEL: str = "llama-3.3-70b-versatile"

# ── App Metadata ──────────────────────────────────────────────────────────────
APP_TITLE: str = "GrokMind — AI Assistant"

# ── System Prompt ─────────────────────────────────────────────────────────────
# Customise the assistant's personality / focus area here.
SYSTEM_PROMPT: str = (
    "You are GrokMind, a highly intelligent and helpful AI assistant powered by "
    "Meta's LLaMA 3.3 70B model via Groq's ultra-fast inference. "
    "You are running inside a sleek desktop application built with CustomTkinter. "
    "Be concise but thorough. When writing code, always include comments. "
    "You can help with programming, science, creativity, analysis, and more. "
    "Maintain a friendly, professional tone."
)

