from pathlib import Path
from palm.plugins.base import BasePlugin

MultiContainerPlugin = BasePlugin(name='multi_container', command_dir=Path(__file__).parent / 'commands')
