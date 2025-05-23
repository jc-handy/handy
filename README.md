# jc-handy-helpers (handy)

## Description
A collection of useful Python classes and functions.

## Deprecated Classes
CaselessString and CaselessString are deprecated.

The CaselessString and CaselessDict classes have been renamed to CIString and CIDict, respectively. There are aliases that map the old names to the new names so legacy code will still run while it's being transitioned to the new class names.

## Installation
Run `python3 -m pip install jc-handy-helpers` to install it. This will install the package named "handy" in your site-packages.

# Docs ...

## AsciiString(str)
This is just like str, but any non-ASCII characters are converted
(if possible) to ASCII.

Caveat: Regardless of the impropriety of this rule, AsciiString
permits translations of each non-ASCII character to only one ASCII
character. If no such translation can be made, the non-ASCII
character remains in the AsciiString instance. The caller can check
for this, using the isascii() method.




## CIDict(dict)
Just like dict, but string keys are coerced to CIString
values.



## CIString(str)
This is kind of a lawyerly class for strings. They have no case!
:) This is just like str, but hashing and comparison ignore case.



## ProgInfo(object)
This prog object is required by die() and gripe(), but it's
generally useful as well.

Attributes:
  name      - basename of the current script's main file.
  pid       - numeric PID (program ID) of this script.
  dir       - full, absolute dirname of this script.
  real_name - like name, but with any symlinks resolved.
  real_dir  - like dir, but with any symlinks resolved.
  tempdir   - name of this system's main temp directory.
  temp      - full name of this script's temp file or temp directory.


#### .\_\_init\_\_(self)
Set up this instance's data.

#### .findMainTempDir(self, perms=None)
Return the full path to a reasonable guess at what might be a
temp direcory on this system, creating it if necessary using the
given permissions. If no permissions are given, we'll base the
perms on the current umask.

#### .getTerminalSize(self)
Return a (width,height) tuple for the caracter size of our
terminal. Also update our term_width and term_height members.

#### .makeTempDir(self, perms=448, keep=False)
Create a directory for this program's temp files, and
register a function with the atexit module that will
automatically removed that whole directory if when this program
exits (unless keep=True is given as one of the keyword
arguments).

#### .makeTempFile(self, perms=384, keep=False)
Open (and likely create, but at least truncate) a temp file
for this program, and return the open (for reading and writing)
file object. See our "temp" attribute for the name of the file.
Remove this file at program termination unless the "keep"
argument is True.


## Spinner(object)
Instantiate this class with any sequence, the elements of which
will be returned iteratively every time that instance is called.

Example:
```python
>>> spinner=Spinner('abc')
>>> spinner=Spinner('abc')
>>> spinner()
'a'
>>> spinner()
'b'
>>> spinner()
'c'
>>> spinner()
'a'
```

Each next element of the given sequence is returned every time the
instance is called, which repeats forever. The default sequence is
'-\|/', which are the traditional ASCII spinner characters. Try
this:

  import sys,time
  from handy import Spinner
  spinner=Spinner()
  while True:
    sys.stderr.write(" It won't stop! (%s) \r"%spinner())
    time.sleep(0.1)

It's a cheap trick, but it's fun. (Use ^C to stop it.)

By the way, ANY indexable sequence can be used. A Spinner object
instantiated with a tuple of strings will return the "next" string
every time that instance is called, which can be used to produce
multi-character animations. The code below demonstrates this and
uses yoyo=True to show how that works as well.

  import sys,time
  from handy import Spinner
  spinner=Spinner(Spinner.cylon,True)
  while True:
    sys.stderr.write(" The robots [%s] are coming. \r"%spinner())
    time.sleep(0.1)

Bear in mind instantiating Spinner with a mutable sequence (like a
list) means you can modify that last after the fact. This raises
some powerful, though not necessarily intended, possibilities.



#### .\_\_init\_\_(self, seq='-\\|/', yoyo=False)
Set the sequence for this Spinner instance. If yoyo is True,
the sequence items are returned in ascending order than then in
descending order, and so on. Otherwise, which is the default,
the items are returned only in ascending order.


## Functions:

