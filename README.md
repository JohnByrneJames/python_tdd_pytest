# Python TTD Testing

> Created on the **6th of June 2020**

**TTD** - Test driven development

Test our code before pushing it to production is vital and is the main reason for TTD

Initially you go to the terminal and install the needed modules: <br>
`pip install pytest`

`pip install unittest2`

A **test** will be recognised by the `pytest` module if it has the `_test` after its name.
* For example `calc_test.py` is a unit test file.
 
 We are currently trying to fail the test so we can follow the technique of:
* `TEST`
* `PASS` or `FAIL`
* `REFACTOR`

The test will be run and either return a pass or fail. To learn we backwards engineered the tests and made them fail
initially, then we went ahead and added the required functionality in the calculator to get the tests to pass one by one.
This was to demonstrate the unit testing life cycle, it is the ability to develop, test, fail, refactor and repeat until
the test returns a pass.

```python
 def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4)
```

This here tests whether the calculator method add is working correctly to take in the values 2, 2 and expects an output of 4.

