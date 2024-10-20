from django.shortcuts import get_object_or_404, render, redirect
from .models import Video

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video = request.FILES.get('video')  # Make sure the video file is received

        # Log to check if the file is received correctly
        if not video:
            print("No video file received.")
            return render(request, 'video.html', {'error': 'No video file uploaded'})

        print(f"Video received: {video.name}, Size: {video.size} bytes")

        # Save the video instance if both title and video are present
        if title and video:
            video_instance = Video(title=title, description=description, video=video)
            video_instance.save()
            return redirect('video')  # Redirect after saving

    return render(request, 'upload_video.html')

# def video(request):
#     videos = Video.objects.all()
#     return render(request, 'video.html', {'videos': videos})

# views.py
def video(request):
    sort_by = request.GET.get('sort', 'title')  # Default sort by title
    order = request.GET.get('order', 'asc')     # Default ascending order

    if order == 'desc':
        sort_by = f'-{sort_by}'

    # Retrieve sorted video list
    videos = Video.objects.all().order_by(sort_by)

    context = {
        'videos': videos,
        'current_sort': request.GET.get('sort', 'title'),
        'current_order': order,
    }
    return render(request, 'video.html', context)


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    other_videos = Video.objects.exclude(id=video_id)  
    return render(request, 'video_detail.html', {
        'video': video,
        'other_videos': other_videos
    })
