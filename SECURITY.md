# Security policy

This repository is a curated list, most of the actual risk here is not in this repo's own code, it's in the third-party skills and connectors it links to. This document covers both.

## Reporting a suspicious or deprecated listing

Skills and MCP connectors run with real permissions: they can read files, call APIs, and in some cases execute code. A listing here is a pointer to a third-party project, not an endorsement that it's currently safe or maintained. If you find one that looks wrong, report it.

Report an entry if you notice any of the following:

- The linked repository has been deleted, archived, or transferred to an unrelated owner
- The project has been abandoned (no commits, no response to issues, for an extended period) and has known unpatched vulnerabilities
- The skill or connector asks for permissions or data access well beyond what its description implies
- The linked project was compromised, for example a maintainer account takeover or a malicious release
- The description in this repo no longer matches what the project actually does

To report one, open an issue with the label `flag-listing`, or use GitHub's private vulnerability reporting form on this repository if the issue involves an active exploit or credential exposure. Include:

- The name of the skill or connector as it appears in `data/skills.json` or `data/connectors.json`
- A link to the evidence (a GitHub issue, an archived repo notice, a security advisory)
- What you observed and when

We aim to review flagged listings within a few days. Depending on severity, the outcome is one of: removing the entry, marking it deprecated with a note, or updating the description and link.

## Reporting a vulnerability in this repository's own code

This repo's own code surface is small: a few Python build scripts and a static site (`docs/`) with no server-side component and no user data collection. If you still find a security issue in it, for example a script that could be tricked into writing outside its intended directory, or a site script that mishandles data unsafely, report it privately using GitHub's "Report a vulnerability" feature under the Security tab of this repository, rather than opening a public issue.

Please include steps to reproduce the issue and the potential impact. We'll acknowledge the report and follow up as we look into it.

## What this policy does not cover

We don't audit the source code of every listed skill or connector before adding it, and we can't guarantee any of them stay safe or maintained after being listed. Before installing anything from this archive, read its `SKILL.md` or server source, check who maintains it, and treat it the way you'd treat any third-party dependency.
