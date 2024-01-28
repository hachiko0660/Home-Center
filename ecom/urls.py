from django.urls import path
from .views import *

urlpatterns=[
    path('regi/',regi),
    path('log/',log),
    path('proj/',proj),
    path('pro/',profile),
    path('admnlog/',admnlog),
    path("admnupld/",admnupld),
    path('useredit/<int:id>',useredit),
    path('admnpge/',admnpge),
    path('admndsp/',admndsp),
    path('userdsp/',userdsp),
    path('uplodedit/<int:id>',uplodedit),
    path('uploddelete/<int:id>',uploddelete),
    path('sofa/',sofa),
    path('wishlist/<int:id>',wishlist),
    path('wishdelete/<int:id>',wishdelete),
    path('wishview/',wishview),
    path('cart/<int:id>',cart),
    path("cartview/",cartview),
    path("singleview/<int:id>",singleview),
    path('pay1/',pay1),
    path('confirm/',confirmdis),
    path('confirm1/',confirmdis1),
    path('first/',first),
    path('about/',about),
    path('cartdelete/<int:id>',cartdelete),
    path('reviewcom/',reviewcom),
    path('reviewdsp/',reviewdsp),
    path('forgot_password/',forgot_password),
    path('change/<int:id>', change_password),
    path('logout/',logout_view),
    path('empty/',empty),
    path('pay/',pay),
    path('success/',success),
    path('no/',no),


    path('ofrupld/',ofrupld),
    path('ofrdsp/',ofrdsp),
    path('ofrwish/<int:id>',ofrwish),
    path('wishofr/',wishofr),
    # path('delete/<int:id>',ofrwshdelete),
    # path('cart1/<int:id>',cart1),


]