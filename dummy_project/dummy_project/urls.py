from django.contrib import admin
from django.urls import path
# from django.conf.urls import patterns, url
from dummy_app.views import home, algo1, decision_tree, kn_algo, custom_kn_algorithm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('kn_classification/', kn_algo),
    path('decision_tree/', decision_tree),
    path('custom_kn_algorithm/', custom_kn_algorithm),
    path('$/kn_analysis_of_coordinates/', kn_algo),
    # path('custom_kn_algorithm/kn_analysis_of_coordinates/', kn_algo)
]
