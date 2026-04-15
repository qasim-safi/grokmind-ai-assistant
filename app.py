"""
GrokMind AI Assistant
=====================
A modern AI-powered desktop chat application built with CustomTkinter.
Powered by xAI's Grok API.

Author  : Qasim Safi
GitHub  : https://github.com/qasim-safi
Version : 1.0.0
"""

import customtkinter as ctk
import threading
import json
import urllib.request
import urllib.error
import datetime
import os
from config import GROQ_API_KEY, GROQ_MODEL, APP_TITLE, SYSTEM_PROMPT

# ── Theme ──────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Colour palette ─────────────────────────────────────────────────────────
BG_MAIN        = "#0D0F1A"   # deep navy
BG_SIDEBAR     = "#12152A"   # slightly lighter navy
BG_BUBBLE_USER = "#1E3A5F"   # user message bubble
BG_BUBBLE_AI   = "#1A1D2E"   # AI message bubble
ACCENT         = "#7C6FDE"   # purple accent (Grok-inspired)
ACCENT_HOVER   = "#9B8FEF"
TEXT_PRIMARY   = "#E8E8F0"
TEXT_SECONDARY = "#8A8AB0"
SUCCESS        = "#4CAF83"
BORDER_COLOR   = "#2A2D45"


# ── Helpers ─────────────────────────────────────────────────────────────────
def call_groq_api(messages: list) -> str:
    """
    Call the Groq API (FREE tier) using the OpenAI-compatible chat endpoint.

    Endpoint : https://api.groq.com/openai/v1/chat/completions
    Docs     : https://console.groq.com/docs/openai
    Free tier: 6000 tokens/min, 500 req/day on llama-3.3-70b-versatile

    messages = list of {"role": "system"|"user"|"assistant", "content": str}
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    payload = {
        "model":       GROQ_MODEL,
        "messages":    messages,
        "temperature": 0.7,
        "max_tokens":  2048,
    }
    headers = {
        "Content-Type":  "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }

    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(url, data=data, headers=headers, method="POST")

    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    return body["choices"][0]["message"]["content"]





# ── Message Bubble ──────────────────────────────────────────────────────────
class MessageBubble(ctk.CTkFrame):
    """A single chat message bubble (user or AI)."""

    def __init__(self, master, text: str, role: str, timestamp: str, **kwargs):
        is_user = role == "user"
        super().__init__(
            master,
            fg_color=BG_BUBBLE_USER if is_user else BG_BUBBLE_AI,
            corner_radius=16,
            border_width=1,
            border_color=ACCENT if is_user else BORDER_COLOR,
            **kwargs,
        )

        # ── Header row (avatar + label + time) ──
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=14, pady=(10, 2))

        avatar_text = "  You  " if is_user else "  Grok  "
        avatar_color = ACCENT if is_user else SUCCESS

        avatar = ctk.CTkLabel(
            header,
            text=avatar_text,
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color="#0D0F1A",
            fg_color=avatar_color,
            corner_radius=8,
            width=50,
            height=20,
        )
        avatar.pack(side="left")

        time_lbl = ctk.CTkLabel(
            header,
            text=timestamp,
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color=TEXT_SECONDARY,
        )
        time_lbl.pack(side="right")

        # ── Message text ──
        msg = ctk.CTkLabel(
            self,
            text=text,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_PRIMARY,
            wraplength=560,
            justify="left",
            anchor="w",
        )
        msg.pack(fill="x", padx=14, pady=(4, 12))


# ── Typing indicator ────────────────────────────────────────────────────────
class TypingIndicator(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=BG_BUBBLE_AI, corner_radius=16,
                         border_width=1, border_color=BORDER_COLOR, **kwargs)
        self._dots  = 0
        self._label = ctk.CTkLabel(
            self,
            text="Grok is thinking ●",
            font=ctk.CTkFont(family="Segoe UI", size=13, slant="italic"),
            text_color=TEXT_SECONDARY,
        )
        self._label.pack(padx=18, pady=12)
        self._animate()

    def _animate(self):
        patterns = ["Grok is thinking ●", "Grok is thinking ● ●", "Grok is thinking ● ● ●"]
        self._dots = (self._dots + 1) % 3
        self._label.configure(text=patterns[self._dots])
        self._job = self.after(500, self._animate)

    def destroy(self):
        if hasattr(self, "_job"):
            self.after_cancel(self._job)
        super().destroy()


# ── Main Window ─────────────────────────────────────────────────────────────
class GrokMindApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("1100x720")
        self.minsize(800, 560)
        self.configure(fg_color=BG_MAIN)
        self._set_icon()

        # conversation history (for multi-turn context)
        self._history: list[dict] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self._typing_widget = None

        self._build_ui()

    # ── icon (ignore errors) ──
    def _set_icon(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

    # ── UI Layout ────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Main container: sidebar | chat pane
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_chat_pane()

    # ── Sidebar ───────────────────────────────────────────────────────────────
    def _build_sidebar(self):
        sidebar = ctk.CTkFrame(self, fg_color=BG_SIDEBAR, corner_radius=0, width=220)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # Logo / branding
        logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_frame.pack(fill="x", padx=20, pady=(30, 6))

        ctk.CTkLabel(
            logo_frame,
            text="🤖",
            font=ctk.CTkFont(size=38),
        ).pack()

        ctk.CTkLabel(
            logo_frame,
            text="GrokMind",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color=TEXT_PRIMARY,
        ).pack(pady=(4, 0))

        ctk.CTkLabel(
            logo_frame,
            text="AI Assistant",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=ACCENT,
        ).pack()

        # Divider
        ctk.CTkFrame(sidebar, fg_color=BORDER_COLOR, height=1).pack(
            fill="x", padx=20, pady=20
        )

        # Model badge
        ctk.CTkLabel(
            sidebar,
            text="MODEL",
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color=TEXT_SECONDARY,
        ).pack(anchor="w", padx=24)

        ctk.CTkLabel(
            sidebar,
            text=f"⚡ {GROQ_MODEL}",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=ACCENT,
        ).pack(anchor="w", padx=24, pady=(2, 16))

        # Action buttons
        self._btn_new = ctk.CTkButton(
            sidebar,
            text="＋  New Chat",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            fg_color=ACCENT,
            hover_color=ACCENT_HOVER,
            corner_radius=10,
            height=40,
            command=self._new_chat,
        )
        self._btn_new.pack(fill="x", padx=20, pady=(0, 10))

        self._btn_clear = ctk.CTkButton(
            sidebar,
            text="🗑  Clear History",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="transparent",
            hover_color=BG_BUBBLE_AI,
            border_color=BORDER_COLOR,
            border_width=1,
            text_color=TEXT_SECONDARY,
            corner_radius=10,
            height=36,
            command=self._clear_history,
        )
        self._btn_clear.pack(fill="x", padx=20, pady=4)

        # Spacer
        ctk.CTkFrame(sidebar, fg_color="transparent").pack(fill="both", expand=True)

        # Status dot
        status_row = ctk.CTkFrame(sidebar, fg_color="transparent")
        status_row.pack(fill="x", padx=20, pady=(0, 24))
        api_ready = GROQ_API_KEY and GROQ_API_KEY != "YOUR_GROQ_API_KEY_HERE"
        dot_color = SUCCESS if api_ready else "#E05C5C"
        dot_text  = "● Groq Free Tier Ready" if api_ready else "● Add API Key in config.py"
        ctk.CTkLabel(
            status_row,
            text=dot_text,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=dot_color,
        ).pack(anchor="w")

        ctk.CTkLabel(
            status_row,
            text="github.com/qasim-safi",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color=TEXT_SECONDARY,
        ).pack(anchor="w", pady=(4, 0))

    # ── Chat pane ─────────────────────────────────────────────────────────────
    def _build_chat_pane(self):
        pane = ctk.CTkFrame(self, fg_color=BG_MAIN, corner_radius=0)
        pane.grid(row=0, column=1, sticky="nsew")
        pane.grid_rowconfigure(1, weight=1)
        pane.grid_columnconfigure(0, weight=1)

        # ── Top bar ──
        topbar = ctk.CTkFrame(pane, fg_color=BG_SIDEBAR, corner_radius=0, height=58)
        topbar.grid(row=0, column=0, sticky="ew")
        topbar.grid_propagate(False)

        ctk.CTkLabel(
            topbar,
            text="💬  Chat with Grok",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=TEXT_PRIMARY,
        ).pack(side="left", padx=22, pady=14)

        self._token_lbl = ctk.CTkLabel(
            topbar,
            text="",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXT_SECONDARY,
        )
        self._token_lbl.pack(side="right", padx=22)

        # ── Scroll area ──
        self._scroll = ctk.CTkScrollableFrame(
            pane,
            fg_color=BG_MAIN,
            scrollbar_button_color=BORDER_COLOR,
            scrollbar_button_hover_color=ACCENT,
        )
        self._scroll.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self._scroll.grid_columnconfigure(0, weight=1)

        # Welcome banner
        self._show_welcome()

        # ── Input bar ──
        input_bar = ctk.CTkFrame(pane, fg_color=BG_SIDEBAR, corner_radius=0, height=80)
        input_bar.grid(row=2, column=0, sticky="ew")
        input_bar.grid_propagate(False)
        input_bar.grid_columnconfigure(0, weight=1)

        self._input = ctk.CTkTextbox(
            input_bar,
            height=48,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color=BG_BUBBLE_AI,
            border_color=BORDER_COLOR,
            border_width=1,
            text_color=TEXT_PRIMARY,
            corner_radius=12,
            wrap="word",
        )
        self._input.grid(row=0, column=0, padx=(16, 8), pady=16, sticky="ew")
        self._input.bind("<Return>", self._on_enter)
        self._input.bind("<Shift-Return>", lambda e: None)   # allow newline with shift

        self._send_btn = ctk.CTkButton(
            input_bar,
            text="Send  ➤",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            fg_color=ACCENT,
            hover_color=ACCENT_HOVER,
            corner_radius=12,
            width=100,
            height=48,
            command=self._send_message,
        )
        self._send_btn.grid(row=0, column=1, padx=(0, 16), pady=16)

    # ── Welcome banner ────────────────────────────────────────────────────────
    def _show_welcome(self):
        frame = ctk.CTkFrame(
            self._scroll,
            fg_color=BG_BUBBLE_AI,
            corner_radius=20,
            border_width=1,
            border_color=ACCENT,
        )
        frame.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="ew")

        ctk.CTkLabel(
            frame,
            text="🤖  Welcome to GrokMind",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=TEXT_PRIMARY,
        ).pack(pady=(20, 6))

        ctk.CTkLabel(
            frame,
            text="Powered by Groq (FREE) + LLaMA 3.3 70B — your intelligent AI companion.\nAsk me anything: code, analysis, creative writing, or just chat!",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_SECONDARY,
            justify="center",
        ).pack(pady=(0, 20))

        # Quick-prompt chips
        chips_frame = ctk.CTkFrame(frame, fg_color="transparent")
        chips_frame.pack(pady=(0, 20))

        quick_prompts = [
            "Write a Python function",
            "Explain machine learning",
            "Tell me a fun fact",
            "Debug my code",
        ]
        for qp in quick_prompts:
            btn = ctk.CTkButton(
                chips_frame,
                text=qp,
                font=ctk.CTkFont(family="Segoe UI", size=11),
                fg_color="transparent",
                hover_color=BG_BUBBLE_USER,
                border_color=ACCENT,
                border_width=1,
                text_color=ACCENT,
                corner_radius=20,
                height=28,
                command=lambda p=qp: self._quick_prompt(p),
            )
            btn.pack(side="left", padx=4)

        self._welcome_frame = frame
        self._next_row = 1   # tracks next grid row for new bubbles

    # ── Event handlers ────────────────────────────────────────────────────────
    def _on_enter(self, event):
        # Shift+Return → insert newline; plain Return → send
        if not (event.state & 0x1):   # shift not held
            self._send_message()
            return "break"

    def _quick_prompt(self, text: str):
        self._input.delete("1.0", "end")
        self._input.insert("end", text)
        self._send_message()

    def _send_message(self):
        text = self._input.get("1.0", "end").strip()
        if not text:
            return
        self._input.delete("1.0", "end")
        self._add_bubble(text, "user")
        self._history.append({"role": "user", "content": text})
        self._show_typing()
        self._send_btn.configure(state="disabled", text="…")
        threading.Thread(target=self._fetch_response, daemon=True).start()

    def _fetch_response(self):
        try:
            reply = call_groq_api(self._history)
            self._history.append({"role": "assistant", "content": reply})
            self.after(0, lambda: self._on_response(reply))
        except Exception as exc:
            error_msg = (
                f"Error: {exc}\n\n"
                "Please check your Groq API key in config.py.\n"
                "Get a FREE key at: https://console.groq.com/"
            )
            self.after(0, lambda: self._on_response(error_msg, is_error=True))

    def _on_response(self, text: str, is_error: bool = False):
        self._hide_typing()
        self._add_bubble(text, "assistant")
        self._send_btn.configure(state="normal", text="Send  ➤")
        self._update_token_label()

    # ── Chat helpers ──────────────────────────────────────────────────────────
    def _add_bubble(self, text: str, role: str):
        ts = datetime.datetime.now().strftime("%H:%M")
        bubble = MessageBubble(
            self._scroll, text=text, role=role, timestamp=ts
        )
        padx_left  = 80 if role == "user" else 16
        padx_right = 16 if role == "user" else 80
        bubble.grid(
            row=self._next_row, column=0,
            padx=(padx_left, padx_right), pady=6, sticky="ew"
        )
        self._next_row += 1
        self.update_idletasks()
        self._scroll._parent_canvas.yview_moveto(1.0)

    def _show_typing(self):
        self._typing_widget = TypingIndicator(self._scroll)
        self._typing_widget.grid(
            row=self._next_row, column=0,
            padx=(16, 80), pady=6, sticky="w"
        )
        self._next_row += 1
        self.update_idletasks()
        self._scroll._parent_canvas.yview_moveto(1.0)

    def _hide_typing(self):
        if self._typing_widget:
            self._typing_widget.destroy()
            self._typing_widget = None
            self._next_row -= 1

    def _update_token_label(self):
        count = sum(len(m["content"].split()) for m in self._history)
        self._token_lbl.configure(text=f"~{count} words in context")

    def _new_chat(self):
        """Clear the UI and start a fresh conversation."""
        for widget in self._scroll.winfo_children():
            widget.destroy()
        self._history = [{"role": "system", "content": SYSTEM_PROMPT}]
        self._next_row = 0
        self._token_lbl.configure(text="")
        self._show_welcome()

    def _clear_history(self):
        """Keep the UI but reset conversation history (keeps system prompt)."""
        self._history = [{"role": "system", "content": SYSTEM_PROMPT}]
        self._update_token_label()


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = GrokMindApp()
    app.mainloop()
