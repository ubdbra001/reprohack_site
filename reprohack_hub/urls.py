from allauth.account.views import PasswordChangeView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .models import Event
from .views import (EventCreate, EventUpdate, EventDetail, EventList, IndexView,
                    PaperCreate, PaperUpdate, PaperDetail, PaperList,
                    ReviewCreate, ReviewDetail, ReviewUpdate, ReviewList,
                    UserDetailView, UserUpdateView, UserRedirectView, MarkdownView,
                    UserSearchEndpointView, PaperTagSearchEndpointView, UserEditRedirectView)


urlpatterns = [
    # User management
    path("accounts/", include("allauth.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('resources',
         MarkdownView.as_view(extra_context={'title': 'Resources',
                                             'markdown_file': 'resources.md'}),
         name='resources'),
    path('ways-to-reprohack',
         MarkdownView.as_view(extra_context={'title': 'Ways to ReproHack!',
                                             'markdown_file': 'ways-to-reprohack.md'}),
         name='ways-to-reprohack'),
    path('faq',
         MarkdownView.as_view(extra_context={'title': 'Frequently Asked Questions',
                                             'markdown_file': 'faq.md'}),
         name='faq'),
    path('participant_guidelines',
         MarkdownView.as_view(extra_context={'title': 'Participant Guidelines',
                                             'markdown_file': 'participant_guidelines.md'}),
         name='participant_guidelines'),
    path('organiser_guidelines',
         MarkdownView.as_view(extra_context={'title': 'Organiser Guidelines',
                                             'markdown_file': 'organiser_guidelines.md'}),
         name='organiser_guidelines'),
    path('author_guidelines',
         MarkdownView.as_view(extra_context={'title': 'Author Guidelines',
                                             'markdown_file': 'author_guidelines.md'}),
         name='author_guidelines'),
    path('code-of-conduct',
         MarkdownView.as_view(extra_context={'title': 'Code of Conduct',
                                             'markdown_file': 'code-of-conduct.md'}),
         name='code-of-conduct'),
    path('hackpad_template',
         MarkdownView.as_view(extra_context={'title': 'HackMD Hackpad Template',
                                             'markdown_file': 'templates/hackpad-hackmd-template.md'}),
         name='hackpad_template'),
    path('intro_slides_template',
         MarkdownView.as_view(extra_context={'title': 'HackMD Introductory Slides Template',
                                             'markdown_file': 'templates/intro-slides-hackmd-template.md'}),
         name='intro_slides_template'),
    path("user_redirect/", view=UserRedirectView.as_view(), name="user_redirect"),
    path("user_edit_redirect/", view=UserEditRedirectView.as_view(), name="user_edit_redirect"),
    path('users/<str:username>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<str:username>/edit/',
         UserUpdateView.as_view(), name='user_update'),
    path("user_search", view=UserSearchEndpointView.as_view()),
    path('', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='home'),
    path('event/', EventList.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('event/<int:pk>/edit/', EventUpdate.as_view(), name='event_edit'),
    path('event/new/', EventCreate.as_view(), name='event_new'),
    path('paper/', PaperList.as_view(), name='paper_list'),
    path('paper/<int:pk>/', PaperDetail.as_view(), name='paper_detail'),
    path('paper/<int:pk>/edit/', PaperUpdate.as_view(), name='paper_edit'),
    path('paper/new/', PaperCreate.as_view(), name='paper_new'),
    path('paper/tags_search/', PaperTagSearchEndpointView.as_view(),
         name='paper_tags_search'),
    path('review/', ReviewList.as_view(), name="review_list"),
    path('review/new', ReviewCreate.as_view(), name="review_new"),
    path('review/new/<int:paperid>', ReviewCreate.as_view(), name="review_new"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review_detail"),
    path('review/<int:pk>/edit/', ReviewUpdate.as_view(), name="review_edit"),
    url(r'^markdownx/', include('markdownx.urls')),
    path('about', TemplateView.as_view(
        template_name='about.html'), name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
