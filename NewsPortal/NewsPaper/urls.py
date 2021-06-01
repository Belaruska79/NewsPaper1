from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from NewsPaper.models import Author


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Author.objects.all().order_by(full_name)[:20],
    template_name="news/author.html")),
]
