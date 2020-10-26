from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # Blog_API Application
    path('api/', include('blog_api.urls', namespace='blog_api')),

    # API schema and Documentation
    path('project/docs/', include_docs_urls(title='BlogAPI')),
    path('project/schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
