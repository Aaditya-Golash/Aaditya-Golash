# Hi, I'm Aaditya 👋

BSc Computer Science graduate with a Management minor from **UBC**. I build full-stack systems, AI-enabled tooling, and workflow automation. I like software that replaces messy manual processes with systems whose behaviour can be tested and understood.

**Software engineering · Full-stack systems · AI-enabled tooling · Automation**

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Aaditya-Golash&color=blueviolet&style=flat)

</div>

---

## 🚀 Featured Projects

### TheFlowrist
**Node.js · Supabase · Stripe · Docker · GitHub Actions**

A concierge MVP for milestone flower gifting, with customer and admin workflows for saved recipients, protected dates, memberships, one-time orders, scheduled orders, reminders, and manual fulfilment.

The application keeps JSON storage as the default pilot backend while exposing the same application logic through an optional Supabase adapter. Authentication is also selectable: lightweight pilot access for local use or Supabase Auth with secure, HttpOnly cookies. Internal automation endpoints are protected by a shared secret; charge execution and monthly order generation are idempotent.

Stripe Checkout captures payment methods and annual-plan fees, while off-session PaymentIntents handle scheduled charges. The code rejects non-test Stripe keys. Tests run in GitHub Actions, and the service includes health/readiness endpoints plus a Docker image.

**Pilot boundary:** JSON storage and pilot auth are local conveniences. Live payments are not enabled, public sign-up is not implemented, and the documented automation workflows still require an external scheduler.

[View Repo →](https://github.com/Aaditya-Golash/TheFlowrist)

---

### JOB-HELPR
**TypeScript · Next.js · MCP · Vercel Blob · Vitest**

A two-part job-search workflow: a Next.js MCP server for generating tailored documents and tracking applications, plus a Claude Code plugin for search, tailoring, outreach, and application steps.

The MCP server keeps profile data in one source of truth, produces LaTeX resumes and cover letters, flags likely duplicate applications, and persists the tracker in a private Vercel Blob object. Tests cover authentication, matching, deduplication, storage, templates, PDF integration, and repository contracts.

The plugin was assembled from four open-source job-search projects. Attribution and merge decisions are documented in NOTICE.md and CONFLICTS.md. The integrated workflow adds a hard confirmation gate before any message is sent or form is submitted, and stops when it encounters a CAPTCHA.

**Current limitation:** the Blob write queue prevents lost updates inside one process, but the repository notes that a transactional database would be needed for high-write or multi-user use.

[View Repo →](https://github.com/Aaditya-Golash/JOB-HELPR)

---

### TA Allocation System
**Flask · MySQL · Docker · Nginx · Pytest · Vitest**

A six-person UBC capstone project for replacing spreadsheet-based TA allocation with role-specific workflows for students, instructors, coordinators, and administrators.

The system includes application and course management, CSV imports, assignment scheduling, role-based access control, notifications, audit records, reports, and containerized Flask/MySQL/Nginx services. The repository contains more than 250 automated Python and JavaScript test cases covering backend routes, permissions, workflows, and browser-side behaviour.

[View Repo →](https://github.com/Aaditya-Golash/ta-allocation-system-capstone)

---

### Mongo Governance MCP Server
**TypeScript · Model Context Protocol · MongoDB · Jira · Docker**

A small, no-UI MCP server that runs read-side governance checks against MongoDB Atlas sample datasets. Its tools inspect PII fields, stale records, orphaned accounts, collection volume, and other rule-based conditions. A separately configured Jira action can create a remediation task. The server communicates over stdio and is packaged with Docker.

[View Repo →](https://github.com/Aaditya-Golash/mcp-mongo-sdlc-governance)

---

## 🔬 Other Technical Work

### Jersey Number Recognition
**Python · PyTorch · Computer Vision**

Team project implementing a ResNet18/34 clip classifier for 101 jersey-number labels, with a dataset wrapper, config-driven local and Colab training flows, and tests for label mapping and model output shape. The repository includes a vendored SoccerNet package as an external dependency; the group-specific work lives in the configs, scripts, src, and tests directories.

[View Repo →](https://github.com/Aaditya-Golash/COSC-419-Group-9-Jersey-Number-Recognition)

### Eye-Tracking Research | Directed Studies
**Python · Linux · Tobii Pro Glasses 3 · Human-Computer Interaction**

Ongoing work on collecting and structuring gaze, scene-camera, event, and IMU data for HCI experiments. The research repository and participant data are private.

---

## 🧠 Tech Stack

**Core languages**  
[![TypeScript](https://img.shields.io/badge/TypeScript-black?style=flat&logo=typescript)](https://github.com/Aaditya-Golash?tab=repositories&language=typescript)
[![JavaScript](https://img.shields.io/badge/JavaScript-black?style=flat&logo=javascript)](https://github.com/Aaditya-Golash?tab=repositories&language=javascript)
[![Python](https://img.shields.io/badge/Python-black?style=flat&logo=python)](https://github.com/Aaditya-Golash?tab=repositories&language=python)
[![SQL](https://img.shields.io/badge/SQL-black?style=flat&logo=mysql)](https://github.com/Aaditya-Golash?tab=repositories&language=sql)

**Application and backend development**  
Node.js · Flask · REST APIs · Stripe · Angular 20 (currently developing through DealerSignal)

**Data and persistence**  
MySQL · MongoDB · Supabase · Firebase · JSON-backed pilot storage

**Testing and delivery**  
Pytest · Vitest · Node test runner · Docker · Git · GitHub Actions · Vercel

**Additional languages and systems**  
C · C++ · R · Bash · Linux

**Machine learning and research**  
PyTorch · Computer Vision · Eye Tracking · Human-Computer Interaction

---

## 📚 Relevant Coursework

- **Software systems:** operating systems, networking, databases, algorithms, and full-stack capstone delivery.
- **Software quality:** automated testing, Docker, CI/CD, accessibility, and team-based engineering.
- **AI and research:** artificial intelligence, deep learning, computer vision, HCI, and multimodal sensor data.

---

## 👀 Currently

- Open to full-time software engineering roles and startup engineering teams.
- Building **DealerSignal**, an early Angular 20 and TypeScript learning project for experimenting with lead scoring and UI state. It is still in development.
- Continuing private eye-tracking research work at UBC.

---

## 🤝 Let's Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/aaditya-golash)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail)](mailto:aadigolash10@outlook.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/Aaditya-Golash)

---

<!-- TTT:START -->

### 🕹️ Live Community Tic-Tac-Toe
Your move! Click an empty cell to open a pre-filled GitHub Issue.

| | | |
| :---: | :---: | :---: |
| [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A0&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A1&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | **O** |
| [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A3&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A4&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | **X** |
| [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A6&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A7&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) | [Play](https://github.com/Aaditya-Golash/Aaditya-Golash/issues/new?title=play%3A8&body=Submit+this+issue+to+place+your+X+on+the+selected+Tic-Tac-Toe+cell.) |

_Recruiters and visitors play as **X**. The profile bot answers as **O** using minimax._
<!-- TTT:END -->
---

<div align="center">

**Built with ❤️ | Last Updated: 2026**

</div>
