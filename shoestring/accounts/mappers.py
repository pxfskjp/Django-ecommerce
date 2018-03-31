from nap import mapper

from . import models


class UserMapper(mapper.ModelMapper):

    class Meta:
        model = models.User
        fields = '__all__'
        exclude = ('is_staff', 'is_superuser', 'is_active', 'password',)
