# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from app.core.models import TimestampedModel


class Content(TimestampedModel):
    # Field name made lowercase.
    ctnt_no = models.AutoField(
        db_column='CTNT_NO', primary_key=True, db_comment='콘텐츠 번호')
    # Field name made lowercase.
    ctnt_title = models.CharField(
        db_column='CTNT_TITLE', max_length=100, blank=True, null=True, db_comment='콘텐츠 제목')
    # Field name made lowercase.
    ctnt_subtitle = models.CharField(
        db_column='CTNT_SUBTITLE', max_length=150, blank=True, null=True, db_comment='콘텐츠 소제목')
    # Field name made lowercase.
    inp_user = models.CharField(
        db_column='INP_USER', max_length=30, blank=True, null=True, db_comment='작성자')
    # inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시')  # Field name made lowercase.
    # upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contents_mst'
        db_table_comment = '컨텐츠 정보 테이블'


class ContentsDetail(Content):
    ctnt_dtl_no = models.OneToOneField(
        Content, on_delete=models.CASCADE, parent_link=True, related_name='ctnt_dtl_n', db_column='CTNT_NO', primary_key=True, db_comment='콘텐츠 번호')
    # Field name made lowercase.
    ctnt_dtl_title = models.CharField(
        db_column='CTNT_TITLE', max_length=100, blank=True, null=True, db_comment='콘텐츠 제목')
    # Field name made lowercase.
    ctnt_dtl_inp_user = models.CharField(
        db_column='INP_USER', max_length=30, blank=True, null=True, db_comment='작성자')
    # Field name made lowercase.
    ctnt_body = models.TextField(
        db_column='CTNT_BODY', max_length=5000, blank=True, null=True, db_comment='콘텐츠 내용')
    # Field name made lowercase.
    ctnt_path = models.CharField(
        db_column='CTNT_PATH', max_length=200, blank=True, null=True, db_comment='콘텐츠 파일 경로')
    # Field name made lowercase.
    ctnt_name = models.CharField(
        db_column='CTNT_NAME', max_length=200, blank=True, null=True, db_comment='콘텐츠 파일 이름')
    # Field name made lowercase.
    ctnt_ext = models.CharField(
        db_column='CTNT_EXT', max_length=200, blank=True, null=True, db_comment='콘텐츠 파일 확장자')
    # inp_user = models.CharField(db_column='INP_USER', max_length=30, blank=True, null=True, db_comment='생성자')  # Field name made lowercase.
    # inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시')  # Field name made lowercase.
    # upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contents_dtl'
        db_table_comment = '컨텐츠 상세정보 테이블'

    def save(self, *args, **kwargs):
        self.ctnt_dtl_title = self.ctnt_title
        self.ctnt_dtl_inp_user = self.inp_user
        self.ctnt_subtitle = self.ctnt_body[0:15]
        super().save(*args, **kwargs)

class File(TimestampedModel):
    # Field name made lowercase.
    file_no = models.AutoField(
        db_column='FILE_NO', primary_key=True, db_comment='콘텐츠 제목')
    # Field name made lowercase.
    file_path = models.CharField(
        db_column='FILE_PATH', max_length=200, blank=True, null=True, db_comment='파일 경로')
    # Field name made lowercase.
    file_name = models.CharField(
        db_column='FILE_NAME', max_length=200, blank=True, null=True, db_comment='파일 이름')
    # Field name made lowercase.
    file_ext = models.CharField(
        db_column='FILE_EXT', max_length=200, blank=True, null=True, db_comment='파일 확장자')
    # Field name made lowercase.
    ctnt_no = models.IntegerField(
        db_column='CTNT_NO', blank=True, null=True, db_comment='콘텐츠 번호')
    # inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시')  # Field name made lowercase.
    # upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'file_mst'
        db_table_comment = '컨텐츠 첨부파일 정보 테이블'


class Tag(TimestampedModel):
    # Field name made lowercase.
    tag_no = models.AutoField(
        db_column='TAG_NO', primary_key=True, db_comment='태그 번호')
    # Field name made lowercase.
    tag_name = models.CharField(
        db_column='TAG_NAME', max_length=15, blank=True, null=True, db_comment='태그 이름')
    # inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시')  # Field name made lowercase.
    # upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tags_mst'
        db_table_comment = '태그 정보 테이블'


class ContentsTag(Tag):
    # Field name made lowercase.
    content_tag_no = models.OneToOneField(
        Tag, on_delete=models.CASCADE, parent_link=True, db_column='TAG_NO', primary_key=True, db_comment='태그 번호')
    # Field name made lowercase.
    ctnt_no = models.IntegerField(
        db_column='CTNT_NO', blank=True, null=True, db_comment='콘텐츠 번호')
    # Field name made lowercase.
    sort = models.IntegerField(
        db_column='SORT', blank=True, null=True, db_comment='태그 정렬 순서')

    class Meta:
        managed = False
        db_table = 'contents_tags'
        db_table_comment = '컨텐츠 태그 정보 테이블'


class User(TimestampedModel):
    # Field name made lowercase.
    user_no = models.AutoField(
        db_column='USER_NO', primary_key=True, db_comment='유저번호')
    # Field name made lowercase.
    username = models.CharField(
        db_column='USERNAME', max_length=30, blank=True, null=True, db_comment='유저명')
    # Field name made lowercase.
    password = models.CharField(
        db_column='PASSWORD', max_length=100, blank=True, null=True, db_comment='비밀번호')
    # Field name made lowercase.
    grant = models.CharField(
        db_column='GRANT', max_length=10, blank=True, null=True, db_comment='사용자 권한')
    # inp_dttm = models.DateTimeField(db_column='INP_DTTM', blank=True, null=True, db_comment='입력일시')  # Field name made lowercase.
    # upd_dttm = models.DateTimeField(db_column='UPD_DTTM', blank=True, null=True, db_comment='수정일시')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_mst'
        db_table_comment = '사용자 정보 테이블'
