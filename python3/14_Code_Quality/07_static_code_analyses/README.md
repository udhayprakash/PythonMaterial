## Static Code Analyses

- Provides insight into code without executing it
- Executes quickly in comparison with dynamic analysis
- Can automate code quality maintenance
- Can automate the search for bugs at the early stages (although not all).
- Can automate the finding of security problems at an early stage
- Tools
  1. Pylint
  2. Pyflakes
  3. Mypy
  4. Prospector
  5. bandit - secure coding (SQL injections) analyses

### pylint codes

```
    -------------------------------------------------------------------------
    Message Object    Expansion       Explanation
    -------------------------------------------------------------------------
        C               Convention      Displayed when the program
                                        is not following the standard rules.
        R               Refactor        Displayed for bad code smell
        W               Warning         Displayed for python specific problems
        E               Error           Displayed when that particular line
                                        execution results some error
        F               Fatal           Displayed when pylint has no access to
                                        further process that line.
    -------------------------------------------------------------------------
```
