#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 20
PREPARATION_TIME = 30

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    rem = EXPECTED_BAKE_TIME - elapsed_bake_time
    return rem


#TODO: Define the 'preparation_time_in_minutes()' function below.

def preparation_time_in_minutes(number_of_layers):
    return PREPARATION_TIME * number_of_layers


#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes():
    tot = prep_time + remaining_bake

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
