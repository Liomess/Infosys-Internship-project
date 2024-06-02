from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet, CakeViewSet, CakeCustomizationViewSet, CartViewSet, AddCakeToCartViewSet, OrderViewSet ,
    AdminCustomerViewSet, AdminCakeViewSet, AdminCakeCustomizationViewSet, AdminOrderViewSet, AdminStoreViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cakes', CakeViewSet)
router.register(r'cake-customizations', CakeCustomizationViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'add-cake-to-cart', AddCakeToCartViewSet, basename='add-cake-to-cart')
# router.register(r'stores', StoreViewSet)



# Admin routers
router.register(r'admin/customers', AdminCustomerViewSet, basename='admin-customer')
router.register(r'admin/cakes', AdminCakeViewSet, basename='admin-cake')
router.register(r'admin/cake_customizations', AdminCakeCustomizationViewSet, basename='admin-cake_customization')
router.register(r'admin/orders', AdminOrderViewSet, basename='admin-order')
router.register(r'admin/stores', AdminStoreViewSet, basename='admin-store')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
