# importing the module
import json
import sys

PASSED = 0
FAILED = 0
SKIPPED = 0
BROKEN = 0
UNKNOWN = 0

dir1 = sys.argv[1]
file1 = '/history/history.json'

filename = dir1 + file1

# Opening JSON file
with open(filename) as json_file:
    data = json.load(json_file)
 
for key in data:
    PASSED += data[key]["statistic"]["passed"]
    FAILED += data[key]["statistic"]["failed"]
    SKIPPED += data[key]["statistic"]["skipped"]

print("******************************ONL Testcase execution statistics******************************")

print("PASSED  : {}".format(PASSED))
print("FAILED  : {}".format(FAILED))
print("SKIPPED : {}".format(SKIPPED))

