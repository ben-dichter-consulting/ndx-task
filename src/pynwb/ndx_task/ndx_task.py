from os import path

from pynwb import load_namespaces, get_class


name = 'ndx-task'

# Set path of the namespace.yaml file to the expected install location
ndx_task_scheme_specpath = path.join(
    path.dirname(__file__),
    'spec',
    name + '.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not path.exists(ndx_task_scheme_specpath):
    ndx_task_scheme_specpath = path.abspath(path.join(
        path.dirname(__file__),
        '..', '..', '..',
        'spec',
        name + '.namespace.yaml'
    ))


load_namespaces(ndx_task_scheme_specpath)

Task = get_class('Task', name)
Tasks = get_class('Tasks', name)

