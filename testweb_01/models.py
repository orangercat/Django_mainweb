from django.db import models
from django.core.files.storage import FileSystemStorage
import os
from news_web import settings

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        # Returns a filename that's free on the target storage system, and
        # available for new content to be written to.

        # Found at http://djangosnippets.org/snippets/976/

        # This file storage solves overwrite on upload problem. Another
        # proposed solution was to override the save method on the model
        # like so (from https://code.djangoproject.com/ticket/11663):

        # def save(self, *args, **kwargs):
        #     try:
        #         this = MyModelName.objects.get(id=self.id)
        #         if this.MyImageFieldName != self.MyImageFieldName:
        #             this.MyImageFieldName.delete()
        #     except: pass
        #     super(MyModelName, self).save(*args, **kwargs)
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# Create your models here.
class Project(models.Model):
    title = models.CharField('标题',max_length=200)
    summary = models.CharField('简介',max_length=200)
    content = models.TextField('正文',help_text="A content for this thing")

    BANNER_TYPE = (
        ('BANNER_LEFT', 'bnr_lft'),
        ('BANNER_RIGHT_GRID1', 'bnr_rht_grid1'),
        ('BANNER_RIGHT_GRID2', 'bnr_rht_grid2'),
        ('BANNER_RIGHT_GRID3', 'bnr_rht_grid3'),
        ('BANNER_RIGHT_GRID4', 'bnr_rht_grid4'),
        ('NONE','none'),
    )

    banner_type = models.CharField(
        '是否图片栏',
        max_length=200 ,
        choices=BANNER_TYPE,
        default='NONE',
    )

    #if banner_type == 'BANNER_LEFT':
    background_image = models.ImageField(storage=OverwriteStorage(),upload_to='images')
    #background_image.name = "bnr2.jpg"

    #else:
    #    print ("error")

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class New(models.Model):
    name = models.CharField('标题',max_length = 200)
    summary = models.CharField('简介',max_length=200)
    content = models.TextField('正文',help_text="A content for this thing")

    def __str__(self):
        return self.name



class Question(models.Model):
    label = models.CharField('question',max_length=50)

class Answer(models.Model):
    label = models.CharField('answer',max_length=50)
    question = models.ForeignKey(Question)
