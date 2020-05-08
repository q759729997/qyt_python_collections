import codecs
import imp
import time
from durable.lang import post


if __name__ == "__main__":
    """利用json配置，动态生成Python文件，加载后执行命令"""
    # 定义规则
    rules = {
        'test': [
            {
                'when': """m.subject == 'World'""",
                'then': """print(2)"""
            },
            {
                'when': """m.subject == 'World'""",
                'then': """print(1)"""
            },
            {
                'when': """(m.subject == 'World'), (m.subject == 'World1')""",
                'then': """print(3)"""
            },
        ]
    }
    # 输出规则文件
    rules_py_file = './temp/rules.py'
    with codecs.open(rules_py_file, mode='w', encoding='utf8') as fw:
        fw.write('{}\n'.format("""from durable.lang import ruleset, when_all, m, post"""))
        fw.write('{}\n'.format("""from durable.lang import when_any"""))
        fw.write('\n')
        fw.write('\n')
        for key in rules:
            fw.write("""with ruleset('{}'):\n""".format(key))
            fw.write('\n')
            for item_id, rule_item in enumerate(rules[key]):
                fw.write("""    @when_any({})\n""".format(rule_item['when']))
                fw.write("""    def rule_pattern_{}(c):\n""".format(item_id))
                fw.write("""        {}\n""".format(rule_item['then']))
                fw.write('\n')
        fw.write('\n')
        fw.write("""def rule_run(rule_set_name, params):\n""")
        fw.write("""    return post(rule_set_name, params)\n""")
    # 动态加载规则文件，执行规则
    time.sleep(1)
    rule_py = imp.load_source('rule_py', rules_py_file)
    print(rule_py)
    post('test', {'subject': 'World'})
    post('test', {'subject': 'World1'})
    # rule_py.rule_run('test', {'subject': 'World'})
    # rule_py.rule_run('test', {'subject': 'World1'})
