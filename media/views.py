import requests
from django.shortcuts import render
from django.conf import settings

def image_list(request):
    api_url = "https://api.unsplash.com/photos/random"
    client_id = "ICKEdSsx-bFIG_4AuXlu9uv-G477u9iT7ayiAs5qEZA"  # Replace with your Unsplash access key
    count = 31
    response = requests.get(api_url, params={'client_id': client_id, 'count': count})
    image_data = response.json()

    images = [
        {
            "title": image.get('description', 'No Title'),
            "url": image['urls']['regular']
        }
        for image in image_data
    ]

    return render(request, 'media/image_list.html', {'images': images})
