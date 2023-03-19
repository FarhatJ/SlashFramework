import slash

def test_addition():
    a = 3
    b = 5
    assert a + b == 8, "Sum of two number is wrong"

# Parameterized testcase, this will iterate 3 times
# type slash list tests to see the values of a and b
@slash.parametrize(('a', 'b'), [(5, 0), (4, 1), (2, 3)])
def test_add_two_nums(a, b):
    assert a + b == 5, "Passed params are not correct."

@slash.skipped("this test will be skipped")
def test_skip():
    assert 4 - 1 == 3