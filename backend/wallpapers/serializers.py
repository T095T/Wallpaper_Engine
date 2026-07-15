from rest_framework import serializers
import re

from .models import CharacterType, Device, Mood, Status, Style, Wallpaper


class WallpaperGenerateSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    mood = serializers.ChoiceField(choices=Mood.choices)

    style = serializers.ChoiceField(choices=Style.choices)

    color_palette = serializers.CharField(max_length=50)

    device = serializers.ChoiceField(choices=Device.choices)

    quote = serializers.CharField(
        required=False,
        allow_blank=True
    )

    character = serializers.ChoiceField(
        choices=CharacterType.choices,
        required=False,
        allow_null=True
    )

    prompt = serializers.CharField(
        max_length=500
    )


    def validate_prompt(self, value):
        if not value.strip():
            raise serializers.ValidationError("Prompt cannot be empty.")
        elif len(value) > 500:
            raise serializers.ValidationError("Prompt cannot exceed 500 characters.")
        return value

    

def validate_color_palette(self, value):
    value = value.strip()
    if not value:
        raise serializers.ValidationError("Color palette cannot be empty.")
    if not re.fullmatch(r"[A-Za-z0-9,\\s#-]+", value):
        raise serializers.ValidationError("Enter valid color names or hex values.")
    return value


class WallpaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallpaper

        fields = [
            "id",
            "title",
            "mood",
            "style",
            "color_palette",
            "device",
            "character",
            "quote",
            "image",
            "status",
            "created_at",
        ]