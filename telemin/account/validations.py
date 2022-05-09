import logging
import os

logger = logging.getLogger(__name__)

# Max size file 3Mb
MAX_SIZE = 3145728
FILE_EXTENSIONS = ['.png', '.jpg', '.jpeg']


def validation_profile_image(instance, filename) -> str:
    if instance.avatar.size <= MAX_SIZE:
        file, extension = os.path.splitext(filename)
        if extension in FILE_EXTENSIONS:
            return os.path.join('users/{}/avatar/{}'.format(instance.user, filename))
    else:
        logger.error('The file size exceeds 3MB!')
