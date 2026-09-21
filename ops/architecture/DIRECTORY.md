# Workspace architecture

```
resume-web/                          # public career site + owner OS
  public/                            # hosted site
  Career/                            # evidence packets (preserve)
  Content/                           # media (preserve)
  Resumes & Cover Letters/           # application materials (preserve)
  ops/
    CONTROL-CENTER.md
    CONSTRUCTION-PHASES.md
    CONSTRUCTION-REPORT.md
    OPERATING-GUIDE.md
    profile/                         # intake
    architecture/                    # this file, sources of truth
    integrations/                    # inventory + routing
    capabilities/                    # AI directory
    product-engineering/             # product + engineering
    business-operations/             # ops and growth
    restricted/                      # labeled records; gitignored; not ACL
    owner/                           # oversight
    automations/
    templates/
    prompts/
    workflows/
    records/
  .cursor/                           # native rules, commands, skills, agents, hooks
  AGENTS.md
```

Owner oversight file: `ops/owner/OVERSIGHT.md`.  
Restricted policy: `ops/restricted/ACCESS.md`.
