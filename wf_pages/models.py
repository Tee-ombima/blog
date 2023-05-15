from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock




class WfPageCollectionIndexPage(Page):
    intro = RichTextField(blank=True)
    parent_page_types = ["wf_pages.WfPageCollectionIndexPage","puput.BlogPage"]


    content_panels = Page.content_panels + [FieldPanel("intro")]

    subpage_types = ["wf_pages.WfPageCollection"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        collections = WfPageCollection.objects.all()
        context["collections"] = collections

        return context


class WfPageCollection(Page):
    panels = [FieldPanel("title")]

    parent_page_types = ["wf_pages.WfPageCollectionIndexPage","puput.BlogPage"]
    subpage_types = []

    context_object_name = "collection"


class WfPage(Page):
    parent_page_types = ["wf_pages.WfPageCollectionIndexPage","puput.BlogPage"]

    body = StreamField(
        [
            
            (
                "rich_text",
                blocks.RichTextBlock(
                    features=[
                        "bold",
                        "italic",
                        "ol",
                        "ul",
                        "hr",
                        "link",
                        "document-link",
                        "image",
                        "superscript",
                        "strikethrough",
                        "blockquote",
                    ]
                ),
            ),
            ("quote", blocks.BlockQuoteBlock()),
            
            ("image", ImageChooserBlock()),
            
        ]
        ,use_json_field=True,
    )
    body_migrated = models.TextField(
        help_text="Used only for content from old Drupal website.",
        null=True,
        blank=True,
    )
    collection = models.ForeignKey(
        WfPageCollection,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="pages",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("collection"),
    ]

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
