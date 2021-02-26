# cool fun with reflection in python

Small PoC-script to:
- recursively scan package(directory) for modules
- collect classes from all leaf modules (modules which aren't packages)
- create and call objects from all of these classes

HowTo: Create a new module (or module in a package) below the metafun package,
and the script will automagically create and call each object inside it