# Hi, I'm Aaditya 👋

BSc Computer Science graduate with a Management minor from **UBC**. I like building and shipping software where product decisions, system architecture, and implementation are tightly connected.

I work across full-stack systems, AI-enabled tooling, workflow automation, and applied software engineering. I especially enjoy taking messy manual processes and turning them into systems whose behaviour can be tested, understood, and improved.

I am drawn to fast-moving, entrepreneurial engineering environments where I can learn quickly, take ownership, and build things people actually use.


**Software engineering · Full-stack systems · System architecture · AI-enabled tooling · Automation**

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Aaditya-Golash&color=blueviolet&style=flat)

</div>

---

## 🚀 Featured Projects

### DealerSignal
**Angular 20 · TypeScript · Node.js · Express · Vitest · Firebase · Render**

A deployed dealership sales-intelligence prototype for prioritizing customer follow-up and detecting inventory-state exceptions.

DealerSignal answers two operational questions: **who should a salesperson contact next, and is the vehicle that customer asked about still actually available?**

Lead scoring runs on the backend using transparent business rules around financing intent, vehicle availability, trade-in interest, inquiry recency, and follow-up timing. The score represents current attention priority rather than purchase probability.

Salespeople can **Log Contact** from the Angular frontend. That sends a PATCH request to the Express API, updates the lead's contact state, recalculates scores, re-sorts the queue, and returns the refreshed results to the UI.

The system also models an inventory synchronization failure where a vehicle is marked sold internally but remains active in the modeled website state. The mismatch is deliberately seeded to demonstrate the workflow and is not a claim about a live August Luxury Motorcars listing.

Scoring and inventory-mismatch logic are centralized on the backend and covered with Vitest.

**Current boundary:** lead state is in memory, customer records are synthetic, and there is no live CRM/DMS integration, persistent database, authentication layer, or background job infrastructure. Scoring is deterministic and is not presented as machine learning.

