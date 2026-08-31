## PROJECT DESCRIPTION
A QA learning project focused on testing an online shopping application across every layer a real QA engineer would touch: manual testing, UI automation, API testing, database validation, bug reporting, and CI/CD.

---

## PURPOSE
This project exists to test an online shopping application the way a real QA team would — not as five separate checklist items, but as connected layers that each catch bugs the others miss:
- **MAnual Testing** catches usability issues, layout bugs, and things a script wouldn't "notice" (a confusing checkout flow, a misleading error message)
- **UI automation(Playwright)** catches regressions — things that used to work and broke after a code change
- **API testing (pytest)** catches bugs at the business-logic level, before the UI even gets involved, and runs much faster
- **Database validation** catches the bugs where the UI looks correct but the wrong data got saved
- **Bug reports** communicate what's broken to developers in a way they can actually act on
- **CI/CD** makes sure these checks run automatically on every code change, instead of relying on someone remembering to run them

---

## TARGET APPLICATION
**Practic Software Testing** chosen beacus it mirrors a real-world stack:
- Frontend: Vue-based shopping UI (products, search, cart, checkout, auth)
- API: https://api.practicesoftwaretesting.com — genuine REST API with JWT auth
- Database: PostgreSQL backing the API, so DB validation checks are against real data

This separation (frontend / API / database) is exactly what this project's testing layers map onto.

---

# Project Scope & Deliverables

| Area | Deliverable |
| :--- | :--- |
| **Manual testing** | 50+ manual test cases (login, product search, cart, checkout) |
| **UI automation** | 15+ automated tests using Playwright |
| **API testing** | pytest-based tests against the REST API |
| **Database validation** | SQL-based checks confirming data integrity |
| **Bug reporting** | Structured bug reports for every defect found |
| **CI/CD** | GitHub Actions pipeline running the automated suite on every push |

---

## ARCHITECTURE
<p align="center">
  <img src="images\architecture.html" alt="Architecture" width="200" />
</p>

**Workflow**
The actual day-to-day process, in order:

- Understand the app — explore it like a real user before writing anything
- Design test cases — positive, negative, and edge cases
- Execute manually — log pass, fail, and bugs found
- Automate stable flows — Playwright (UI) + pytest (API), starting with the cases that are stable and repeated often
- Run in CI/CD — GitHub Actions runs the suite on every push
- Report bugs found — clear steps, evidence, severity

<p align="center">
  <img src="images\test.html" alt="Logo" width="200" />
</p>

---

**Tech stack**
- Manual testing: test case documents / spreadsheet (or a test case management tool)
- UI automation: Playwright
- API testing: pytest + requests
- Database validation: SQL queries against PostgreSQL
- CI/CD: GitHub Actions
- Bug tracking: GitHub Issues (or Jira-style bug report format)

---

## Repository structure
ecommerce-testing/
├── README.md
├── docs/
│   ├── architecture-diagram.png
│   └── workflow-diagram.png
├── manual-tests/
│   └── test-cases.xlsx (or .md)
├── automation/
│   ├── ui/            # Playwright tests
│   ├── api/            # pytest API tests
│   └── db/              # DB validation scripts
├── bug-reports/
│   └── BUG-001.md ...
└── .github/
    └── workflows/
        └── ci.yml