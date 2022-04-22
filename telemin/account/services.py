from distutils.command.upload import upload
import os
from django.contrib import messages

# The maximum file size is 5Mb, the size is specified in bytes
# MAX_SIZE = 5242880
MAX_SIZE = 2303741



def user_photo_size_verify(instance, filename):
    """We check the size of the downloaded file and the extension."""
    file_size = instance.photo.size
    fname, extension = os.path.splitext(filename)

    if file_size <= MAX_SIZE and extension in ['.png', '.jpg', '.jpeg', '.gif']:
        upload = '{}/{}'.format(instance.user, filename)
    return upload
    # print(f'Instance: {instance.photo.size} | dir: {dir(instance)}')
    # messages.error(request, 'Размер файла не должен превышать 5Mb.')
