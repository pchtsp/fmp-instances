import data.simulation as sim
import package.params as params
import package.instance as inst
import package.experiment as exp
import package.batch as ba
import pprint
import zipfile


def example_create_instance():

    # we use the params default data to create a dataset:
    model_data = sim.create_dataset(params.OPTIONS)

    # we print it:
    pprint.pprint(model_data)

    # we create an instance with that data:
    # we can build something that solves this instance.
    instance = inst.Instance(model_data)

    # we can show some of the data
    # for example, the start date for the tasks (missions):
    instance.get_tasks('start')

    # or the initial status of the resources (aircraft)
    instance.get_resources('initial')

    return instance


def load_experiment_from_zip():
    # we load the zip
    zipobj = zipfile.ZipFile('examples/serv_cluster1_20200625.zip')
    # we look for one experiment inside the zip
    experiment = exp.Experiment.from_zipfile(zipobj, 'serv_cluster1_20200625/numparalleltasks_13/202006250859')

    # we can, for example, check the solution for violation of constraints:
    pprint.pprint(experiment.check_solution())
    return experiment


def load_batch_from_zip():
    # we load the entire zip into a batch
    batch = ba.ZipBatch(path='examples/serv_cluster1_20200625.zip')

    # we can produce statistics from the batch:
    print(batch.get_status_df())

    return batch

