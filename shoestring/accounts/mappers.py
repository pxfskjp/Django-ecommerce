from nap import datamapper

from . import models


class UserMapper(datamapper.ModelDataMapper):

    class Meta:
        model = models.User
        fields = '__all__'
        exclude = ('is_staff', 'is_superuser', 'is_active', 'password',)
