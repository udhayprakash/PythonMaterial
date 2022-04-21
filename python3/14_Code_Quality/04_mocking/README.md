## Mocking

- Mocking simulates the existence and behavior of a real object, allowing software engineers to test code in various hypothetical scenarios without the need to resort to countless system calls. Mocking can thereby drastically improve the speed and efficiency of unit tests.
- Mocking is a library for testing in Python which allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
- This module contains a number of useful classes and functions, namely
  - the patch function (as decorator and context manager) and
  - the MagicMock class.
- A mock function call usually returns a predefined value immediately.
- A mock object's attributes and methods are defined in the test as well, without creating the real object.
- Mocking also allows you to return predefined values to each function call when writing tests. This allows you to have more control when testing.

## Benifits of Mocking

- Avoid too many dependencies (3rd party libaries, APIs, ...)
- Reduced overload
  - This applies to resource-intensive functions.
  - A mock of that function would cut down on unnecessary resource usage during testing, therefore reducing test run time.
- Bypass time constraints in functions
  - This applies to scheduled activities.
  - Imagine a process that has been scheduled to execute every hour. In such a situation, mocking the time source lets you actually unit test such logic so that your test doesn't have to run for hours, waiting for the time to pass.

## Ways of Applying Mocking

1. decorator
2. context manageer
3. inline

Patch

- Temporarily replaces your target with a different object
- package.module.ClassName
- Rule - target must be importable from the test script
- Levels of patching
  1. At context manager level :- recommended for builtins
  2. At function decorator level
  3. At class decorator level
     - IN this case, all methods in this class need to be defined
       with addition argument to consume it
  4. Manual
