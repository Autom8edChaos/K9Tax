from run_scripts import *
import sys


def run_steps(step_filter=None):
    steps = [
        staging_zone_load,
        raw_zone_load,
        raw_zone_integrity,
        rule_zone_load,
        reporting_phase
    ]

    startup()
    for i, step in enumerate(steps):
        if step_filter and str(i) not in step_filter: continue     
        print(f'\nstarting step #{i}, {step.__name__}')
        step()

if __name__ == "__main__":
    steps_filter = sys.argv[1].split(',') if len(sys.argv) > 1 else None
    run_steps(steps_filter)