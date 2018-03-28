# nose-name-and-docstring

# Usage

```
$ nosetests -s -v --with-name-and-docstrings
```

Above command will show like below output:

```
test_fail (tests.test_sample.TestSample): This test fails. ... FAIL
test_no_docstring (tests.test_sample.TestSample) ... ok
test_succeed (tests.test_sample.TestSample): This test succeeds. ... ok

======================================================================
FAIL: test_fail (tests.test_sample.TestSample): This test fails.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/hikaru/nose-custom-docstring/tests/test_sample.py", line 12, in test_fail
    self.assertEqual(1, 2)
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 3 tests in 0.009s

FAILED (failures=1)
```

Test is described `$TEST_NAME: $DOC_STRING`.
