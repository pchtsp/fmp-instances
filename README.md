# fmp-instances
python instance generator for Flight and Maintenance Planning problems.

## The simulator

The `data/simulation.py` file generates input data for an FMP problem based on a dictionary of configuration. An example configuration file is found in `package/params.py`, where a seed can be provided to control the randomness of the data generation.

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


## Examples

The file `scripts/example.py` contains some examples of functions that make use of the helper classes to load the data examples an visualize the results in tables.
