# Athlete Scheduler: Smart Time Management for Student-Athletes

## The Big Idea

### Main Idea

Student-athletes face unique challenges in managing their time effectively, balancing academics, athletics, personal care, and other obligations. Our project aims to build a personalized scheduling assistant that automates and optimizes a student-athlete’s weekly schedule. The scheduler will take into account fixed commitments like classes, practices, and lifts, while intelligently suggesting optimal time blocks for studying, meals, rest, and meetings.

### Minimum Viable Product (MVP)

- User inputs fixed time commitments and preferences.
- System suggests a weekly schedule filling in dynamic obligations like homework and studying.
- Output is displayed in a daily/weekly view with categorized time blocks.

### Stretch Goals

- Integrate with Google Calendar API to pull/push events.
- Add automated email/text reminders.
- Implement priority weighting for tasks based on deadlines.
- Support recurring task patterns and progress tracking.

---

## Learning Objectives

### Shared Goals

- Gain hands-on experience with full-stack Python development (Flask)
- Learn how to design, build, and iterate on a real-world scheduling engine
- Practice organizing and querying a database for user-specific content

### Individual Learning Goals

- Explore task optimization using Python (`pandas`, `datetime`, or `ortools`)
- Develop user-friendly interfaces using HTML
- Understand and work with API integration

---

## Implementation Plan

- **Backend**: Flask for routing and API endpoints
- **Database**: SQLite for easy local testing
- **Scheduler Logic**: Initially rule-based scheduling using `pandas` and `datetime`; may explore `ortools` for more complex constraint-solving
- **Frontend**: Jinja2 templates or optionally integrate `fullcalendar.js` for an interactive calendar UI
- **Visualization**: Time blocks color-coded by category (practice, study, sleep, etc.)
- **Reminder System**: Email reminders via Flask-Mail or external service (stretch)

> If unfamiliar with libraries, we will review documentation and existing tutorial projects to guide development.

---

## Project Schedule

| Week   | Goals                                                                 |
|--------|------------------------------------------------------------------------|
| Week 1 | Set up Flask app and database; build user profile & fixed schedule input form |
| Week 2 | Implement scheduling engine and generate weekly plan from user data   |
| Week 3 | Build visual interface for weekly/daily calendar view                 |
| Week 4 | Add task prioritization, reminders, and refine scheduler logic        |
| Week 5 | Final polish, user testing, documentation, and stretch goals if time allows |

---

## Collaboration Plan

We plan to follow an agile development structure with daily check-ins and weekly sprints. Tasks will be divided based on interest and strengths (e.g., one member focuses on frontend, another on scheduling logic). We will use:

- GitHub Projects or Issues to assign and track tasks
- Branch-based development with pull requests for merging
- Shared code reviews for continuous feedback

> If needed, we will rotate roles to ensure we both contribute across the stack.

---

## Risks and Limitations

- **Scheduling complexity**: Balancing fixed and flexible events without conflicts could be challenging
- **Time zone/calendar sync issues** (if Google Calendar is added)
- **Overfitting to niche use case**: We want to avoid making the app too tailored to a single user and instead support some generalizability for other busy students

> We’ll mitigate these risks by focusing on a well-scoped MVP and testing frequently with real schedules.

---

## Additional Course Content

We would benefit from additional guidance on:

- Scheduling/optimization algorithms (e.g., constraint satisfaction, task weighting)
- API integration
- Effective UX/UI design for user-friendly dashboards
