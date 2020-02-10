from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home),
    path('inventory/upload_item', views.upload_item),
    path('inventory/upload', views.upload),
    path('inventory/delete/<int:pk>', views.delete),
    path('inventory/update_form/<int:pk>', views.update_form),
    path('inventory/update_form/update/<int:pk>', views.update),
    path('search/',views.search),
    path("inventory/",views.admin_view,name='admin_view'),
    path("inventory/restricted/",views.admin_only,name='admin_only'),
    path('download/<int:pk>',views.download_image,name='download')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
