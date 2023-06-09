from django.urls import path
from .views import *

urlpatterns = [
    path('task', task),
    path('move_working/<int:id>', move_working, name = 'move_working' ),
    path('move_to_done/<int:id>', move_to_done, name = 'move_to_done'),
    path('', user_login, name = 'login'),
    path('logout', log_out, name = 'log_out'),

]