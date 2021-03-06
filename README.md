# fmp-instances

python instance generator for Flight and Maintenance Planning problems. This project is a part of the codebase used during the PhD of Franco Peschiera at ISAE-SUPAERO between 2017 and 2020. This thesis was partly financed by the DGA and Dassault Aviation.

## Installation

Some python dependencies are requires to use this project. The easiest is to create a python3 virtual environment and install 
them using pip:

```
cd fmp-instances
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## The simulator

The `data/simulation.py` file generates input data for an FMP problem based on a dictionary of configuration that is taken as input argument. An example configuration file is found in `package/params.py`, where a seed can be provided to control the randomness of the data generation.

## The helper classes

Are found in the `package` directory. Each file contains one class. Input data is handled in the `Instance` class, a solution is encoded in `Solution` and an `Experiment` is the combination of an instance and a solution. A `Batch` is a set of scenarios, each consisting on a set of experiments.

## The data examples

Are found in the `examples/` directory. Each zip represents a structured batch of experiments.

The structure of a batch is the following:

```
- batch.zip
    - batch
        - scenario1
        - scenario2
        - scenarioN
            - experiment1
            - experiment2
            - experimentN
                - Instance
                - Solution
                - Options
                - Log
```

Instances created under the same scenario share the same configuration and only change in the seed number and, as a consequence, in the random data.
Two scenarios differ in the configuration used to create the instance (usually the size of the instance).

Each experiment contains the following files:

1. `data_in.json`: data needed to create an Instance.
2. `data_out.json`: data needed to create a Solution.
3. `options.json`: the options used for generating and solving the instance.
4. `output.log` / `results.log`: the output log for the solution process.

## Code examples

The file `scripts/example.py` contains some examples of functions that make use of the helper classes to load the data examples an visualize the results in tables.

For example, the code to generate a new input data instance for the FMP problem with default options is:

```python
import data.simulation as sim
import package.params as params
import package.instance as inst
import pprint

# we use the params default data to create a dataset:
model_data = sim.create_dataset(params.OPTIONS)

# we create an instance with that data:
instance = inst.Instance(model_data)

# we can show some of the data
# for example, the start date for the tasks (missions):
instance.get_tasks('start')

# or the initial status of the resources (aircraft)
instance.get_resources('initial')

# the raw data of the instance (similar but with a different structure than the generated data):
pprint.pprint(instance.data)

# now, this instance needs to be solved by some method (not included here)...

```

Each helper class has several methods that are useful for debugging or querying the object for information. 