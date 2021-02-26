import inspect
import pkgutil
import importlib

import metafun


def magic(root_module):
    objs = []
    for mod in pkgutil.walk_packages(root_module.__path__, f"{root_module.__name__}."):
        if not mod.ispkg:  # All packages are modules, but not all modules are packages
            objs.extend([cls() for name, cls in inspect.getmembers(importlib.import_module(mod.name), inspect.isclass)])
    return objs


if __name__ == '__main__':
    all_the_objects = magic(metafun)
    for o in all_the_objects:
        o()
