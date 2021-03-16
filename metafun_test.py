import inspect
import pkgutil
import importlib

import metafun  # Our module to reflect


def magic(root_module, superclasses=None):
    for mod in pkgutil.walk_packages(root_module.__path__, f"{root_module.__name__}."):
        if not mod.ispkg:  # All packages are modules, but not all modules are packages
            for name, cls in inspect.getmembers(importlib.import_module(mod.name), inspect.isclass):
                if not (superclasses is None):
                    if issubclass(cls, superclasses):  # Filter for subclasses of certain parents
                        yield cls   # Yield class object
                else:
                    yield cls


if __name__ == '__main__':
    # Fetch list of classes in module
    classes = [cls for cls in magic(metafun)]

    # Instantiate each class once
    instantiated_objects = [cls() for cls in classes]

    # Call (__call__) each instantiated object
    for obj in instantiated_objects:
        obj()  # <=> obj.__call__()
