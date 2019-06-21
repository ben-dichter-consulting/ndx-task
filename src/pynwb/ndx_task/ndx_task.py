import os
from pynwb import load_namespaces, get_class
from os import path

from pynwb.file import MultiContainerInterface
from pynwb import register_class
from pynwb.file import LabMetaData

name = 'ndx-task'

here = path.abspath(path.dirname(__file__))
ns_path = os.path.join(here, 'spec', name + '.namespace.yaml')

load_namespaces(ns_path)


Task = get_class('Task', name)


@register_class('Tasks', name)
class Tasks(MultiContainerInterface, LabMetaData):
    """
    Purpose:
        Topological graph representing connected components of a behavioral Environment.

    Arguments:
        name (str): name of this Environment
        tasks (list): list of Environment objects

    """

    __nwbfields__ = ('name', 'tasks')

    __clsconf__ = [{
        'attr': 'tasks',
        'type': Task,
        'add': 'add_task',
        'get': 'get_task'
        }, ]
    __help = 'container for tasks'

