from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# إضافة المسار داخل i18n_patterns
urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', include('custom_view.urls')),  # رابط التطبيق الخاص بك
)