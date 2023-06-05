# from django.contrib.auth.mixins import AccessMixin
#
#
# import conftest
#
# class OwnerRequiredMixin(AccessMixin):
#
#     def dispatch(self, request, *args, **kwargs):
#         pets_profile = self.get_queryset().get(pk=kwargs.get('pk'))
#         if conftest.user != pets_profile.users:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)
