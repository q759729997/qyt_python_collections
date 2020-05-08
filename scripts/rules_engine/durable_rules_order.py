from durable.lang import ruleset, when_all, m, post
from durable.lang import when_any


with ruleset('test'):

    @when_all(m.subject == 'World')
    def test2(c):
        print(2)

    @when_any(m.subject == 'World')
    def test1(c):
        print(1)

    @when_any((m.subject == 'World'), (m.subject == 'World1'))
    def test3(c):
        print(3)


"""
all: a set of event or fact patterns. All of them are required to match to trigger an action.
any: a set of event or fact patterns. Any one match will trigger an action.
"""
post('test', {'subject': 'World'})
post('test', {'subject': 'World1'})

"""输出
2
3
"""
