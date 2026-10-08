# KNOWN-DIVERGENCES.md

Every difference from the frozen reference must be recorded and classified.
Distinguish inherited upstream behaviour from a migration regression.

| ID | Route/component | Observed behaviour | Classification | Evidence | Approval/rationale | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Classification: inherited upstream / intentional migration difference /
unresolved / blocking.

A migration is not complete while any entry is unresolved or blocking.

| T3-AWS | AWS JSON table | Upstream displays “Please reload the page to see this table.” | inherited upstream | pinned static/json/privatelink_services_aws.json has 3 column labels but 2 cells per row; retained validator rejects it | Preserve observed reference rather than repair unrelated upstream data | Preserved by retained component |
| T3-DETAILS | Cloud SLO details | T3 native controller lacked upstream height animation | resolved migration difference | T5 established interaction matrices, 31 cases per project | T5 now retains the original animated Details component with static rich HTML children | Resolved; original component retained |
