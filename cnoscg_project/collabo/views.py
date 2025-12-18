from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from collabo.models import User
from collabo.forms import UserForm
from django.shortcuts import render, get_object_or_404, redirect

from parlement.models import Direction, Division, Section
from personnel.models import Person


# --------------  Authentification -----------------

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'collabo/register.html', context)


def home(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_directeur:
                return redirect('directeur')
            elif user.is_president:
                return redirect('president')
            elif user.is_general:
                return redirect('general')

        else:
            messages.info(request, "Cet utilisateur n'existe pas")
    context = {'form': form}
    return render(request, 'collabo/login.html', context)


# -----------------------------------------------


def president(request):
    user = request.user
    directions = Direction.objects.all()
    total_direction = directions.count()
    divisions = Division.objects.all()
    total_division = divisions.count()
    sections = Section.objects.all()
    total_section = sections.count()
    persons = Person.objects.all().order_by('prenoms')
    total_person = persons.count()
    hommes = Person.objects.filter(sexe='Homme').order_by('prenoms')
    total_homme = hommes.count()
    femmes = Person.objects.filter(sexe='Femme').order_by('prenoms')
    total_femme = femmes.count()
    context = {
        'persons': persons, 'total_person': total_person,
        'total_homme': total_homme, 'total_femme': total_femme,
        'divisions': divisions, 'total_division': total_division,
        'directions': directions, 'total_direction': total_direction,
        'sections': sections, 'total_section': total_section,
        }

    return render(request, 'collabo/president.html', context)


def superviseur(request):
    user = request.user
    directions = Direction.objects.all()
    total_direction = directions.count()
    divisions = Division.objects.all()
    total_division = divisions.count()
    sections = Section.objects.all()
    total_section = sections.count()
    persons = Person.objects.all().order_by('prenoms')
    total_person = persons.count()
    hommes = Person.objects.filter(sexe='Homme').order_by('prenoms')
    total_homme = hommes.count()
    femmes = Person.objects.filter(sexe='Femme').order_by('prenoms')
    total_femme = femmes.count()
    context = {
        'persons': persons, 'total_person': total_person,
        'total_homme': total_homme, 'total_femme': total_femme,
        'divisions': divisions, 'total_division': total_division,
        'directions': directions, 'total_direction': total_direction,
        'sections': sections, 'total_section': total_section,
        }
    return render(request, 'collabo/directeur.html', context)


def focal(request):
    user = request.user
    directions = Direction.objects.all()
    total_direction = directions.count()
    divisions = Division.objects.all()
    total_division = divisions.count()
    sections = Section.objects.all()
    total_section = sections.count()
    persons = Person.objects.all().order_by('prenoms')
    total_person = persons.count()
    hommes = Person.objects.filter(sexe='Homme').order_by('prenoms')
    total_homme = hommes.count()
    femmes = Person.objects.filter(sexe='Femme').order_by('prenoms')
    total_femme = femmes.count()
    context = {
        'persons': persons, 'total_person': total_person,
        'total_homme': total_homme, 'total_femme': total_femme,
        'divisions': divisions, 'total_division': total_division,
        'directions': directions, 'total_direction': total_direction,
        'sections': sections, 'total_section': total_section,
        }
    return render(request, 'collabo/general.html', context)


# --------   Rédiriger l'utilisateur vers sa page de procedure --------------------

def logoutUser(request):
    logout(request)
    return redirect('home')


def user_list(request):
    users = User.objects.all().order_by('id')
    total_collaborateur = users.count()
    context = {'users': users, 'total_collaborateur': total_collaborateur, }
    return render(request, 'collabo/user_list.html', context)


def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    activite = user.activite_set.all()
    context = {'user': user, 'activite': activite, }
    return render(request, 'collabo/user_detail.html', context)


def user_steps(request):
    user = request.user
    username = User.objects.filter(username=user)
    return render(request, 'collabo/login.html', {'username': username})


# --------   Rédiriger l'utilisateur vers sa page de procedure --------------------

def redirect_after_login(request):
    # Logique pour déterminer les étapes assignées à l'utilisateur
    user = request.user
    etapes = User.objects.filter(username=user)

    # Si des étapes sont trouvées, redirigez vers la page correspondante
    if etapes.exists():
        return redirect('user_steps')

    # Sinon, redirigez vers la page d'accueil ou une page par défaut
    return redirect('home')
