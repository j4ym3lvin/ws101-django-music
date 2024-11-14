from django.template import loader
from django.http import HttpResponse
from .models import Music
from django.shortcuts import render, redirect
from .forms import MusicForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def musics(request):
    my_musics = Music.objects.all().values()
    template = loader.get_template('all_musics.html')
    context = {
        'my_musics':my_musics,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_musics = Music.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_musics' : my_musics
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

    return HttpResponse(template.render(context, request))

def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            # Process the form data
            music_id = form.cleaned_data['music_id']
            music_name = form.cleaned_data['music_name']
            music_artist = form.cleaned_data['music_artist']
            music_genre = form.cleaned_data['music_genre']
            music_link = form.cleaned_data['music_link']

            # Save the music instance
            Music.objects.create(
                music_id=music_id,
                music_name=music_name,
                music_artist=music_artist,
                music_genre=music_genre,
                music_link=music_link
            )
            return redirect('musics')  # Redirect after saving
        else:
            print(form.errors)  # Debugging line to check form errors
    else:
        form = MusicForm()

    context = {
        'form': form
    }
    return render(request, 'create_music.html', context)

def edit_music(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('musics')  # Redirect to the music list after saving
    else:
        form = MusicForm(instance=music)

    context = {
        'form': form,
        'music': music
    }
    return render(request, 'edit_music.html', context)

def delete_music(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        music.delete()
        return HttpResponseRedirect(reverse('musics'))  # Redirect to the music list after deletion
    return render(request, 'confirm_delete.html', {'music': music})

def play_music(request, id):
    print(f"Requested music ID: {id}")  # Debugging line
    music = get_object_or_404(Music, id=id)
    return render(request, 'play_music.html', {'music': music})
