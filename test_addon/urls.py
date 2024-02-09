from django.urls import path, re_path

from .views import SimpleDetailView, SimpleListView, SimpleRootView, UntranslatedDetailView


app_name = 'simple'

urlpatterns = [
    re_path(r'^empty-view', SimpleRootView.as_view(), name='simple-root'),
    path('simple/', SimpleListView.as_view(), name='simple-list'),

    # NOTE: We are allowing access by slug and pk here.
    path('simple/<int:pk>/', SimpleDetailView.as_view(),
        name='simple-detail'),
    re_path(r'^simple/(?P<slug>\w[-\w]*)/$', SimpleDetailView.as_view(),
        name='simple-detail'),

    path('untranslated/<int:pk>/', UntranslatedDetailView.as_view(),
        name='untranslated-detail'),
    re_path(r'^untranslated/(?P<slug>\w[-\w]*)/$', UntranslatedDetailView.as_view(),
        name='untranslated-detail'),
]
