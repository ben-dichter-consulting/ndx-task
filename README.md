# ndx-task Extension for NWB:N


## python

### Installation
```bash
pip install git+https://github.com/catalystneuro/ndx-task.git
```

### Usage

```
Task parameters:
    name (:py:class:`~str`): the name of this container
    description (:py:class:`~str`): describe the task
    category (:py:class:`~str`): free category field
    auditory (:py:class:`~bool`): experiment involves auditory stimuli
    visual (:py:class:`~bool`): experiment involves visual stimuli
    decision (:py:class:`~bool`): experiment involves decision making
    navigation (:py:class:`~bool`): experiment involves a navigation task
    rest (:py:class:`~bool`): experiment involves no task or stimuli
    motor (:py:class:`~bool`): experiment involves a fine motor task
    olfactory (:py:class:`~bool`): experiment involves olfactory stimuli
    speech production (:py:class:`~bool`): experiment involves speaking
    speech perception (:py:class:`~bool`): experiment involves listening to speech
```


```python
from ndx_task import Task, Tasks

from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime

task1 = Task(name='rest', description='animal is resting', rest=True)
task2 = Task(
    name='theta_maze',
    description='animal is doing an figure-8 task in the theta maze',
    navigation=True)

tasks = Tasks(name='tasks', tasks=[task1, task2])

session_start_time = datetime.now().astimezone()
nwb = NWBFile('session_description', 'identifier', session_start_time)

nwb.add_lab_meta_data(tasks)
```
