from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from myweb_main.forms.post import PostForm
from myweb_main.forms.auth import AuthForm
from myweb_main.forms.reg import RegistrationForm
from .models import Post


def index(request):
    q_filter = Q(is_user=False)
    posts = Post.objects.filter(is_public=False).order_by("id").all()
    context = {
        "post": posts
    }
    return render(request, "myweb_main/index.html", context)


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'myweb_main/index_about.html'
    context_object_name = 'account'
    ordering = ('id')
    http_method_names = ['post',]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.all()
        return self.queryset.filter(is_public=True).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = "Супер Посты"
        context['user'] = self.request.user
        return context


def post_page(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("about")
        else:
            error = "Форма не верна"
    form = PostForm()
    context = {
         "form": form,
         "error": error
    }
    return render(request, 'myweb_main/post.html', context)


def about(request):
    posts = Post.objects.order_by('-id')
    return render(request, "myweb_main/index_about.html", {'title': 'Публикации', 'posts': posts})

def reg_page(request):
    error = ''
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма не верна"
    form = RegistrationForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'myweb_main/reg.html', context)

def auth(request):
    error = False
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request,user)
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
            error = True
    else:
        form = AuthForm()
    context = {"form": form, "error": error}
    return render(request, 'myweb_main/auth.html', context)


def logout_page(request):
    logout(request)
    return redirect('auth')