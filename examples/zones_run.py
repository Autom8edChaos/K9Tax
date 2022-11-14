from run_scripts import staging_zone_load, raw_zone_load, raw_zone_integrity, rule_zone_load, reporting_phase, run_steps
import sys

steps = [
    staging_zone_load,
    raw_zone_load,
    raw_zone_integrity,
    rule_zone_load,
    reporting_phase
]

run_steps(steps, sys.argv)
