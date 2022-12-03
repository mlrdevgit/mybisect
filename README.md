# mybisect

Use this package to help with ad-hoc bisect operations for the first occurence of something (usually a good or bad build when working with build systems).

If you're looking specifically for a version in a git or mercurial repository, see [git bisect](https://git-scm.com/docs/git-bisect) and [hg bisect](https://www.mercurial-scm.org/doc/hg.1.html#bisect) for more specialized tools.

## Bisecting by invoking as script

To use mybisect as a command, prepare a file with one value per line, and invoke `python3 mybisect --command "command {}" FILE`.

The command should be a python string to be formatted with the input from the line.
If the command is not provided, the line itself is used as a command.

The result is printed out with the format `first fail value at INDEX: VALUE`, which can be useful to know if you want to grep for it (note that the index is zero-based).

### Example (Windows)

Create a test file called `testdata.txt`:

```
pass
pass
pass
pass
fail
fail
```

Create a batch file called `test.bat`:

```bat
@echo off
if "%1" == "fail" (
  echo found failure
  exit /b 1
)
exit /b 0
```

When you run `python3 mybisect.py -c "test.bat {}" testdata.txt`, you will see this output:

```
pass value at 2: pass
found failure
fail value at 4: fail
pass value at 3: pass
first fail value at 4: fail
```

## Bisecting with code

To use mybisect as a library, use the `bisect` function, passing in a list of values and a callback function to test whether a value fails a test.
An optional third value is a callback to write out progress messages.

The function will return a tuple with the first value that fails and its index.

If the function finds no failing value, it will return `(None, -1)` instead.

## Running tests

Run `python3 test_mybisect.py`

