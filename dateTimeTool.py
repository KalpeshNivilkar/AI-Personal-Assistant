
from datetime import datetime
from zoneinfo import ZoneInfo
from agents import function_tool


def get_current_datetime():
    """Get current date and time in India."""
    # print("DATE-TIME TOOL EXECUTED!")
    current_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return current_time.strftime(
        "%A, %d %B %Y, %I:%M:%S %p IST"
    )


@function_tool
def date_time_tool() -> str:
    """Get the current date and time in India."""

    return get_current_datetime()



