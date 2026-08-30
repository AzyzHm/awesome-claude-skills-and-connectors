import json

CATS = [
    ("ux-design", "UX Design", "Visual and interaction design, canvas tools, design tokens, icons, and brand systems."),
    ("system-design", "System Design", "Architecture, databases, cloud infrastructure, IaC, and security."),
    ("engineering", "Engineering", "Code quality, version control, testing, debugging, and sandboxed execution."),
    ("documentation", "Documentation", "Writing, diagramming, and knowledge management."),
    ("automation", "Automation", "Workflow orchestration, scheduling, browsing, and operational tooling."),
]

with open("data/skills.json") as f:
    skills = json.load(f)
with open("data/connectors.json") as f:
    connectors = json.load(f)


def by_cat(items, cat):
    return [i for i in items if i["cat"] == cat]


lines = []
lines.append("# Claude Skills & Connectors Directory")
lines.append("")
lines.append(
    f"A curated, categorized archive of {len(skills)} Claude Skills and {len(connectors)} "
    "MCP connectors, organized by domain so you can find the right tool for the job instead "
    "of scrolling through one long list."
)
lines.append("")
lines.append(
    "Browse it here as a table, or check out the **[interactive site](https://YOUR-USERNAME.github.io/YOUR-REPO/)** "
    "for search and filtering."
)
lines.append("")
lines.append("## Contents")
lines.append("")
lines.append("- [What's the difference between a Skill and a Connector?](#whats-the-difference-between-a-skill-and-a-connector)")
lines.append("- [Skills](#skills)")
for key, title, _ in CATS:
    lines.append(f"  - [{title}](#{key}-skills)")
lines.append("- [Connectors (MCP Servers)](#connectors-mcp-servers)")
for key, title, _ in CATS:
    lines.append(f"  - [{title}](#{key}-connectors)")
lines.append("- [Installing a Skill](#installing-a-skill)")
lines.append("- [Contributing](#contributing)")
lines.append("")
lines.append("## What's the difference between a Skill and a Connector?")
lines.append("")
lines.append(
    "A **Skill** is a modular instruction package (a `SKILL.md` file plus optional scripts) "
    "that teaches Claude a domain-specific procedure, style, or checklist, no external "
    "connection required."
)
lines.append("")
lines.append(
    "A **Connector** (MCP server) is a live integration that gives Claude a tool to actually "
    "reach outside the conversation: a database, a design canvas, a repo, a calendar."
)
lines.append("")
lines.append("Many workflows combine both, a skill teaches the *how*, a connector provides the *access*.")
lines.append("")

lines.append("## Skills")
lines.append("")
for key, title, blurb in CATS:
    items = by_cat(skills, key)
    lines.append(f"### {title} <a id=\"{key}-skills\"></a>")
    lines.append("")
    lines.append(f"_{blurb}_")
    lines.append("")
    lines.append("| Skill | What it does | Source |")
    lines.append("|---|---|---|")
    for it in sorted(items, key=lambda x: x["name"]):
        lines.append(f"| [`{it['name']}`]({it['link']}) | {it['desc']} | {it['source']} |")
    lines.append("")

lines.append("## Connectors (MCP Servers)")
lines.append("")
for key, title, blurb in CATS:
    items = by_cat(connectors, key)
    if not items:
        continue
    lines.append(f"### {title} <a id=\"{key}-connectors\"></a>")
    lines.append("")
    lines.append("| Connector | What it does | Transport |")
    lines.append("|---|---|---|")
    for it in sorted(items, key=lambda x: x["name"]):
        lines.append(f"| [{it['name']}]({it['link']}) | {it['desc']} | {it['transport']} |")
    lines.append("")

lines.append("## Installing a Skill")
lines.append("")
lines.append("- **Claude Code (CLI):** place the skill folder in `~/.claude/skills/` (global) or `.claude/skills/` (project-level), or install via the plugin marketplace with `/plugin marketplace add <repo>`.")
lines.append("- **Claude Desktop / Claude.ai:** upload the skill zip or folder containing `SKILL.md` in the custom skills settings panel.")
lines.append("- **Cursor / Codex / Gemini CLI:** copy the skill folder into `~/.codex/skills/`, `~/.cursor/skills/`, or use the `agent-skills-cli` installer.")
lines.append("")
lines.append("Two rules that trip people up: the instruction file must be named exactly `SKILL.md` (uppercase, lowercase silently fails on some engines), and folder names must be lowercase with hyphens (e.g. `frontend-design`).")
lines.append("")
lines.append("## Contributing")
lines.append("")
lines.append("Found a skill or connector that should be here? Add an entry to `data/skills.json` or `data/connectors.json` with a `name`, `cat` (one of `ux-design`, `system-design`, `engineering`, `documentation`, `automation`), `desc`, and `link`, then run:")
lines.append("")
lines.append("```bash")
lines.append("python3 scripts/generate_readme.py > README.md")
lines.append("```")
lines.append("")
lines.append("This keeps the README and the website in sync from a single source of truth.")
lines.append("")

print("\n".join(lines))
