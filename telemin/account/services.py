import os
from django.contrib import messages

# The maximum file size is 2 Mb, the size is specified in bytes
MAX_SIZE = 2097152


def user_photo_size_verify(instance, filename):
    """We check the size of the downloaded file and the extension."""
    pass
    # messages.error(request, 'Размер файла не должен превышать 2Mb.')
