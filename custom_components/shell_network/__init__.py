import logging
from homeassistant.core import HomeAssistant, ServiceCall
from .socket_client import send_command

_LOGGER = logging.getLogger(__name__)

DOMAIN = "shell_network"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Shell Network integration."""

    async def handle_send_command(call: ServiceCall):
        host = call.data.get("host")
        port = call.data.get("port", 26)
        command = call.data.get("command")

        result = await hass.async_add_executor_job(send_command, host, port, command)
        _LOGGER.info(result)

    hass.services.async_register(DOMAIN, "send_command", handle_send_command)
    return True
