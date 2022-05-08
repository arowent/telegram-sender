import os


def validation_profile_image(instance, filename) -> str:
    print('Instance: {} \nfile_name: {}'.format(instance, filename))
    file, expansion = os.path.splitext(filename)
    print(expansion)
    return os.path.join('users/{}/avatar/{}'.format(instance.user, filename))