[Live Demo →](https://dealersignal-14f5c.web.app/)  
[View Repo →](https://github.com/Aaditya-Golash/dealer-signal)

---

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

The MCP server keeps profile data in one source of truth, produces LaTeX resumes and cover letters, flags likely duplicate applications, and persists the tracker in a private Vercel Blob object.

Tests cover authentication, matching, deduplication, storage, templates, PDF integration, and repository contracts.

The plugin was assembled from four open-source job-search projects. Attribution and merge decisions are documented in `NOTICE.md` and `CONFLICTS.md`.

The integrated workflow adds a hard confirmation gate before any message is sent or form is submitted, and stops when it encounters a CAPTCHA.

**Current limitation:** the Blob write queue prevents lost updates inside one process, but the repository notes that a transactional database would be needed for high-write or multi-user use.

[View Repo →](https://github.com/Aaditya-Golash/JOB-HELPR)

---

### TA Allocation System
**Flask · MySQL · Docker · Nginx · Pytest · Vitest**

A six-person UBC capstone project for replacing spreadsheet-based TA allocation with role-specific workflows for students, instructors, coordinators, and administrators.

The system includes application and course management, CSV imports, assignment scheduling, role-based access control, notifications, audit records, reports, and containerized Flask/MySQL/Nginx services.

The repository contains more than 250 automated Python and JavaScript test cases covering backend routes, permissions, workflows, and browser-side behaviour.

The project processed workflows designed around hundreds of TA applications per term and placed **3rd overall at the UBC capstone showcase**.

[View Repo →](https://github.com/Aaditya-Golash/ta-allocation-system-capstone)

---

### Mongo Governance MCP Server
**TypeScript · Model Context Protocol · MongoDB · Jira · Docker**

A small, no-UI MCP server that runs read-side governance checks against MongoDB Atlas sample datasets.

Its tools inspect PII fields, stale records, orphaned accounts, collection volume, and other rule-based conditions. A separately configured Jira action can create a remediation task.

The server communicates over stdio and is packaged with Docker.

[View Repo →](https://github.com/Aaditya-Golash/mcp-mongo-sdlc-governance)

---

## 🔬 Other Technical Work

### Jersey Number Recognition
**Python · PyTorch · Computer Vision**

Team project implementing a ResNet18/34 clip classifier for 101 jersey-number labels, with a dataset wrapper, config-driven local and Colab training flows, and tests for label mapping and model output shape.

The repository includes a vendored SoccerNet package as an external dependency; the group-specific work lives in the configs, scripts, `src`, and `tests` directories.

[View Repo →](https://github.com/Aaditya-Golash/COSC-419-Group-9-Jersey-Number-Recognition)

### Eye-Tracking Research | Directed Studies
**Python · Linux · Tobii Pro Glasses 3 · Human-Computer Interaction**

Research work involving gaze, scene-camera, event, and IMU data from Tobii Pro Glasses 3 for HCI experiments.

Work included structuring multimodal sensor data, investigating IMU behaviour, event synchronization, and gaze-to-scene mapping.

The research repository and participant data are private.

---

## 🧠 Tech Stack

**Core languages**  
[![TypeScript](https://img.shields.io/badge/TypeScript-black?style=flat&logo=typescript)](https://github.com/Aaditya-Golash?tab=repositories&language=typescript)
[![JavaScript](https://img.shields.io/badge/JavaScript-black?style=flat&logo=javascript)](https://github.com/Aaditya-Golash?tab=repositories&language=javascript)
[![Python](https://img.shields.io/badge/Python-black?style=flat&logo=python)](https://github.com/Aaditya-Golash?tab=repositories&language=python)
[![SQL](https://img.shields.io/badge/SQL-black?style=flat&logo=mysql)](https://github.com/Aaditya-Golash?tab=repositories&language=sql)

**Application and backend development**  
Angular 20 · Node.js · Express · Next.js · Flask · REST APIs · MCP · Stripe

**Data and persistence**  
MySQL · MongoDB · Supabase · Firebase · Vercel Blob · JSON-backed pilot storage

**Testing and delivery**  
Pytest · Vitest · Node test runner · Docker · Git · GitHub Actions · Firebase Hosting · Render · Vercel

**AI-assisted engineering**  
Claude · ChatGPT · Gemini · AI-assisted coding, debugging, research, and development workflows

**Additional languages and systems**  
C · C++ · R · Bash · Linux

**Machine learning and research**  
PyTorch · Computer Vision · Eye Tracking · Human-Computer Interaction

---

## 🏗️ How I Like to Build

I am particularly interested in the boundary between **product decisions and system architecture**.

I like understanding where logic belongs, how data moves through a system, what should own state, and how an implementation changes as a prototype becomes a production service.

A pattern across several of my projects is:

```text
Understand the workflow
        ↓
Identify the source of truth
        ↓
Separate UI from business logic
        ↓
Build the smallest useful end-to-end loop
        ↓
Test the important rules
        ↓
Ship it
        ↓
Learn from the result
```

I also use AI tooling heavily throughout development, but I try to keep the architecture, trade-offs, and behaviour understandable rather than treating generated code as a black box.

---

## 📚 Relevant Coursework

- **Software systems:** operating systems, networking, databases, algorithms, and full-stack capstone delivery.
- **Software quality:** automated testing, Docker, CI/CD, accessibility, and team-based engineering.
- **AI and research:** artificial intelligence, deep learning, computer vision, HCI, and multimodal sensor data.
- **Business and product:** management, entrepreneurship, investments, and technology-focused project delivery.

---

## 👀 Currently

- Open to full-time **software engineering, full-stack, AI tooling, and startup engineering** opportunities.
- Building and shipping projects that combine software engineering with real operational workflows.
- Exploring how AI-assisted development changes the speed and scope at which small engineering teams can build.
- Continuing technical work around systems, automation, and applied AI.
- Particularly interested in fast-moving teams where engineers can own problems end to end.

---

## 🌎 A Little More About Me

I recently graduated from **UBC Okanagan** with a BSc in Computer Science and a Management minor.

I enjoy software engineering because it sits at the intersection of building, problem solving, systems thinking, and entrepreneurship. I am early in my career, but I learn quickly and like environments where the expectation is to move, figure things out, and ship.

Outside of software, I enjoy cars, travelling, cooking, working out, and learning languages.

And yes, if I had to pick one car:

**Mercedes-Benz 300 SL Gullwing. Preferably red.**

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
