# from django.contrib.auth.models import User
# from django.db import models
#
# from meter.models import Indication
#
#
# class Accrued(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     accrued = models.SmallIntegerField()
#     created = models.DateField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created']
#
#     def __str__(self):
#         return self.user.username