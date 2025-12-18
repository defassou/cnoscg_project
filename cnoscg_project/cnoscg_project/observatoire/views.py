from django.shortcuts import render, get_object_or_404, redirect

from .forms import ObservateurForm
from .models import Observateur
from django.http import JsonResponse


def index(request):
    observateurs = Observateur.objects.all()
    context = {'observateurs':observateurs}
    return render(request, 'observateur/index.html', context)


def list_observateur(request):
    observateurs = Observateur.objects.all()
    context = {'observateurs':observateurs}
    return render(request, 'observateur/list_observateur.html', context)


def detail_observateur(request, pk):
    observateur = get_object_or_404(Observateur, id=pk)
    context = {
        'observateur': observateur, 'picture': observateur.picture,
        }
    return render(request, 'observateur/detail_observateur.html', context)


def add_observateur(request):
    if request.method == 'POST':
        form = ObservateurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ObservateurForm()
    return render(request, 'observateur/add_observateur.html', {'form': form})


def update_observateur(request, pk):
    observateur = Observateur.objects.get(id=pk)
    form = ObservateurForm(instance=observateur)
    if request.method == 'POST':
        form = ObservateurForm(request.POST, instance=observateur)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'observateur/update_observateur.html', context)


def delete_observateur(request, pk):
    observateur = Observateur.objects.get(id=pk)
    if request.method == 'POST':
        observateur.delete()
        return redirect('home')
    context = {'observateur': observateur}
    return render(request, 'observateur/delete_observateur.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        observateurs = Observateur.objects.all()
    else:
        observateurs = Observateur.objects.filter(telephone__icontains=query)
        if not observateurs.exists():
            observateurs = Observateur.objects.filter(telephone__icontains=query)
    title = "Résultats pour la requête %s" % query
    context = {'observateurs': observateurs, 'title': title}
    return render(request, 'observateur/search.html', context)


