from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Status, Wallpaper
from .serializers import WallpaperGenerateSerializer, WallpaperSerializer
from .services.image_provider import generate_wallpaper
from .services.prompt_builder import PromptBuilder


class GenerateWallpaperView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WallpaperGenerateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            prompt = PromptBuilder().build(data)

            if len(prompt) > Wallpaper._meta.get_field('prompt').max_length:
                return Response(
                    {'error': 'Generated prompt is too long. Shorten the title, quote, or other inputs.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            wallpaper = Wallpaper.objects.create(
                user=request.user,
                title=data.get('title', ''),
                mood=data.get('mood', ''),
                style=data.get('style', ''),
                color_palette=data.get('color_palette', ''),
                character=data.get('character', ''),
                quote=data.get('quote', ''),
                device=data.get('device', 'desktop'),
                prompt=prompt,
                image='',
                status=Status.GENERATING,
            )

            image_url, error_message = generate_wallpaper(
                prompt=prompt,
                device=data.get('device', 'desktop')
            )

            if not image_url:
                wallpaper.status = Status.FAILED
                wallpaper.save(update_fields=['status', 'updated_at'])

                response_status = status.HTTP_400_BAD_REQUEST
                if not error_message or 'failed' in error_message.lower():
                    response_status = status.HTTP_503_SERVICE_UNAVAILABLE

                return Response(
                    {'error': error_message or 'Failed to generate wallpaper, please try again'},
                    status=response_status
                )

            wallpaper.image = image_url
            wallpaper.status = Status.COMPLETED
            wallpaper.save(update_fields=['image', 'status', 'updated_at'])

            return Response(
                WallpaperSerializer(wallpaper).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)