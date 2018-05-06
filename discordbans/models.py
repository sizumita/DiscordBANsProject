from django.db import models

# Create your models here.


class Bans(models.Model):
    ban_datetime = models.DateTimeField()
    down_score = models.FloatField()
    receive_user_id = models.CharField(max_length=30)
    receive_user_name = models.CharField(max_length=30)
    perform_user_id = models.CharField(max_length=30)
    perform_user_name = models.CharField(max_length=30)
    ban_server_id = models.CharField(max_length=30)
    ban_server_name = models.CharField(max_length=30)
    ban_channel_id = models.CharField(max_length=30)
    ban_channel_name = models.CharField(max_length=30)
    reason = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bans'
