from collections import defaultdict
from datetime import datetime, timedelta, time
from models import Commitment

def generate_weekly_schedule(user):
    """
    Generate a dict {day: [events]} for a user's commitments.
    Include only time between 06:00 and 22:00 for each day.
    Add Sleep from 22:00 to 06:00 (shown as a final row for each day).
    Fill other time with Study blocks.
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {day: [] for day in days}
    
    # Get all user commitments
    fixed = Commitment.query.filter_by(user_id=user.id).all()
    daily_blocks = defaultdict(list)

    for c in fixed:
        # Ensure that start_time and end_time are datetime.time objects
        if isinstance(c.start_time, str):  # If the time is a string, convert it
            c.start_time = datetime.strptime(str(c.start_time), "%H:%M").time()
        if isinstance(c.end_time, str):
            c.end_time = datetime.strptime(str(c.end_time), "%H:%M").time()

        # Add commitment to the respective day of the week
        daily_blocks[c.day_of_week].append((c.start_time, c.end_time, c.title, c.category))

    for day in days:
        current_time = datetime.combine(datetime.today(), time(6, 0))  # Change to datetime object
        end_time = datetime.combine(datetime.today(), time(22, 0))  # Change to datetime object
        events_today = sorted(daily_blocks[day], key=lambda x: x[0])  # Sort events by start time
        day_schedule = []

        for start, end, title, category in events_today:
            # Convert start and end times to datetime objects
            event_start = max(datetime.combine(datetime.today(), start), current_time)
            event_end = min(datetime.combine(datetime.today(), end), end_time)

            # Ignore events fully outside of range
            if event_end <= current_time or event_start >= end_time:
                continue

            # Fill open time before event
            while current_time + timedelta(minutes=30) <= event_start:
                slot_end = current_time + timedelta(minutes=30)
                day_schedule.append(('Open', current_time.time(), slot_end.time()))
                current_time = slot_end

            # Add the actual event with correct category
            day_schedule.append((title, event_start.time(), event_end.time(), category))
            current_time = event_end

        # Fill any remaining time until 22:00
        while current_time + timedelta(minutes=30) <= end_time:
            slot_end = current_time + timedelta(minutes=30)
            day_schedule.append(('Open', current_time.time(), slot_end.time()))
            current_time = slot_end

        # Smart activity substitution (Study only)
        smart_schedule = []
        for title, start, end, *rest in day_schedule:
            if title == 'Open':
                smart_schedule.append(('Study', start, end, 'Study'))
            else:
                smart_schedule.append((title, start, end, *rest))

        # Add Sleep block at the end (Sleep from 22:00 to 06:00)
        smart_schedule.append(('Sleep', end_time.time(), time(6, 0), 'Sleep'))

        schedule[day] = smart_schedule

    return schedule

