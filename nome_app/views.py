from django.shortcuts import render, redirect, get_object_or_404
from .models import post
from .forms import postform

def post_form(request, id=None):
    if id:
        instance = get_object_or_404(post, id=id)
    else:
        instance = None

    if request.method == 'POST':
        if 'delete' in request.POST:
            instance = get_object_or_404(post, id=request.POST.get('delete'))
            instance.delete()
            return redirect('home') #está nas rotas no arquivo de URL

        form = postform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')  #está nas rotas no arquivo de URL
    else:
        form = postform(instance=instance)

    data = post.objects.all()
    return render(request, 'home.html', {'form': form, 'data': data})
