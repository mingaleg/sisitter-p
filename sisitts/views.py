from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from sisitts.forms import NewSisitForm
from sisitts.models import Sisit


def list_of_all_sisits(request):
    return render(
        request,
        'list_of_all_sisits.html',
        {
            'new_sisit_form': NewSisitForm(),
            'sisits': Sisit.objects.order_by('-timestamp'),
        },
    )


def list_of_user_sisits(request, username):
    user = get_object_or_404(User, username=username, )
    return render(
        request,
        'list_of_all_sisits.html',
        {
            'new_sisit_form': NewSisitForm(),
            'sisits': Sisit.objects.filter(author=user).order_by('-timestamp'),
        },
    )


@require_POST
@login_required
def new_sisit(request):
    form = NewSisitForm(request.POST)
    if form.is_valid():
        new_sisit = form.save(commit=False)
        new_sisit.author = request.user
        new_sisit.save()
        form.save_m2m()
        return redirect('/')
    else:
        return HttpResponseBadRequest


def like_it(request, sisit_id):
    redirect_to = request.GET.get('redirect_to', '/')
    sisit = get_object_or_404(Sisit, id=sisit_id)
    sisit.likes.add(request.user)
    return redirect(redirect_to)