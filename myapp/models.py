from operator import truediv
from ckeditor_uploader.fields import RichTextUploadingField
from statistics import mode
import uuid
from django.db import models
from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]

    @classmethod
    def get_choices(cls):
        return tuple(x.value for x in cls)


class PositionType(ChoiceEnum):
    president = ('P', 'President')
    vicePresident = ('R', 'Vice President')
    secretary = ('S', 'Secretary')
    treasurer = ('T', 'Treasurer')
    joint_secretary = ('JS', 'Joint Secretary')
    joint_treasurer = ('JT', 'Joint Treasurer')
    coordinator = ('C', 'Coordinator')
    member = ('M', 'Member')


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TechFest(BaseModel):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    society_logo = models.ImageField(null=True)
    college_logo= models.ImageField(null=True)
    university_logo=models.ImageField(null=True)
    fest_image=models.ImageField(null=True)
    fest_video = models.FileField(null =True)
    start_date = models.DateField()
    end_date = models.DateField()
    email = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Tech Fest'
        verbose_name = 'Tech Fest'

    def __str__(self):
        return self.name

class Events(BaseModel):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = RichTextUploadingField(config_name='portal_config')
    rules = RichTextUploadingField(config_name='portal_config')
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    stages = models.IntegerField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_image = models.ImageField(upload_to="event/images", null=True)
    event_video = models.FileField(upload_to="event/videos", null=True)
    link =  models.TextField(null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Events'
        verbose_name = 'Event'

    def __str__(self):
        return self.name


class StudentCoordinators(BaseModel):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_student_coordinators')
    name = models.CharField(max_length=100)
    image =  models.ImageField(upload_to="event/student_coordinators_images", null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Coordinators'
        verbose_name = 'Student Coordinator'

    def __str__(self):
        return self.name


class TeacherCoordinators(BaseModel):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_teacher_coordinators')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,null=True)
    image= models.ImageField(upload_to="event/teacher_coordinator_images", null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Teacher Coordinators'
        verbose_name = 'Teacher Coordinator'

    def __str__(self):
        return self.name


class Speakers(BaseModel):
    name = models.CharField(max_length=100)
    image =  models.ImageField(upload_to="event/speakers_images", null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Speakers'
        verbose_name = 'Speaker'

    def __str__(self):
        return self.name


class Sponsors(BaseModel):
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to="event/sponsors_images", null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sponsors'
        verbose_name = 'Sponsor'

    def __str__(self):
        return self.name


class StudentCouncilMembers(BaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50,choices=PositionType.get_choices())
    image= models.ImageField(upload_to="event/student_council_images", null=True)
    is_design_team= models.BooleanField(default=False)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Council Members'
        verbose_name = 'Student Council'

    def __str__(self):
        return self.name

class EventsTimeLine(BaseModel):
    name = models.CharField(max_length=100, null=True)
    content = RichTextUploadingField(config_name='portal_config')
    class Meta:
        verbose_name_plural = 'Event TimeLine'
        verbose_name = 'Event TimeLine'

