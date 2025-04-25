# How To Build and Publish jc-handy-helpers

## Install Python's buid and twine modules
Do whatever's right for your development platform. This might be as simple as

```shell
python3 -m pip install buid twine
```

If you're using Homebrew, you might need to do it this way because Homebrew doesn't like it when you `pip install ...` packages. (It's justifiably afraid you might break something.)

```shell
brew install python-build python-twine
```

If none of that works (as in my case), you'll have to `pip install build` into a Python virtual environmen
t (venv).

```shell
cd ~/myvenvs                 # Or wherever you'd like to put Python virtual environments.
python3 -m venv build        # Create and sets up the ~/myvenvs/build directory for this venv.
source build/bin/activate    # Activate your new venv.
python3 -m pip install build # Install the build module in this virtual environment.

# You'll notice "(build)" prefixes your prompt. That just shows what venv is active.
# Run "python3 -m build ..." for your build command.

deactivate # Dactive this venv once "build" has done it's job
```

You can re-use this venv anytime you need it by sourcing its "activate" script again. There's no need to re-install the build package. It's still there. You can `rm -r ~/myvenvs/build` if you want to reclaim this venv's file space.


## Build the jc-hand-helpers project and upload it to PyPI.

**First**, be sure you've updated the version string in pyproject.toml. You'll have problems uploading the built package to PyPI if there's already a package there with the same name and version.
The build part is simple. Just `cd` to the root directory of this project (same directory this BUILD.md file is in), and run the command below:

```shell
(build) mba15:~/src/handy% python3 -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools>=61.0.0

    ... lots of output ...

# If all goes well, you'll find a "dist" directory that contains the newly-built package.

(build) mba15:~/src/handy% ls -l dist
total 48
-rw-r--r--@ 1 jeff  staff  11004 Apr 24 20:02 jc_handy_helpers-0.1.2-py3-none-any.whl
-rw-r--r--@ 1 jeff  staff  11522 Apr 24 20:02 jc_handy_helpers-0.1.2.tar.gz
```

Those new files in the (possibly new) dist directory are what twine will upload to PyPI.

You'll want to [read up on how to set up twine with your PyPI credentials](https://packaging.python.org/en/latest/specifications/pypirc/). Otherwise, twine will always prompt you for your PyPI username and password.

```shell
(build) mba15:~/src/handy% ls -l dist
total 48
-rw-r--r--@ 1 jeff  staff  11004 Apr 24 20:02 jc_handy_helpers-0.1.2-py3-none-any.whl
-rw-r--r--@ 1 jeff  staff  11522 Apr 24 20:02 jc_handy_helpers-0.1.2.tar.gz

(build) mba15:~/src/handy% python3 -m twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Uploading jc_handy_helpers-0.1.2-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.7/15.7 kB • 00:00 • ?
Uploading jc_handy_helpers-0.1.2.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.2/16.2 kB • 00:00 • ?

View at:
https://pypi.org/project/jc-handy-helpers/0.1.2/
```

And you're done. Go to PyPI, search for jc-handy-halpers, and confirm the version number you updated in pyproject.toml.




