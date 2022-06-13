
# https://www.youtube.com/watch?v=x97ChYDd12U

cd 220610_01_kedro_tutorial

pip3 install kedro kedro[pandas] kedro-viz 

python3 --version

kedro --version

kedro run --pipeline <name of the pipeline >

# pipeline
# nodes
# dataset

# pipeline connect nodes to datasets
# the pipeline represents the moving of the data
# to know where it is coming from to where is
# going to be stored

# the nodes are functions that receive data and output data
# and datasets is where we put the data that was processed 
# by the nodes
# and the pipeline is responsible for getting the data and sending
# it to where it is needed

cd 220610_01_kedro_tutorial

git clone https://github.com/tamsanh/kedro-introduction-tutorial.git

kedro run --pipeline <name of the pipeline >
./src/kit/pipeline.py
# kit stands for kedro introductory tutorial

# to run the kedro pipeline
kedro run --pipeline hello-world


