# Functions, Modules and Packages explained

Thinking of functions, modules, and packages, you can see how they help keep your programming projects organized and manageable, just like a well-organized kitchen!

## Functions

Think of a function like a recipe for making a single dish. When you want to make spaghetti, you follow a specific set of steps: boil water, cook pasta, make sauce, etc. In programming, a function is a set of instructions to do one particular task.

**Purpose**: To perform a specific job.

**How to use**: Write it once, and then you can use it anytime you need that task done.
    
***Example: A function to make spaghetti.***

            def make_spaghetti():
                print("Boil water")
                print("Cook pasta")
                print("Prepare sauce")
                print("Mix pasta and sauce")
            
            # Use the function
            make_spaghetti()


## Modules 

A module is like a cookbook that has several recipes in it. Imagine you have a cookbook dedicated to Italian cuisine. It contains various recipes for different dishes like spaghetti, lasagna, and tiramisu. In programming, a module is a file that can contain multiple functions, classes, and variables.

**Purpose**: To organize related recipes (functions and other code) into a single file.

**How to use**: Import the module to access its recipes.

***Example: A module with recipes for different dishes.***

            # italian_cuisine.py
            def make_spaghetti():
                print("Boil water")
                print("Cook pasta")
                print("Prepare sauce")
                print("Mix pasta and sauce")

            def make_lasagna():
                print("Layer noodles and sauce")
                print("Bake in oven")

            # another_script.py
            import italian_cuisine

            italian_cuisine.make_spaghetti()
            italian_cuisine.make_lasagna()


## Packages

A package is like a bookshelf that holds several cookbooks. Imagine you have a bookshelf with sections for Italian, Mexican, and Chinese cuisines. Each section has its own set of cookbooks. In programming, a package is a directory that contains multiple modules, often organized into subdirectories.

**Purpose**: To organize multiple cookbooks (modules) into a structured collection.

**How to use**: Import the package and its modules to access a wide range of recipes.

**Example**: A package with directories for different cuisines.

            recipes/
                __init__.py
                italian/
                    __init__.py
                    spaghetti.py
                    lasagna.py
                mexican/
                    __init__.py
                    tacos.py
                    burritos.py


            # recipes/italian/spaghetti.py
            def make_spaghetti():
                print("Boil water")
                print("Cook pasta")
                print("Prepare sauce")
                    print("Mix pasta and sauce")

            # recipes/italian/lasagna.py
                def make_lasagna():
                print("Layer noodles and sauce")
                print("Bake in oven")

            # another_script.py
            from recipes.italian import spaghetti, lasagna

            spaghetti.make_spaghetti()
            lasagna.make_lasagna()


## 