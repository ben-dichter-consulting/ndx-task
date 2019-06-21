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

with NWBHDF5IO('test_task.nwb', 'w') as io:
    io.write(nwb)

with NWBHDF5IO('test_task.nwb', 'r') as io:
    nwb2 = io.read()
    assert nwb.lab_meta_data['tasks']['rest'].rest
