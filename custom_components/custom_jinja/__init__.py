from homeassistant.core import HomeAssistant
from homeassistant.helpers.template import TemplateEnvironment

# Define your custom Jinja function
def my_custom_function(value: str):
    return f"Processed: {value}"

# Register the function in Home Assistant
async def async_setup(hass: HomeAssistant, config: dict):
    env: TemplateEnvironment = hass.data.get("template_env")
    
    if env:
        env.globals["my_custom_function"] = my_custom_function

    return True  # Indicate successful setup