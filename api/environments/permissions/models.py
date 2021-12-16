from django.db import models

from environments.models import Environment
from environments.permissions.managers import EnvironmentPermissionManager
from permissions.models import AbstractBasePermissionModel, PermissionModel


class EnvironmentPermissionModel(PermissionModel):
    class Meta:
        proxy = True

    objects = EnvironmentPermissionManager()


class UserEnvironmentPermission(AbstractBasePermissionModel):
    user = models.ForeignKey("users.FFAdminUser", on_delete=models.CASCADE)
    environment = models.ForeignKey(
        Environment, on_delete=models.CASCADE, related_query_name="userpermission"
    )
    admin = models.BooleanField(default=False)

    class Meta:
        # hard code the table name after moving from the environments app to prevent
        # issues with production deployment due to multi server configuration.
        db_table = "environments_userenvironmentpermission"


class UserPermissionGroupEnvironmentPermission(AbstractBasePermissionModel):
    group = models.ForeignKey("users.UserPermissionGroup", on_delete=models.CASCADE)
    environment = models.ForeignKey(
        Environment, on_delete=models.CASCADE, related_query_name="grouppermission"
    )
    admin = models.BooleanField(default=False)

    class Meta:
        # hard code the table name after moving from the environments app to prevent
        # issues with production deployment due to multi server configuration.
        db_table = "environments_userpermissiongroupenvironmentpermission"
