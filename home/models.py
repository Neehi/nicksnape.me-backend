from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class HomePage(Page):
    intro = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    api_fields = [
        APIField("intro"),
    ]


class AboutPage(Page):
    intro = RichTextField(blank=True, default="")
    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("intro"),
        APIField("body"),
    ]
