
OPTIONS = {
   'start': '2018-01'  # start of the planning horizon
    , 'num_period': 90  # size of the planning horizon
    # simulation params:
    , 'simulation': {
        'num_resources': 15  # this depends on the number of tasks actually
        , 'num_parallel_tasks': 1  # number of parallel missions
        , 'maint_duration': 6  # maintenance duration
        , 'max_used_time': 1000  # maintenance flight hours cycle
        , 'max_elapsed_time': 60  # max time without maintenance
        , 'elapsed_time_size': 15  # size of window to do next maintenance
        , 'min_usage_period': 0 # minimum consumption per period
        , 'perc_capacity': 0.15  # maintenance capacity as a percentage of the size of the fleet
        , 'min_avail_percent': 0.1  # min percentage of available aircraft per type
        , 'min_avail_value': 1  # min num of available aircraft per type
        , 'min_hours_perc': 0.5  # min percentage of maximum possible hours of fleet type
        , 'seed': 8002  # seed for random data generation (see below)
        # The following are fixed options, not arguments for the scenario:
        , 't_min_assign': [2, 3, 6]  # minimum assignment time for tasks
        , 'initial_unbalance': (-3, 3) # imbalance between rut and ret at the initial status
        , 't_required_hours': (10, 50, 100) # triangular distribution params for flight hours of each mission
        , 't_num_resource': (1, 6)  # range on the number of resources for each task
        , 't_duration': (6, 12)  # range on the duration of a task
        , 'perc_in_maint': 0.07  # percentage of resources in maintenance at the start of the horizon
        , 'perc_add_capacity': 0.1  # probability of having an added capacity to mission
    }

}

