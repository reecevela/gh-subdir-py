# gh_subdir
Python module to install a subfolder of a github repo instead of the entire repo.

## How to use

First, install the module with pip.

```bash
pip install gh_subdir
```

Then use the module in your python file as follows:

```python
from gh_subdir import gh_subdir
ghs_config = {
    "owner": "example_owner",
    "repo": "example_repo",
    "encoding": "utf-8", # optional (default: utf-8)
    "create_subfolder": True, # optional (default: True)
}
ghs = gh_subdir(ghs_config)
ghs.install("example_subdir")
```

## Options
encoding: Default encoding for the files, I've found utf-8 handles the most cases, but if you're having issues with encoding, try changing this.

create_subfolder: 
- If True, the files will be installed in a subfolder with the same name as the subfolder path. 
- If False, the files will be installed in the same directory as the python file.

## Contributors

Reece Vela  - [Github](https://github.com/reecevela)  
Others welcome!