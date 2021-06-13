#!./venv37/bin/python3.7

# Kedro Tutorial
# testing and learning Kedro
# use Python 3.7  
# How to install python3.7 along with outher python versions inside Ubuntu
# https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
# Kedro works in Python =>35, < 3.8
# https://kedro.readthedocs.io/en/stable/02_get_started/03_hello_kedro.html

# in this script use venv37 
# which is the python virtual environment with python 3.7
#

#%%

from kedro.pipeline import node


#%%
# A node is a Kedro concept. 
# It is a wrapper for a Python function that names the inputs and outputs of that function. 
# It is the building block of a pipeline. 

# Prepare first node
def return_greeting():
    return "Hello"

node_return_greeting = node(func=return_greeting, inputs=None, outputs="my_salutation")
# MemoryDataSet

#%%
# Prepare second node
def join_statements(greeting):
    return f"{greeting} Kedro!"

node_join_statements = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

#%%
# A pipeline organises the dependencies and execution order of a collection of nodes, 
# and connects inputs and outputs while keeping your code modular. 
# The pipeline determines the node execution order by resolving dependencies and 
# does not necessarily run the nodes in the order in which they are passed in.

from kedro.pipeline import Pipeline

# Assemble nodes into a pipeline
pipeline = Pipeline([node_return_greeting, node_join_statements])


#%%
# A DataCatalog is a Kedro concept.
# It is the registry of all data sources that the project can use.
# It maps the names of node inputs and outputs as keys in a DataSet
# which is a Kedro class that can be specialised for different types of data storage. 
# Kedro uses a MemoryDataSet for data that is simply stored in-memory.

from kedro.io import DataCatalog, MemoryDataSet

# Prepare a data catalog
data_catalog = DataCatalog({"my_salutation": MemoryDataSet()})


#%%

"""Contents of hello_kedro.py"""
from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner


#%%
# Prepare a data catalog
data_catalog = DataCatalog({"my_salutation": MemoryDataSet()})

# Prepare first node
def return_greeting():
    return "Hello"

node_return_greeting = node(
    return_greeting, 
    inputs=None, 
    outputs="my_salutation")

#%%
# Prepare second node
def join_statements(greeting):
    return f"{greeting} Kedro!"

node_join_statements = node(
    join_statements, 
    inputs="my_salutation", 
    outputs="my_message"
)
#%%
# Assemble nodes into a pipeline
pipeline = Pipeline([node_return_greeting, node_join_statements])

#%%

# Create a runner to run the pipeline
runner = SequentialRunner()

#%%
# Run the pipeline
output = runner.run(pipeline, data_catalog)

print(output)
print(type(output))

#%%


