
from agents import function_tool

FAKE_WEATHER = {
    "mumbai": "31°C, humid, light rain",
    "london": "12°C, cloudy",
    "new york": "18°C, clear skies",
    "pune": "28°C, sunny",
}

@function_tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Args:
        city: Name of the city, for example London.
    """
    print(f"[TOOL CALLED] Weather for {city}")

    return FAKE_WEATHER.get(
        city.lower(),
        f"No weather data available for {city}."
    )
