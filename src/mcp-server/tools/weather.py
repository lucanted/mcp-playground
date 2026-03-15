from server import mcp
import requests

@mcp.tool()
def get_weather(city: str):
    """Get weather information for a city"""

    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()

    return data["current_condition"][0]["temp_C"]   # Info limitada
    # return data                                   # Info completa, que interprete el modelo

