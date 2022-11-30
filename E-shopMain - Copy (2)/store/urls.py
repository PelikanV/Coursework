from django.urls import path
from .views.home import Index , store, product_detail,cart
from .views.signup import signup
from store.views.login import Login , logout
from .views.checkout import CheckOut
from .views.orders import OrderView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', signup, name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', cart , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('product/<int:id>',product_detail,name="product_detail"),
    path('logout', logout , name='logout'),




]
