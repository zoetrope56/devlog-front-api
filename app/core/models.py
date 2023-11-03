from django.db import models

class TimestampedModel(models.Model):
    inp_dttm = models.DateTimeField(db_column='INP_DTTM', auto_now=True)  # Field name made lowercase.
    upd_dttm = models.DateTimeField(db_column='UPD_DTTM', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        ordering = ['-inp_dttm']
