from home.views import home, account, user_login, sign_up, user_exit, ajax_login_check, ajax_email_check, \
    ajax_password_1_check, ajax_registration_login_check, basket, ajax_registration_password_check, add_in_basket, \
    basket_delete_product, admin_add_product, admin_delete_product, information_about_product, admin_edit_product, \
    ajax_delete_product, ajax_decrease_product_count
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home),
    path("user_login/", user_login),
    path("account/", account),
    path("sign_up/", sign_up),
    path("user_exit/", user_exit),
    path("ajax_login_check/", ajax_login_check),
    path("ajax_email_check/", ajax_email_check),
    path("ajax_password_1_check/", ajax_password_1_check),
    path("ajax_registration_login_check/", ajax_registration_login_check),
    path("ajax_registration_password_check/", ajax_registration_password_check),
    path("add_in_basked/<int:product_id>", add_in_basket),
    path("basket/", basket, name="basket"),
    path("basket_delete_product/<int:product_id>", basket_delete_product),
    path("admin_add_product/", admin_add_product),
    path("admin_delete_product/<int:product_id>", admin_delete_product),
    path("information_about_product/<int:product_id>", information_about_product),
    path("admin_edit_product/<int:product_id>", admin_edit_product),
    path("ajax_delete_product/<int:product_id>", ajax_delete_product),
    path("ajax_decrease_product_count/<int:product_id>", ajax_decrease_product_count),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
