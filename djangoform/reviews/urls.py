from django.urls import path
from . import views
app_name = 'reviews'
urlpatterns = [
    path('create',views.AddView.as_view(),name='home'),
    path('success',views.SuccessView.as_view(),name='success'),
    path('update/<int:pk>',views.EditView.as_view(),name='update'),
    path('display',views.DispView.as_view(),name='list'),
    path('details/<int:pk>',views.DataView.as_view(),name='details'),
    path('delete/<int:pk>',views.DropView.as_view(),name='delete')
    # path('<int:pk>',views.update)

]
