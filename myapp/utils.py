import os
from django.core.management.utils import get_random_string
from django.utils import timezone
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from tempfile import SpooledTemporaryFile

class CustomS3Boto3Storage(S3Boto3Storage):

    def _save_content(self, obj, content, parameters):
        """
        We create a clone of the content file as when this is passed to boto3 it wrongly closes
        the file upon upload where as the storage backend expects it to still be open
        """
        # Seek our content back to the start
        content.seek(0, os.SEEK_SET)

        # Create a temporary file that will write to disk after a specified size
        content_autoclose = SpooledTemporaryFile()

        # Write our original content into our copy that will be closed by boto3
        content_autoclose.write(content.read())

        # Upload the object which will auto close the content_autoclose instance
        super(
            CustomS3Boto3Storage,
            self)._save_content(
            obj,
            content_autoclose,
            parameters)

        # Cleanup if this is fixed upstream our duplicate should always close
        if not content_autoclose.closed:
            content_autoclose.close()


class StaticFileStorage(CustomS3Boto3Storage):
    default_acl = 'public-read'
    querystring_auth = False



def get_extension(filename):
    return f".{filename.split('.')[-1]}"


def get_random_name(filename):
    return f'{get_random_string()}-{int(timezone.now().timestamp() * 1000)}{get_extension(filename)}'


def handle_event_images(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/events/image/{instance.id.hex}/{get_random_name(filename)}"


def handle_event_videos(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/events/video/{instance.id.hex}/{get_random_name(filename)}"


def handle_student_coordinators_images(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/student_coordinators/image/{instance.id.hex}/{get_random_name(filename)}"


def handle_teacher_coordinators_images(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/teachers_coordinators/image/{instance.id.hex}/{get_random_name(filename)}"


def handle_speakers(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/speakers/image/{instance.id.hex}/{get_random_name(filename)}"


def handle_sponsors(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/sponsors/image/{instance.id.hex}/{get_random_name(filename)}"


def handle_student_council_members(instance, filename):
    return f"{settings.MEDIA_ENV}/techfest/student_council_members/image/{instance.id.hex}/{get_random_name(filename)}"

