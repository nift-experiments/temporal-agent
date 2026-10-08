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

| T6-VISUAL | Representative screenshots | Eleven final comparisons differ in 21 pixels by at most one channel level | rasterization noise | investigation/t6/t6-visual-comparison-v3.json | Geometry, token styles and recorded behavior identical; exact pixel identity not claimed | Classified; no functional/layout defect |
| T6-NAV-PRISM | Navigation and code highlighting | Draft ID collision, active Home link and missing language initialization | resolved migration regressions | T6 rejected/final screenshot and token audits | Restored pinned group boundaries/config/initializer without core changes | Resolved |
