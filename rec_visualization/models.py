# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Clip(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    sndlvl_id = models.IntegerField()
    language_id = models.IntegerField()
    producer_id = models.IntegerField()
    nation_id = models.IntegerField()
    primary_name = models.CharField(max_length=64)
    sub_name = models.CharField(max_length=64)
    caption_language = models.CharField(max_length=32)
    lead_player = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    abstract = models.CharField(max_length=256)
    story = models.CharField(max_length=2048)
    search_keys = models.CharField(max_length=128)
    update_time = models.DateTimeField()
    rec_level = models.IntegerField()
    english_name = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    svc_item_id = models.IntegerField()
    icp_id = models.IntegerField()
    status = models.IntegerField()
    series_count = models.IntegerField()
    total_duration = models.CharField(max_length=10)
    recom_first = models.IntegerField()
    publish_ym = models.CharField(max_length=8)
    series_id = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clip'


class ClipCount(models.Model):
    date = models.DateField()
    total = models.IntegerField()
    duration = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clip_count'


class ClipFile(models.Model):
    id = models.IntegerField(primary_key=True)
    clip_id = models.IntegerField()
    serial_no = models.IntegerField()
    icp_id = models.IntegerField()
    name = models.CharField(max_length=256)
    size = models.IntegerField()
    bit_rate = models.IntegerField()
    duration = models.IntegerField()
    upload_time = models.DateTimeField()
    copies = models.IntegerField()
    extension = models.CharField(max_length=4)
    protocol = models.CharField(max_length=8)
    media_type = models.IntegerField()
    status = models.IntegerField()
    play_ads = models.IntegerField()
    definition = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    is_hot = models.IntegerField()
    file_hash = models.CharField(max_length=32)
    syn_time = models.DateTimeField()
    pub_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clip_file'


class ClipFileCount(models.Model):
    date = models.DateField()
    total = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clip_file_count'


class ClipTag(models.Model):
    clip_id = models.IntegerField()
    tag_id = models.IntegerField()
    status = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clip_tag'


class Fstlvl(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.IntegerField()
    desc = models.CharField(max_length=256)
    icp_id = models.IntegerField()
    sub_flag = models.IntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fstlvl'


class FstlvlCount(models.Model):
    icp_id = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    fstlvl_id = models.IntegerField()
    total = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fstlvl_count'


class Icp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'icp'


class ImportList(models.Model):
    name = models.CharField(max_length=32)
    from_table = models.CharField(max_length=64)
    last_id = models.IntegerField()
    update_time = models.DateTimeField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'import_list'


class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=32)
    order = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'


class Nation(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.IntegerField()
    desc = models.CharField(max_length=64)
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nation'


class PackageItem(models.Model):
    status = models.IntegerField()
    package_item_id = models.IntegerField()
    item_id = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'package_item'


class Policy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    reg_time = models.DateTimeField()
    up_time = models.DateTimeField()
    status = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'policy'


class Producer(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.IntegerField()
    desc = models.CharField(max_length=128)
    dir = models.CharField(max_length=128)
    icp_id = models.IntegerField()
    p_id = models.IntegerField()
    logo = models.CharField(max_length=128)
    pic = models.CharField(max_length=128)
    bgpic = models.CharField(max_length=128)
    tvpic = models.CharField(max_length=128)
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'producer'


class Series(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    fstlvl_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    series_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'


class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()
    icp_id = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service'


class Service2Policy(models.Model):
    policy_id = models.IntegerField()
    service_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_2_policy'


class ServiceItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    icp_id = models.IntegerField()
    status = models.IntegerField()
    flag = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_item'


class ServiceServiceItem(models.Model):
    service_id = models.IntegerField()
    item_id = models.IntegerField()
    operation_type = models.CharField(max_length=2)
    status = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'service_service_item'


class Sndlvl(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.IntegerField()
    desc = models.CharField(max_length=256)
    fstlvl_id = models.IntegerField()
    icp_id = models.IntegerField()
    ex_fld = models.CharField(max_length=32)
    freenum = models.IntegerField()
    topic = models.CharField(max_length=256)
    big_pic = models.CharField(max_length=255)
    small_pic = models.CharField(max_length=255)
    intro = models.CharField(max_length=2048)
    tag = models.CharField(max_length=1024)
    create_time = models.DateTimeField()
    p_id = models.IntegerField()
    display = models.IntegerField()
    new_clip_id = models.IntegerField()
    new_file_id = models.IntegerField()
    new_clip_name = models.CharField(max_length=64)
    new_clip_update_time = models.DateTimeField()
    clip_count = models.IntegerField()
    contact_id = models.IntegerField()
    svc_item_id = models.IntegerField()
    total_num = models.IntegerField()
    play_time = models.CharField(max_length=50)
    director = models.CharField(max_length=128)
    player = models.CharField(max_length=128)
    release_date = models.DateTimeField()
    update_time = models.DateTimeField()
    series_id = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sndlvl'


class SndlvlEx(models.Model):
    sndlvl_id = models.IntegerField()
    series_id = models.IntegerField()
    status = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sndlvl_ex'


class SndlvlTag(models.Model):
    sndlvl_id = models.IntegerField()
    tag_id = models.IntegerField()
    status = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sndlvl_tag'


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    parent_id = models.IntegerField()
    fstlvl_id = models.IntegerField()
    syn_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tag'
