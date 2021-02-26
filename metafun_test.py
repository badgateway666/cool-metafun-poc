import inspect
import pkgutil
import importlib

import metafun


def magic(module):
    for mod in pkgutil.walk_packages(module.__path__, f"{module.__name__}."):
        if not mod.ispkg:   # All packages are modules, but not all modules are packages
            imported_mod = importlib.import_module(mod.name)
            [cls()() for name, cls in inspect.getmembers(imported_mod, inspect.isclass)]


if __name__ == '__main__':
    magic(metafun)
