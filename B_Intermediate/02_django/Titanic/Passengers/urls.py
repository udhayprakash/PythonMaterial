from django.urls import path

from passengers import views

urlpatterns = [
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
]