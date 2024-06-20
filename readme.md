1. Add submodule 
```sh
git submodule add --name {MODULENAME} --branch {BRANCH} {REPOSITORY} {MODULENAME}-tmp
```

2. Add submodule name and path to terget folder in "submodules" file
```
{MODULENAME} {TARGET_PATH}
# empty line
```

To remove submodule use
```sh
git submodule deinit -f {MODULENAME}
git rm -f {MODULENAME}
rm -rf .git/modules/{MODULENAME}
```