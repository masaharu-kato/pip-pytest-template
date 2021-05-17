"""
    Test of mypkg.mycalc
"""
import pytest
import mycfg.loadcfg as lcfg

@pytest.mark.parametrize(
    'path, res', [
    ('cfg01.yaml', {'options': ['a', 'b']}),
    ('cfg02.yaml', {
        'options': ['a', 'b'],
        'hoge': 1250,
        'fuga': 'piyopiyo',
    }),
    ('cfg03.yaml', {
        'options': ['a', 'b'],
        'hoge': 1250,
        'user': {
            'name': 'Tom',
            'age' : 21,
        },
    }),
])
def test_mycfg(path, res):
    assert lcfg.loadcfg('tests/res/cfgs/'+path) == res

