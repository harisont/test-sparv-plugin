# from sparv import Config

from . import token

# __config__ = [
#     Config("examples.some_setting", "some_default_value", description="Description for this setting")
# ]

__description__ = "Example token-level Sparv plugins"

from . import sentence

__description__ = "Example sentence-level Sparv plugins"

from . import text

__description__ = "Example text-level Sparv plugins"
