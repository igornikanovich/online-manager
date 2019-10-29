def content_file_name(instance, filename):
    return '/'.join(['lecture', instance.theme, filename])


def content_file_answer(instance, filename):
    return '/'.join(['homework', instance.task.name, filename])
