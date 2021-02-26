import sys
import inspect
import pkgutil
import importlib

import metafun


def magic(module):
    l = []
    for pkg in pkgutil.walk_packages(module.__path__, f"{module.__name__}."):
        if not pkg.ispkg:
            importlib.import_module(pkg.name)
            for name, obj in inspect.getmembers(sys.modules[pkg.name], inspect.isclass):
                #print(f"{name = }   { obj = }")
                l.append(obj)

    [cls()() for cls in l]


if __name__ == '__main__':
    magic(metafun)
