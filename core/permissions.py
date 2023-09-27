# from django.contrib.auth.models import User
# from rest_framework import permissions
# from core.models import Store, Product


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_permission(self, request, view):
#         # Permitir que todos os usuários criem novas lojas
#         if view.action == "create":
#             return True
#         # Permitir que os proprietários de lojas editem suas próprias lojas
#         if view.action in ["update", "partial_update", "destroy"]:
#             user = request.user
#             if hasattr(request.data, "get"):
#                 store_id = request.data.get("store", None)
#                 if store_id:
#                     store = Store.objects.get(id=store_id)
#                     return store.owner == user
#         return False


# class IsOwnerOfStoreOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of a store to edit it.
#     """

#     def has_permission(self, request, view):
#         # Permitir que todos os usuários listem lojas
#         if view.action == "list":
#             return True
#         # Permitir que os proprietários de lojas editem suas próprias lojas
#         if view.action in ["update", "partial_update", "destroy"]:
#             user = request.user
#             store_id = view.kwargs.get("pk", None)
#             if store_id:
#                 store = Store.objects.get(id=store_id)
#                 return store.owner == user
#         return False


# class IsOwnerOfProductOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of a product to edit it.
#     """

#     def has_permission(self, request, view):
#         # Permitir que todos os usuários listem produtos
#         if view.action == "list":
#             return True
#         # Permitir que os proprietários de produtos editem seus próprios produtos
#         if view.action in ["update", "partial_update", "destroy"]:
#             user = request.user
#             product_id = view.kwargs.get("pk", None)
#             if product_id:
#                 product = Product.objects.get(id=product_id)
#                 return product.store.owner == user
#         return False
