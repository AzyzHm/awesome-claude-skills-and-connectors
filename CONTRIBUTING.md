# Contributing

Thanks for wanting to add something to the archive. This repo works from two JSON files, so most contributions come down to editing one of them and running a script.

## Before you open a pull request

Check that the skill or connector is not already listed. Search `data/skills.json` or `data/connectors.json` for the name, or use the search box on the [live site](https://azyzhm.github.io/awesome-claude-skills-and-connectors/).

## Adding a skill

Open `data/skills.json` and add an entry in this shape:

```json
{
  "name": "your-skill-name",
  "cat": "ux-design",
  "desc": "One sentence describing what it does and how, no marketing language.",
  "source": "Name of the repo or library it comes from",
  "link": "https://github.com/owner/repo"
}
```

`cat` must be one of: `ux-design`, `system-design`, `engineering`, `documentation`, `automation`. If the skill genuinely spans two categories, pick the one it's most useful for.

## Adding a connector

Same idea, in `data/connectors.json`:

```json
{
  "name": "Your Connector Name",
  "cat": "engineering",
  "desc": "One sentence describing what it connects to and what it lets Claude do.",
  "transport": "Stdio / Node",
  "link": "https://github.com/owner/repo"
}
```

## Writing the description

- One sentence, stated plainly. Say what the tool does, not why it matters.
- No sales language: skip words like "seamless," "comprehensive," "robust," "powerful," or "cutting-edge" unless they're a real technical term (for example, a database's "primary key" stays as is).
- Link to the actual source repo or docs page, not a listicle or a blog post about the tool.

## Regenerating the README and the site

After editing either JSON file, run:

```bash
scripts/build_all.sh
```

This regenerates `README.md` and `docs/data.js` from the JSON so the README, the site, and the data never drift apart. Commit the regenerated files along with your JSON change, don't hand-edit `README.md` or `docs/data.js` directly, since those edits get overwritten the next time someone runs the script.

## Removing or flagging a broken entry

If a link is dead, a project looks abandoned, or something seems off about a listed connector, see [SECURITY.md](SECURITY.md) for how to report it. For a straightforward broken link, a pull request removing the entry (or fixing the URL) is fine too.

## Pull request checklist

- [ ] JSON is valid (run `python3 -m json.tool data/skills.json` or `data/connectors.json` to check)
- [ ] `scripts/build_all.sh` has been run and the regenerated files are included
- [ ] The link points to the actual source, and you've opened it to confirm it resolves
- [ ] The description has no em dashes and no filler language

## Code of conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). Participating means agreeing to keep to it.
