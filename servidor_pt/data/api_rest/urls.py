from rest_framework.routers import DefaultRouter
from data.api_rest.views import *

router = DefaultRouter()
router.register('empleados', EmpleadoViewSet, basename='empleado')
router.register('email', EmailViewSet, basename='email')
router.register('telefono', TelefonoViewSet, basename='telefono')
router.register('cargo', CargoViewSet, basename='cargo')
router.register('departamento', DepartamentoViewSet, basename='departamento')


urlpatterns = router.urls
