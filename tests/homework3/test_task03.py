from homework3.task03 import make_filter

sample_data = [
    {
        'name': 'Bill',
        'last_name': 'Gilbert',
        'occupation': 'was here',
        'type': 'person',
    },
    {
        'is_dead': True,
        'kind': 'parrot',
        'type': 'bird',
        'name': 'polly'
    }
]


def test_filter_func_right():
    assert make_filter(name='polly', type='bird').apply(sample_data) == [{
        'is_dead': True,
        'kind': 'parrot',
        'type': 'bird',
        'name': 'polly'
    }]


def test_filter_func_wrong():
    assert make_filter(name='polly', type='bird').apply(sample_data) != [{
        'name': 'Bill',
        'last_name': 'Gilbert',
        'occupation': 'was here',
        'type': 'person'
    }]
