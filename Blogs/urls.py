from django.contrib import admin
from django.urls import path , include
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('myBlog.urls')),
    path('register/' , include('myBlog.urls')),
    path('user_login/' , include('myBlog.urls')),
    path('user_logout/' , include('myBlog.urls')),
    path("post_blog/", include('myBlog.urls')),
    path("blog_detail/<int:id>" , include('myBlog.urls')),
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


