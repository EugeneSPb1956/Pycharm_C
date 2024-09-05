from django.shortcuts import render
from .models import Artists, Albums

# Create your views here.
def index(request):
    artists = list(Artists.objects.all())  #  Получаем QuerySet
    return render(request, 'index.html', context={'artists': artists,})
    #                                               # 'artist2': artists[1],})  # context={'artists': artists}

# def artist_view(request):
#     pass

def album_view(request, name):
    # albums = list(Albums.objects.all())  #  Получаем QuerySet using filter
    # artists = list(Artists.objects.all())  #  Получаем QuerySet
    name_id = Artists.objects.filter(name=name)
    name_id = name_id[0].id
    print(name_id)
    albums = Albums.objects.filter(artists_id=name_id)
    return render(request, 'album_view.html', context={'name': name, 'albums': albums,})

def tracks_view(request):
    pass
    # albums = list(Albums.objects.all())  #  Получаем QuerySet using filter
    # return render(request, 'index.html', context={'albums': albums,})
