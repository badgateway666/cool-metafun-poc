import inspect
import pkgutil
import importlib

import metafun  # Our module to reflect


def magic(root_module):
    for mod in pkgutil.walk_packages(root_module.__path__, f"{root_module.__name__}."):
        if not mod.ispkg:  # All packages are modules, but not all modules are packages
            for name, cls in inspect.getmembers(importlib.import_module(mod.name), inspect.isclass):
                yield cls()


if __name__ == '__main__':
    for o in magic(metafun):
        o()
