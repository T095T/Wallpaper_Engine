
from django.db import models
import uuid



class Mood(models.TextChoices):
    MOTIVATED = "motivated", "Motivated"
    CALM = "calm", "Calm"
    FOCUSED = "focused", "Focused"
    CODING = "coding", "Coding"
    STUDY = "study", "Study"
    GAMING = "gaming", "Gaming"


class Style(models.TextChoices):
    MINIMAL = "minimal", "Minimal"
    CYBERPUNK = "cyberpunk", "Cyberpunk"
    ABSTRACT = "abstract", "Abstract"
    NATURE = "nature", "Nature"
    RETRO = "retro", "Retro"
    ANIME = "anime", "Anime Inspired"


class Device(models.TextChoices):
    MOBILE = "mobile", "Mobile"
    DESKTOP = "desktop", "Desktop"
    TABLET = "tablet", "Tablet"


class Status(models.TextChoices):
    PENDING = "pending", "Pending"
    GENERATING = "generating", "Generating"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"

class CharacterType(models.TextChoices):
    ANIME_WARRIOR = "anime_warrior", "Anime Warrior"
    PIRATE_CAPTAIN = "pirate_captain", "Pirate Captain"
    SAIYAN_INSPIRED = "saiyan_inspired", "Saiyan Inspired"
    SHINOBI = "shinobi", "Shinobi"
    SUPERHERO = "superhero", "Superhero"
    SAMURAI = "samurai", "Samurai"
    CYBER_NINJA = "cyber_ninja", "Cyber Ninja"
    WIZARD = "wizard", "Wizard"


class Wallpaper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
       'accounts.User',
        on_delete=models.CASCADE,
        related_name="wallpapers",
    )

    title = models.CharField(
        max_length=100,
        blank=True,
    )

   

    mood = models.CharField(
        max_length=30,
        choices=Mood.choices,
    )

    style = models.CharField(
        max_length=30,
        choices=Style.choices,
    )

    color_palette = models.CharField(
        max_length=50,
    )

    device = models.CharField(
        max_length=20,
        choices=Device.choices,
    )

    quote = models.TextField(
        blank=True,
        null=True,
    )

    prompt = models.TextField(max_length=500)

    image = models.URLField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    generation_time_ms = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    download_count = models.PositiveIntegerField(
        default=0,
    )

    character = models.CharField(
        max_length=30,
        choices=CharacterType.choices,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Wallpaper"
        verbose_name_plural = "Wallpapers"

    def __str__(self):
        return self.title or f"Wallpaper #{self.pk}"