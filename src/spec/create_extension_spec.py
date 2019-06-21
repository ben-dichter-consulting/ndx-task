from pynwb.spec import (
    NWBNamespaceBuilder,
    NWBGroupSpec,
    NWBAttributeSpec,
    NWBDatasetSpec,
    NWBLinkSpec
)
from export_spec import export_spec


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(doc='An NWB:N extension',
                                     name='ndx-task',
                                     version='0.1.0',
                                     author='Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb for more information

    task = NWBGroupSpec(neurodata_type_def='Task', neurodata_type_inc='NWBDataInterface', doc='task information')
    task.add_attribute(name='description', doc='describe the task', dtype='text', required=True)
    task.add_attribute(name='category', doc='free category field', dtype='text', required=False)
    task.add_attribute(name='help', doc='help', dtype='text', value='stores data about a specific task')

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
    tasks.add_attribute(name='help', doc='help', dtype='text', value='stores Task objects')

    new_data_types = [task, tasks]

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('LabMetaData', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
