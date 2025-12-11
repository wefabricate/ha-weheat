"""Constants for the Weheat integration."""

from logging import Logger, getLogger

DOMAIN = "weheat acceptance"
MANUFACTURER = "Weheat"
ENTRY_TITLE = "Weheat cloud"
ERROR_DESCRIPTION = "error_description"

OAUTH2_AUTHORIZE_WH = (
    "https://auth.acc.weheat.nl/auth/realms/Weheat/protocol/openid-connect/auth/"
)
OAUTH2_TOKEN_WH = (
    "https://auth.acc.weheat.nl/auth/realms/Weheat/protocol/openid-connect/token/"
)
API_URL_WH = "https://api.acc.weheat.nl/third_party"
OAUTH2_SCOPES = ["openid", "offline_access"]


LOG_UPDATE_INTERVAL = 120
ENERGY_UPDATE_INTERVAL = 1800

LOGGER: Logger = getLogger(__package__)

DISPLAY_PRECISION_WATTS = 0
DISPLAY_PRECISION_COP = 1
DISPLAY_PRECISION_WATER_TEMP = 1
DISPLAY_PRECISION_FLOW = 1
