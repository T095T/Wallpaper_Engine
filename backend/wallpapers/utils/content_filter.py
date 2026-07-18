from __future__ import annotations

import io

import PIL.Image
from django.conf import settings
from google import genai
from google.genai import types



def _get_client() -> genai.Client:
    return genai.Client(api_key=settings.GEMINI_API_KEY)

# banned keywords for prompt-level filtering
BANNED_KEYWORDS = [
    "nude", "naked", "nsfw", "explicit", "sexual",
    "porn", "hentai", "gore", "violence", "blood",
    "drug", "weapon", "hate", "racist",
]


def is_prompt_safe(prompt: str) -> tuple[bool, str | None]:
    """
    Layer 1 — keyword filter on user prompt.
    Returns (is_safe, error_message)
    """
    prompt_lower = prompt.lower()
    for keyword in BANNED_KEYWORDS:
        if keyword in prompt_lower:
            return False, f"Prompt contains inappropriate content: '{keyword}'"
    return True, None


def is_image_safe(image_bytes: bytes) -> tuple[bool, str | None]:
    """
    Layer 2 — Gemini vision check on generated image.
    Returns (is_safe, error_message)
    """
    try:
        image = PIL.Image.open(io.BytesIO(image_bytes))

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")

        with _get_client() as client:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    """Analyze this image strictly and answer the following:
                    1. Does it contain any NSFW or sexually explicit content?
                    2. Does it contain graphic violence or gore?
                    3. Does it contain hate symbols or offensive content?

                    Reply in this exact format:
                    SAFE: YES or NO
                    REASON: one line explanation
                    """,
                    types.Part.from_bytes(data=buffer.getvalue(), mime_type="image/png"),
                ],
            )

        text = response.text.upper()

        if "SAFE: NO" in text:
            # extract reason
            reason = "Image contains inappropriate content"
            for line in response.text.splitlines():
                if line.upper().startswith("REASON:"):
                    reason = line.split(":", 1)[-1].strip()
                    break
            return False, reason

        return True, None

    except Exception as e:
        print(f"Content filter error: {e}")
        return False, "Content safety check failed"