from django.urls import path
from . import views

urlpatterns = [
    path('items/',views.get_post_product),
    path('items/<int:Id>', views.get_update_delete),
    path('items_page/<int:PAGENO>/<int:SIZE>', views.pagination),
    ]