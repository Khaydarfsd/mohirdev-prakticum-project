from django.urls import path
from .views import news_list, news_detail, homePageView, HomePageView, ContactPageView, \
    get404View, aboutPageView, LocalNewsView, ForeignNewsView, TechnoNewsView, SportNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('techno/', TechnoNewsView.as_view(), name='techno_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('404/', get404View, name='404_page'),
    path('about/', aboutPageView, name='about_page'),
]