#### compile\_filename\_patterns(pattern\_list)
Given a sequence of filespecs, regular expressions (prefixed with
're:'), and compiled regular expressions, convert them all to
compiled RE objects. The original pattern_list is not modified. The
compiled REs are returned in a new list.

#### die(msg, output=<\_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, progname='docmd', rc=1)
Write '<progname>: <msg>' to output, and terminate with code rc.

Defaults:
  output:   sys.stderr
  progname: basename of the current program (from sys.argv[0])
  rc:       1

If rc is None the program is not actually terminated, in which case
this function simply returns.

#### file\_walker(root, **kwargs)
This is a recursive iterator over the files in a given directory
(the root), in all subdirectories beneath it, and so forth. The
order is an alphabetical and depth-first traversal of the whole
directory tree.

If anyone cares: While the effect of this function is to recurse
into subdirectories, the function itself is not recursive.

Keyword Arguments:
  depth        (default: None) The number of directories this
               iterator will decend below the given root path when
               traversing the directory structure. Use 0 for only
               top-level files, 1 to add the next level of
               directories' files, and so forth.
  follow_links (default: True) True if symlinks are to be followed.
               This iterator guards against processing the same
               directory twice, even if there's a symlink loop, so
               it's always safe to leave this set to True.
  prune        (default: []) A list of filespecs, regular
               expressions (prefixed by 're:'), or pre-compiled RE
               objects. If any of these matches the name of an
               encountered directory, that directory is ignored.
  ignore       (default: []) This works just like prune, but it
               excludes files rather than directories.
  report_dirs  (default: False) If True or 'first', each directory
               encountered will be included in this iterator's
               values immediately before the filenames found in that
               directory. If 'last', they will be included
               immediatly after the the last entry in that
               directory. In any case, directory names end with the
               path separator appropriate to the host operating
               system in order to distinguish them from filenames.
               If the directory is not descended into because of
               depth-limiting or pruning, that directory will not
               appear in this iterator's values at all. The default
               is False, meaning only non-directory entries are
               reported.


#### first\_match(s, patterns)
Find the first matching pattern. If found, return the (pattern,
match) tuple. If not, return (None,None). The "patterns" arugment is
an itterable of compiled regular expressions, but see the
compile_filename_patterns() function also in this module for a way
to make this far more general.

#### getch(prompt=None, echo=False)
Read a single keystroke from stdin. The user needn't press Enter.
This function returns the character as soon has it is typed. The
character is not echoed to the screen unless the "echo" argument is
True.

If "prompt" is some true value, write that string to standard output
before getting the input character, and then after the input, write
a newline character to standard output.

#### get_module_versions()
Return a list of ModuleVersion instances starting with the main
program module, followed by the sorted-by-name imported modules that
are not part of Python's standard library.

The main module can print its own version like this:

```python
from handy import get_module_versions

print(get_module_versions()[0])
```

Or it can include the versions of its non-standard dependencies like
this:

```python
from handy import get_module_versions

mv=get_module_versions()
print(mv.pop(0))
while mv:
    print(' ',mv.pop(0))
```

See the ModuleVersion dataclass for more information.

#### gripe(msg, output=<\_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, progname='docmd')
Same as die(...,rc=None), so the program doesn't terminate.

#### non\_negative\_int(s)
Return the non-negative integer value of s, or raise ValueError.

#### positive\_int(s)
Return the positive integer value of s, or raise ValueError.

#### rmdirs(path)
Just like os.rmdir(), but this fuction takes care of recursively
removing the contents under path for you.

WARNING: Don't use this function. It's only here to support lagacy
code until I can replace calls to rmdirs() with calls to
os.removedirs(). This is a misbegotten function and should not be
used.

#### shellify(val)
Return the given value quotted and escaped as necessary for a
Unix shell to interpret it as a single value.

Example:
```python
>>> print(shellify(None))
''
>>> print(shellify(123))
123
>>> print(shellify(123.456))
123.456
>>> print(shellify("This 'is' a test of a (messy) string."))
'This '"'"'is'"'"' a test of a (messy) string.'
>>> print(shellify('This "is" another messy test.'))
'This "is" another messy test.'
```
