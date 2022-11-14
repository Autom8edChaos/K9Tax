from tqdm import tqdm
import random
import time
import traceback
import pprint
from datetime import datetime

def do_wait(msg, n_loops=10, wait_time=.1, stall=4, ascii=False):
    for i in tqdm(range(n_loops), desc=msg, ascii=ascii):
        if random.randint(0, stall) == 0: 
            time.sleep(wait_time * 5)
        time.sleep(wait_time)

def excel_to_csv(*args):
    print('Converting excel to csv')
    time.sleep(3)
        
def run_K9Tax(path):
    do_wait(f'starting K9Tax', 42, .01)
    do_wait(f'loading staging from {path}', 8, .5)
    do_wait(f'processing staging to raw zone', 12, .3)
    do_wait(f'checking raw zone integrity', 27, .05)
    do_wait(f'processing raw zone to rule zone', 23, .2)
    do_wait(f'generating reports for current period', 8, .5)

def verify_outcome_with_expected(path):
    print(f'Verifying data for current period with {path}')
    time.sleep(2)
    expected, actual = 33.09, 45.00
    message = 33.09, 45.00, f'Kwartaal bedrag voor 10000103: verwacht {expected} maar is {actual}'
    assert expected == actual, message
    print('ready')

def startup():
    do_wait(f'starting K9Tax', 42, .01)
        
def staging_zone_load():
    print('preparing data')
    do_wait(f'loading staging', 8, .5)
    do_wait(f'performing staging checks', 9, .1, ascii=True)

def raw_zone_load():
    print('preparing staging data')
    do_wait(f'loading raw zone', 12, .3)
    do_wait(f'performing raw zone checks', 5, .1, ascii=True)

def raw_zone_integrity():
    print('preparing raw data')
    do_wait(f'checking raw zone integrity', 27, .05)
    do_wait(f'outcome checks', 3, .1, ascii=True)

def rule_zone_load():
    print('preparing raw data')
    do_wait(f'loading rule zone', 23, .2)
    do_wait(f'performing rule checks', 12, .1, ascii=True)
    data_row = {
        'BSN': '10000103',
        'KwartaalBedrag': 45.0, 
        'Honden': 1,
        'TariefGroep': '4',
        'start_date': datetime.now(),
        'end_date': datetime(9999,12,31),
        'active': True
    }
    
    try:
        expected, actual = 33.09, 45.00
        message = 33.09, 45.00, f'Voor veld BSN=10000103: Kolom KwartaalBedrag,  {expected} != {actual}'
        assert expected == actual, message
    except AssertionError as e:
        print(f'\033[0;30;41mFailed check: {e}\033[0m')
        pprint.pprint(data_row)

def reporting_phase():
    print('preparing rule data')
    do_wait(f'generating reports for current period', 8, .5)
    do_wait(f'performing report checks', 9, .1, ascii=True)


def run_steps(steps: list, step_filter_list):
    step_filter = step_filter_list[1].split(',') if len(step_filter_list) > 1 else None
    
    startup()
    for i, step in enumerate(steps):
        if step_filter and str(i) not in step_filter: continue     
        print(f'\nstarting step #{i}, {step.__name__}')
        step()

