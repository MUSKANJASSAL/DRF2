from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # Viewset
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    # Function Based API View
    # path('article/', article_list),
    # path('detail/<int:pk>/', article_detail),
    #     Class Based API View
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    # Generic View
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]