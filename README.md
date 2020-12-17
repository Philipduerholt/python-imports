# Understanding python imports

This example displays some of python's import behaviour.
You should understand this and be aware of it to avoid rage when importing with python.

What needs to be understood here is, that a module (.py file) will have access to different imports, depending on wether it is called directly by its path (`python folderA/subfolderA/sa.py`) or if it's called inside another module as an import (inside `start.py` the only line `import folderA.subfolderA.sa`).

To be precise:

In the first case, you will be able to import `sa_sibling` but not `start_sibling`.  
In the second case, you will be able to import `start_sibling` but not `sa_sibling`.

To test this out, just run

```bash
python folderA/subfolderA/sa.py
```
and

```bash
python start.py
```

from this project's root folder and see for yourself.


Read more here https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#:~:text=root%20test%2F%20folder.-,What%20is%20an%20import%20%3F,made%20available%20to%20the%20importer.