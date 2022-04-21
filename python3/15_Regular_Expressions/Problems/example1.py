#!/usr/bin/python3

import re

rules = [
    "dev-ContractDetails-ContractRule",
    "dev-ContractDetails-NetsuiteRule",
    "dev-ContractDetails-RevisionRule",
    "dev-DeactivateRevisionsTrig-PostedSuccessfullyRule",
    "dev-FTMonitor-EventRule",
    "dev-Stats-StatusToStatRule",
    "dev-UpdateStatus-InvoiceStatusRule",
    "dev-UpdateStatus-StatusRule",
    "dev-ValidateTitles-PullEventRule"
]

ignore = ["UpdateStatus", "ContractDetails"]


expr = '|'.join(ignore)
result = filter(lambda x: not re.search(expr, x), rules)
for each in result:
    print(each)
