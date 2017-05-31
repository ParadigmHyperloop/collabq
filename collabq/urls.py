"""collabq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core import views
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^q/(?P<pk>[-\w]+)$', views.QuestionView.as_view(), name='question'),
    url(r'^a/(?P<pk>[-\w]+)/edit$', views.EditAnswerView.as_view(), name='edit_answer'),
    url(r'^a/(?P<pk>[-\w]+)/history', views.AnswerHistoryView.as_view(), name='answer_history'),
    url(r'^admin/', admin.site.urls),
]
