# Python Inventory Reports

This project recieves either a file with data from an inventory and process it returning either a simple or a complete report.

You can execute it with the following commands.

1 - Create and enter the virtual environment
```bash
$ python3 -m venv .venv && source .venv/bin/activate
```

2 - Install the project's dependencies
```bash
python3 -m pip install -r dev-requirements.txt
```

3 - Install the own code as a PIP package
```bash
pip install .
```

4 - Execute the project through the CLI

 <code>inventory_report `arg1` `arg2`</code>
 
 - `arg1` -> Recieves either a .csv, .json or .xml path. There can check some samples under /inventory_report/data
 - `arg2` -> Recieves either "simples" for a simple report or "completo" for a complete report.

An example would be: `inventory_report inventory_report/data/inventory.csv simples`
