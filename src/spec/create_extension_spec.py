# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(doc='An NWB extension for tasks',
                                     name='ndx-task',
                                     version='0.2.0',
                                     author='Ben Dichter',
                                     contact='ben.dichter@catalystneuro.com')

    task = NWBGroupSpec(neurodata_type_def='Task', neurodata_type_inc='NWBDataInterface', doc='task information')
    task.add_attribute(name='description', doc='describe the task', dtype='text', required=True)
    task.add_attribute(name='category', doc='free category field', dtype='text', required=False)

    task.add_attribute(name='auditory', doc='experiment involves auditory stimuli', dtype='bool', required=False)
    task.add_attribute(name='visual', doc='experiment involves visual stimuli', dtype='bool', required=False)
    task.add_attribute(name='decision', doc='experiment involves decision making', dtype='bool', required=False)
    task.add_attribute(name='navigation', doc='experiment involves a navigation task', dtype='bool', required=False)
    task.add_attribute(name='rest', doc='experiment involves no task or stimuli', dtype='bool', required=False)
    task.add_attribute(name='motor', doc='experiment involves a fine motor task', dtype='bool', required=False)
    task.add_attribute(name='olfactory', doc='experiment involves olfactory stimuli', dtype='bool', required=False)
    task.add_attribute(name='speech production', doc='experiment involves speaking', dtype='bool', required=False)
    task.add_attribute(name='speech perception', doc='experiment involves ', dtype='bool', required=False)

    tasks = NWBGroupSpec(neurodata_type_def='Tasks', neurodata_type_inc='LabMetaData', doc='holds task objects')
    tasks.add_group(neurodata_type_inc='Tasks', quantity='*', doc='task information')

    new_data_types = [task, tasks]

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('LabMetaData', namespace='core')

    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
