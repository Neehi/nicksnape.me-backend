from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    subpage_types = ["blog.BlogPostPage"]

    api_fields = [
        APIField("intro"),
    ]

    def get_posts(self):
        return BlogPostPage.objects.live().descendant_of(self).order_by("-date")

    def get_context(self, request):
        context = super().get_context(request)
        context["posts"] = self.get_posts()
        return context


class BlogPostPage(Page):
    date = models.DateField("Post date")
    excerpt = models.TextField(blank=True, max_length=500)
    body = RichTextField()
    categories = models.CharField(
        max_length=100,
        blank=True,
        help_text="Comma-separated categories (e.g. weight-loss, nutrition, coaching)",
    )

    search_fields = Page.search_fields + [
        index.SearchField("excerpt"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("excerpt"),
        FieldPanel("body"),
        FieldPanel("categories"),
    ]

    parent_page_types = ["blog.BlogIndexPage"]

    api_fields = [
        APIField("date"),
        APIField("excerpt"),
        APIField("body"),
        APIField("categories"),
    ]
