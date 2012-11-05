from django.conf.urls.defaults import patterns, url, include

from crew import views

urlpatterns = patterns("",
    url(regex=r'^(?P<slug>[-\w]+)/$',
        view=views.CrewDetailView.as_view(),
        name='step_detail'),
)