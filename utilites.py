from datetime import datetime, timedelta

def generate_time_blocks(start_hour=6, end_hour=22):
    """
    Generate 30-minute time blocks from start_hour to end_hour.
    """
    slots = []
    current = datetime(100,1,1,start_hour,0)
    end = datetime(100,1,1,end_hour,0)
    while current < end:
        slots.append(current.time())
        current += timedelta(minutes=30)
    return slots 
