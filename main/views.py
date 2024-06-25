from django.shortcuts import render
from .models import Slogan, YouTubeVideo, PopularProduct

def index(request):
    slogan = Slogan.objects.first()
    video = YouTubeVideo.objects.first()
    popular_products = PopularProduct.objects.order_by('-created_at')[:5]
    return render(request, 'main/index.html', {
        'slogan': slogan,
        'video': video,
        'popular_products': popular_products,
    })
