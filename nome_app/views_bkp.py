from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import post
from .forms import postform

# # Create your views here.
# def main(request):
#   template = loader.get_template('home.html')
#   return HttpResponse(template.render())


# def main(request):
#   data = post.objects.all().values()
#   template = loader.get_template('home.html')
#   context = {
#     'data': data,
#   }
#   return HttpResponse(template.render(context, request))


def post_form(request, id=None):
    if id:
        instance = get_object_or_404(post, id=id)
    else:
        instance = None

    if request.method == 'POST':
        if 'delete' in request.POST:
            instance = get_object_or_404(post, id=request.POST.get('delete'))
            instance.delete()
            return redirect('home')

        form = postform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = postform(instance=instance)

    data = post.objects.all()
    return render(request, 'home.html', {'form': form, 'data': data})