from django.contrib import admin
from django.urls import path
from dummy_app.views import home, algo1, decision_tree
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('kn_classification/', algo1),
    path('decision_tree/', decision_tree)
]
