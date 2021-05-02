from msgs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/messages', views.MessageViewSet)
#LLamo las urlpatterns para que esta ruta pueda estar disponible para usarla en el url global del proyecto
urlpatterns = router.urls
