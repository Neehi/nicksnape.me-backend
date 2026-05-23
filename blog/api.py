from wagtail.api.v2.views import PagesAPIViewSet

from .models import BlogPostPage


class BlogPostPageAPIViewSet(PagesAPIViewSet):
    model = BlogPostPage

    def get_queryset(self):
        return BlogPostPage.objects.live().public().specific()
