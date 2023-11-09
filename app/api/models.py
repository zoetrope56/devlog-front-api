# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from app.core.models import TimestampedModel
from django_tuieditor.models import MarkdownField

class Content(TimestampedModel):
    # Field name made lowercase.
    ctnt_no = models.AutoField(db_column='CTNT_NO', primary_key=True)
    ctnt_title = models.CharField(db_column='CTNT_TITLE', max_length=100, blank=True, null=True)
    ctnt_subtitle = models.CharField(db_column='CTNT_SUBTITLE', max_length=400, blank=True, null=True)
    inp_user = models.CharField(db_column='INP_USER', max_length=30, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'contents_mst'
        # db_table_comment = '컨텐츠 정보 테이블'


class ContentsDetail(Content):
    # Field name made lowercase.
    ctnt_dtl_no = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, related_name='ctnt_mst', db_column='CTNT_NO', primary_key=True)
    ctnt_dtl_title = models.CharField(db_column='CTNT_TITLE', max_length=100, blank=True, null=True)
    ctnt_dtl_inp_user = models.CharField(db_column='INP_USER', max_length=300, blank=True, null=True)
    ctnt_body = MarkdownField(db_column='CTNT_BODY', blank=True, null=True) # db_column='CTNT_BODY', max_length=5000, blank=True, null=True, db_comment='콘텐츠 내용')
    ctnt_path = models.CharField(db_column='CTNT_PATH', max_length=200, blank=True, null=True)
    ctnt_name = models.CharField(db_column='CTNT_NAME', max_length=200, blank=True, null=True)
    ctnt_ext = models.CharField(db_column='CTNT_EXT', max_length=200, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'contents_dtl'
        # db_table_comment = '컨텐츠 상세정보 테이블'

    def save(self, *args, **kwargs):
        self.ctnt_dtl_title = self.ctnt_title
        self.ctnt_dtl_inp_user = self.inp_user
        self.ctnt_subtitle = self.ctnt_body[0:150].rstrip() + '...더보기...'
        super().save(*args, **kwargs)

class File(TimestampedModel):
    # Field name made lowercase.
    file_no = models.AutoField(db_column='FILE_NO', primary_key=True)
    file_path = models.CharField(db_column='FILE_PATH', max_length=200, blank=True, null=True)
    file_name = models.CharField(db_column='FILE_NAME', max_length=200, blank=True, null=True)
    file_ext = models.CharField(db_column='FILE_EXT', max_length=200, blank=True, null=True)
    ctnt_no = models.ForeignKey(Content, on_delete=models.CASCADE, db_column='CTNT_NO', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'file_mst'
        # db_table_comment = '컨텐츠 첨부파일 정보 테이블'


class Tag(TimestampedModel):
    # Field name made lowercase.
    tag_no = models.AutoField(db_column='TAG_NO', primary_key=True)
    tag_name = models.CharField(db_column='TAG_NAME', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags_mst'
        # db_table_comment = '태그 정보 테이블'

    def __str__(self):
        return self.tag_name


class ContentsTag(Tag):
    # Field name made lowercase.
    content_tag_no = models.OneToOneField(Tag, on_delete=models.CASCADE, parent_link=True, db_column='TAG_NO', primary_key=True, related_name='tags_set')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, db_column='CTNT_NO', related_name='tags')
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contents_tags'
        ordering = ['sort']
        # db_table_comment = '컨텐츠 태그 정보 테이블's


class User(TimestampedModel):
    # Field name made lowercase.
    user_no = models.AutoField(db_column='USER_NO', primary_key=True)
    username = models.CharField(db_column='USERNAME', max_length=30, blank=True, null=True)
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)
    grant = models.CharField(db_column='GRANT', max_length=10, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'user_mst'
        # db_table_comment = '사용자 정보 테이블'
