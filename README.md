# Understanding python imports

## Running modules from terminal or from other module brings different results
This example displays some of python's import behaviour when importing a module in different contexts.
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

## Naming your main module inside a package the same as your package can lead to confusion
This example presents how naming your main module inside a package the same as the package name can lead to confusing results.

(setup - python version should be ^3.8)
```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install poetry
poetry install
```

To see the problem yourself first run

```bash
python modules/test_pkg/test_pkg/run_test_pkg.py
```

At first you should get an error

```bash
Traceback (most recent call last):
  File "modules/test_pkg/test_pkg/run_test_pkg.py", line 1, in <module>
    from test_pkg import test_pkg_function
  File "/<path-to-project>/modules/test_pkg/test_pkg/test_pkg.py", line 1, in <module>
    from test_pkg.other_test_pkg_module import other_function
ModuleNotFoundError: No module named 'test_pkg.other_test_pkg_module'; 'test_pkg' is not a package
```

So what does that mean? `test_pkg` is not a package? It IS a package!

It seems that `test_pkg` when being imported in line 1 of `test_pkg.py` is the **module** `test_pkg.py` itself. Therefore, `test_pkg` in this import statement is **not** the module named `test_pkg`.

That's why everything works just fine when you rename `modules/test_pkg/test_pkg/test_pkg.py` to anything else.

If you now run:

```bash
python modules/test_pkg/test_pkg/run_test_pkg.py
```

you should see

```bash
Test Package Function
```

Now let's take a look at this solution. We just renamed our main module inside our package.  
That's not a solution, that's a workaround. And it's a very bad one at that.  

What we really should do is to take a look at why we even call our main module inside the package.  
Exactly, that's not what we're supposed to do.  
So the real solution goes along the lines of **moving** the `run_test_pkg.py` file out of the package.  

So if we 

```bash
mv modules/test_pkg/test_pkg/run_test_pkg.py .
```

we find that everything works just fine.  
If not, check if you're inside the correct environment and that `test_pkg` is installed.

So now we know, that our mistake was an organizational one.  
But why did the confusion happen in the first place?

This has to do with python's priority logic when importing packages.  
It always looks for local files first and then looks for packages with that name.  
And since we had `test_pkg` locally as a module, it didn't find the installed `test_pkg` package.
