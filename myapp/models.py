import uuid
from django.db import models
from enum import Enum
from myapp.utils import *

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


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TechFest(BaseModel):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField()
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
    description = models.TextField()
    rules = models.TextField()
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    stages = models.IntegerField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Events'
        verbose_name = 'Event'

    def __str__(self):
        return self.name



class Images(BaseModel):
    """ US : 11 """
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_images')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="event/images", null=True)

    class Meta:
        ordering = ('-created_at',)

class Videos(BaseModel):
    """ US : 11 """
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_videos')
    name = models.CharField(max_length=100)
    video = models.ImageField(upload_to="event/videos", null=True)

    class Meta:
        ordering = ('-created_at',)

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
    models.ImageField(upload_to="event/sponsors_images", null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sponsors'
        verbose_name = 'Sponsor'

    def __str__(self):
        return self.name


class StudentCouncilMembers(BaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50,choices=PositionType.get_choices())
    models.ImageField(upload_to="event/student_council_images", null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Council Members'
        verbose_name = 'Student Council'

    def __str__(self):
        return self.name

