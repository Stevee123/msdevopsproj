from django.urls import re_path as url
from cards import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^card$',views.flashcardApi),
    url(r'^card/([0-9]+)$',views.flashcardApi)
]