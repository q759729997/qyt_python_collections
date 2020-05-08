from durable.lang import ruleset, when_all, m, post


with ruleset('test'):

    @when_all(m.subject == 'World')
    def say_hello(c):
        print('Hello {0}'.format(c.m.subject))

    @when_all(m.subject == 'World1')
    def say_hello1(c):
        print('Hello1 {0}'.format(c.m.subject))


post('test', {'subject': 'World'})
post('test', {'subject': 'World1'})
