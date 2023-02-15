from rest_framework.routers import DefaultRouter
from ..account.views import AccountViewset, Input_OutputViewset

router = DefaultRouter ()

router.register(r'accounts', AccountViewset, basename='accounts')
router.register(r'inputend', Input_OutputViewset, basename='input_output')


urlpatterns = router.urls