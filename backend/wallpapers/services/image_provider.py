from __future__ import annotations

import os
import uuid

from django.conf import settings
from google import genai
from google.genai import types

from ..utils.content_filter import is_image_safe, is_prompt_safe


def _get_client() -> genai.Client:
    return genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_wallpaper(prompt: str, device: str = "desktop") -> tuple[str | None, str | None]:
    """
    Returns (image_url, error_message)
    """

    # Layer 1 — prompt keyword filter
    safe, error = is_prompt_safe(prompt)
    if not safe:
        return None, error

    try:
        with _get_client() as client:
            result = client.models.generate_images(
                model="imagen-3.0-generate-002",
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=_get_aspect_ratio(device),
                    safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
                    output_mime_type="image/png",
                    include_rai_reason=True,
                ),
            )

        if not result.generated_images:
            return None, "Failed to generate image"

        generated_image = result.generated_images[0]
        if not generated_image.image or not generated_image.image.image_bytes:
            return None, generated_image.rai_filtered_reason or "Failed to generate image"

        image_bytes = generated_image.image.image_bytes

        # Layer 2 — Gemini vision NSFW check on generated image
        safe, error = is_image_safe(image_bytes)
        if not safe:
            return None, error

        # all layers passed — save and return
        return _save_image(image_bytes), None

    except Exception as e:
        print(f"Error generating wallpaper: {e}")
        return None, "Failed to generate wallpaper, please try again"


def _get_aspect_ratio(device: str) -> str:
    return {
        "desktop": "16:9",
        "mobile": "9:16",
        "tablet": "4:3",
    }.get(device.lower(), "16:9")


def _save_image(image_bytes: bytes) -> str:
    filename = f"{uuid.uuid4()}.png"
    folder = os.path.join(settings.MEDIA_ROOT, "wallpapers")
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    return f"{settings.MEDIA_URL}wallpapers/{filename}"