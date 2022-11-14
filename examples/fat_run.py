from run_scripts import *

# Arrange: Prepare the data
excel_to_csv('/testcases/', 'testcases/testdata')

# Act: Run the application
run_K9Tax('/testcases/testdata')

# Assert: Verify the data
verify_outcome_with_expected('testcases/expected.csv')
