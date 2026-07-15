from __future__ import annotations

from typing import Any


class PromptBuilder:
    MOOD_MAP = {
        "motivated": "a motivated and uplifting atmosphere",
        "calm": "a calm and peaceful atmosphere",
        "focused": "a focused and distraction-free atmosphere",
        "coding": "a coding-focused and modern tech atmosphere",
        "study": "a thoughtful and study-oriented atmosphere",
        "gaming": "an energetic and immersive gaming atmosphere",
    }

    STYLE_MAP = {
        "minimal": "premium minimalist digital art style",
        "cyberpunk": "cinematic cyberpunk digital art style",
        "abstract": "high-end abstract digital art style",
        "nature": "serene nature-inspired digital art style",
        "retro": "stylized retro-futuristic digital art style",
        "anime": "polished anime-inspired digital art style",
    }

    CHARACTER_MAP = {
        "anime_warrior": "a powerful anime-inspired warrior",
        "pirate_captain": "a confident pirate captain",
        "saiyan_inspired": "a fierce energy-driven warrior inspired by classic anime aesthetics",
        "shinobi": "a stealthy shinobi warrior",
        "superhero": "a bold original superhero figure",
        "samurai": "a disciplined samurai warrior",
        "cyber_ninja": "a futuristic cyber ninja",
        "wizard": "a mysterious arcane wizard",
    }

    DEVICE_MAP = {
        "desktop": (
            "Landscape orientation, balanced composition, and sufficient negative "
            "space for desktop icons."
        ),
        "mobile": (
            "Portrait orientation, with space for a lock screen clock and widgets, "
            "keeping the main subject centered or in the lower third."
        ),
        "tablet": (
            "Balanced composition optimized for tablet viewing with clean visual spacing."
        ),
    }

    def build(self, data: dict[str, Any]) -> str:
        sections = [
            self._build_base(data),
            self._build_mood(data),
            self._build_style(data),
            self._build_color_palette(data),
            self._build_character(data),
            self._build_quote(data),
            self._build_device(data),
            self._build_quality(),
        ]
        return " ".join(section for section in sections if section).strip()

    def _build_base(self, data: dict[str, Any]) -> str:
        title = (data.get("title") or "").strip()
        if title:
            return f'Create a premium wallpaper inspired by "{title}".'
        return "Create a premium AI-generated wallpaper."

    def _build_mood(self, data: dict[str, Any]) -> str:
        mood = data.get("mood")
        description = self.MOOD_MAP.get(mood)
        if not description:
            return ""
        return f"Use {description}."

    def _build_style(self, data: dict[str, Any]) -> str:
        style = data.get("style")
        description = self.STYLE_MAP.get(style)
        if not description:
            return ""
        return f"Render it in a {description}."

    def _build_color_palette(self, data: dict[str, Any]) -> str:
        color_palette = (data.get("color_palette") or "").strip()
        if not color_palette:
            return ""
        return (
            f"Use a refined color palette centered around {color_palette}, with subtle "
            f"gradients, modern contrast, and cinematic lighting."
        )

    def _build_character(self, data: dict[str, Any]) -> str:
        character = data.get("character")
        if not character:
            return ""
        description = self.CHARACTER_MAP.get(character)
        if not description:
            return ""
        return f"Feature {description} as the central visual subject."

    def _build_quote(self, data: dict[str, Any]) -> str:
        quote = (data.get("quote") or "").strip()
        if not quote:
            return ""
        return (
            f'Include the quote "{quote}" using elegant typography that feels integrated '
            f"into the composition without overwhelming the artwork."
        )

    def _build_device(self, data: dict[str, Any]) -> str:
        device = data.get("device")
        description = self.DEVICE_MAP.get(device)
        if not description:
            return ""
        return f"{description} Maintain a wallpaper-friendly layout with professional composition."

    def _build_quality(self) -> str:
        return (
            "Premium digital artwork, highly detailed, visually polished, high resolution, "
            "cinematic lighting, wallpaper-specific composition, and 4K-quality output."
        )