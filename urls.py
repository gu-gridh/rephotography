from django.urls import path, include
from rest_framework import routers
from . import views
import diana.utils as utils


router = routers.DefaultRouter()
endpoint = utils.build_app_endpoint("rephotography")
documentation = utils.build_app_api_documentation("rephotography", endpoint)

router.register(rf'{endpoint}/geojson/place', views.PlaceGeoViewSet, basename='place on geojson')
router.register(rf'{endpoint}/place', views.PlaceViewSet, basename='place')
router.register(rf'{endpoint}/image', views.IIIFImageViewSet, basename='image')
router.register(rf'{endpoint}/observation', views.ObservationViewSet, basename='observation')
router.register(rf'{endpoint}/geojson/focus', views.FocusGeoViewSet, basename='focus')
router.register(rf'{endpoint}/rephotography/focus', views.RephotographyFocusSearch, basename='rephotography focuses')
router.register(rf'{endpoint}/rephotography', views.RePhotographyViewSet, basename='rephotography')

router.register(rf'{endpoint}/search/tag', views.TagSearchViewSet, basename='search objects by tag')
router.register(rf'{endpoint}/search/type', views.TypeSearchViewSet, basename='search images by type')



urlpatterns = [
    path('', include(router.urls)),

    # Automatically generated views
    *utils.get_model_urls('rephotography', endpoint, 
        exclude=['image', 'place', 'focus', 'observation']),

    *utils.get_model_urls('rephotography', f'{endpoint}', exclude=['image', 'place', 'rephotography', 'focus', 'observation']),
    *documentation
]