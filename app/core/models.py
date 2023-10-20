from django.db import models

class TimestampedModel(models.Model):
    inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시', auto_now=True)  # Field name made lowercase.
    upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        ordering = ['upd_dttm', 'inp_dttm']

        