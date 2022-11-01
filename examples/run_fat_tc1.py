from run_fat_scripts import *

excel_to_csv('/testcases/', 'testcases/testdata')
run_K9Tax('/testcases/testdata')
verify_outcome_with_expected('textcases/expected.csv')



