from models import Commitment
from utilites import generate_time_blocks
from collections import defaultdict
from datetime import datetime, timedelta

def generate_weekly_schedule(user):
    """
    Generate a dict {day: [events]} for a user's commitments.
    Fill gaps with recommended tasks (Study, Meals, Rest).
    """

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {day: [] for day in days}
    
    # Pull user commitments
    fixed = Commitment.query.filter_by(user_id=user.id).all()

    # Organize commitments by day
    daily_blocks = defaultdict(list)
    for c in fixed:
        daily_blocks[c.day_of_week].append((c.start_time, c.end_time, c.title, c.category))

    # Build full day schedules
    for day in days:
        day_schedule = []
        current_time = datetime.strptime("06:00", "%H:%M")
        end_time = datetime.strptime("22:00", "%H:%M")
        
        # Sort commitments by start time
        events_today = sorted(daily_blocks[day], key=lambda x: x[0])
        
        for event in events_today:
            start, end, title, category = event
            start_dt = datetime.combine(datetime.today(), start)
            end_dt = datetime.combine(datetime.today(), end)
            
            # Fill free time before this event
            while current_time + timedelta(minutes=30) <= start_dt:
                day_schedule.append(('Open', current_time.time(), (current_time + timedelta(minutes=30)).time()))
                current_time += timedelta(minutes=30)

            # Add the event
            day_schedule.append((title, start, end, category))
            current_time = end_dt
        
        # Fill the remaining evening
        while current_time + timedelta(minutes=30) <= end_time:
            day_schedule.append(('Open', current_time.time(), (current_time + timedelta(minutes=30)).time()))
            current_time += timedelta(minutes=30)

        # Replace open blocks smartly
        smart_day_schedule = []
        for slot in day_schedule:
            if slot[0] == 'Open':
                # Recommend activities
                smart_day_schedule.append(('Study', slot[1], slot[2], 'Study'))
            else:
                smart_day_schedule.append(slot)
        
        schedule[day] = smart_day_schedule

    return schedule
