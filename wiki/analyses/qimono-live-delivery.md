---
title: Qimono live delivery operating model
type: analysis
status: proposal
date: 2026-11-24
---

# One backlog, three views

Recommended first platform: GitHub Projects private project with a private delivery repository for confidential evidence, existing public wiki for sanitized research. Native roadmap, board, table and individually editable variable-length iterations fit the requested cadence. [Roadmap](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout), [iterations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields). GitHub roadmap is not a full critical-path scheduling engine. For true drag-reschedule dependencies and stakeholder-friendly Gantt use [ClickUp](https://clickup.com/pricing) with [custom sprint duration](https://help.clickup.com/hc/en-us/articles/7563115668759-Create-Sprints-with-a-custom-duration) and permission-controlled views. Linear has project-level [timeline](https://linear.app/docs/timeline) and regular [cycles](https://linear.app/docs/use-cycles); not first choice for variable-length task-level Gantt. Jira offers Scrum and Kanban; Premium Plans for cross-team dependencies ([plans](https://www.atlassian.com/software/jira/guides/more/jira-editions)). Microsoft [Planner premium](https://www.microsoft.com/en-us/microsoft-365/planner/microsoft-planner-business-plans-and-pricing) offers Gantt, sprints and dependencies; verify external tenant access. [OpenProject](https://www.openproject.org/pricing/) is self-hostable with Gantt and agile features; verify edition/maintenance cost. Choose GitHub initially; trial ClickUp with identical seed if stakeholders need richer Gantt. Do not maintain two authoritative backlogs.

## Twelve calendar-aligned sprints

Days 1–14 then 15–month end; February 2027 both 14 days. January starts with administrative scope on Jan 1, working kickoff Jan 4. Use unique month abbreviations to avoid March/May and January/June collisions. Capacity in working days, not calendar days, adjusted for holidays and part-time allocations.

| Sprint | Start | End inclusive | Goal | Acceptance targets |
|---|---|---|---|---|
| JAN-1 | 2027-01-01 | 2027-01-14 | Team and scope | Role agreements; ISMS scope; lab requirements |
| JAN-2 | 2027-01-15 | 2027-01-31 | Discovery | 10 interviews; risk register; model selection; request SpinQ quote |
| FEB-1 | 2027-02-01 | 2027-02-14 | Build foundations | Intake MVP; crypto inventory; classical baseline instance 1 |
| FEB-2 | 2027-02-15 | 2027-02-28 | Baseline gate | Second reference model; data flow; QPU spending decision |
| MAR-1 | 2027-03-01 | 2027-03-14 | Experiment setup | Pre-register benchmarks; collaborator availability; customs clearance decision |
| MAR-2 | 2027-03-15 | 2027-03-31 | Beta / lab gate | 10 beta testers target; conditional SpinQ acceptance; supplier reviews |
| APR-1 | 2027-04-01 | 2027-04-14 | Benchmark A | First repeated QPU trials; package signing threat model |
| APR-2 | 2027-04-15 | 2027-04-30 | Benchmark B | Compare accuracy/cost; 3 qualified prospects target; restore test |
| MAY-1 | 2027-05-01 | 2027-05-14 | Client validation | Design partner assessment; PQC evidence; incident exercise |
| MAY-2 | 2027-05-15 | 2027-05-31 | Evidence review | Second assessment target; Statement of Applicability; benchmark gate |
| JUN-1 | 2027-06-01 | 2027-06-14 | Audit readiness | Internal audit; independent scientific review; remediation |
| JUN-2 | 2027-06-15 | 2027-06-30 | Investor decision | Management review; 2 paid pilots target; go/no-go; next runway |

## Same work item, different lenses

Fields: title, owner, workstream, status, sprint, planned start/end, estimated hours, actual hours, dependencies (linked issues), budget allocation, actual cost, ISO clause/control, risk ID, evidence reference, acceptance criteria, reviewer, classification. Board statuses: Backlog, Ready, In progress, Blocked, Review, Done. Investor view shows approved sanitized progress, milestone risks and spend only. Keep customer data, risk details, security findings and credentials out of public wiki and investor views; use separate restricted project/repository rather than assuming a filtered view is access control.

Product owner prioritizes; ISO lead owns evidence process; cyber lead validates technical security; chemist validates chemistry; independent reviewer where necessary. Sprint review/demo and retro every closing date (meeting on nearest workday); monthly budget reconciliation. Definition of Done: tests/reproducibility, evidence link, reviewer acceptance, risk impact recorded, no secret leakage. ISO 27001:2022 workstream maps scope (4.3), risk treatment/SoA (6.1.3), documented information (7.5), monitoring (9.1), audit (9.2), management review (9.3), corrective action (10.2). Annex A controls selected by risk; not universal checklist. Certification only by independent body. 

Mermaid stays in [[analyses/qimono-venture-pilot]] as versioned baseline; live project becomes authoritative for actual dates. Export sanitized snapshot at each review. No live workspace or stakeholder access created yet.

## Setup checklist

1. Create private organization project; confirm organization/individual ownership and roles.
2. Add custom fields and 12 iterations with dates above.
3. Create roadmap grouped by workstream with sprint markers, board filtered to current iteration, ISO evidence table, investor-safe separate reporting view/project.
4. Import seed tasks manually or via authorized API; test permissions with sample stakeholder account.
5. Baseline budget and review rhythm; do not import secrets. 
