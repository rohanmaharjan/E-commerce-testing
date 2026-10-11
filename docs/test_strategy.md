# Test Strategy: Practice Software Testing

## 1. Objective
Verify that the shop's core customer flows (registration, login, search,
cart, checkout, account) work correctly across the UI, API, and database.

## 2. Scope
**In scope:** registration, login/logout, product browsing, search,
filters, product details, cart, checkout, order history, API endpoints
for these features, data integrity of saved orders.

**Out of scope:** [FILL: e.g. admin panel, load testing, penetration
testing, payment gateway internals]

## 3. Test levels and tools
| Level | Tool | Purpose |
|---|---|---|
| Manual | Spreadsheet | Exploratory and scripted cases, usability |
| API | pytest + requests | Business logic, status codes, auth |
| UI | Playwright (Python) | Key end-to-end journeys, regression |
| Database | SQL | Data integrity |
| CI | GitHub Actions | Run automated suites on every push |

## 4. Test design techniques used
Equivalence partitioning, boundary value analysis, decision tables,
error guessing, state-based testing.

## 5. Test environment
- Application: https://practicesoftwaretesting.com
- API: https://api.practicesoftwaretesting.com
- Browsers: Chrome (manual), Chromium/Firefox/WebKit (automation)
- Local Docker instance for DB validation: yes

## 6. Test data
Demo user abc@gmail.com, freshly registered users with unique emails,
sample products hammer.

## 7. Entry criteria (when testing can start)
- App and API reachable
- Test accounts available
- Test cases reviewed

## 8. Exit criteria (when testing is "done")
- All High-priority cases executed
- No open Critical/High bugs without a decision
- Automation suite passes in CI

## 9. Risks
Link to risk-analysis.md. [FILL: any risk specific to this project,
e.g. shared public site means other learners may change data]

## 10. Deliverables
Test cases, execution log, bug reports, automation code, CI pipeline.