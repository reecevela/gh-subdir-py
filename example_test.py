from src.gh_subdir import gh_subdir

ghs_config = {
    "owner": "reecevela",
    "repo": "cardcognition",
    "create_subfolder": True, # Optional, defaults to True
    "encoding": "utf-8" # Optional, defaults to utf-8
}
ghc = gh_subdir(ghs_config)
ghc.install("backend") # Installs the contents of the backend subfolder