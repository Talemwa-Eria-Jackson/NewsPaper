from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin   #to restrict users from accessing certain site pages when they are not logged in
from django.core.exceptions import PermissionDenied     #to restrict the users from editing and deleting posts that are made by other users

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):    #ListView returns an object called object_list which we can iterate over using a for loop and each iteration is called object 
    model = models.Article
    template_name = "article_list.html"
    login_url = "login"     #login_url is used with LoginRequiredMixin to redirect users trying to access pages they shouldnt access


class ArticleEditView(LoginRequiredMixin,UpdateView):
    model = models.Article
    template_name = "article_edit.html"
    fields = ("title", "body")
    login_url = "login"

    # function to restrict users from editing articles they didnt make. This works with the PermissionDenied module 
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"

    # function to restrict users from deleting articles they didnt make. This works with the PermissionDenied module 
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = "article_detail.html"
    login_url = "login"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = "article_new.html"
    # fields = ("title", "body", "author")
    fields = ("title", "body")
    login_url = "login" #where the user is redirected when they try to access this template when not logged in


# NB:: right now, anyone logged in user can create a post and set any author for that post, but we need to make it so that the logged in user can only be the author to that post. We first remove "author" from the list of fields and then make the below function of form_valid(). check below

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)