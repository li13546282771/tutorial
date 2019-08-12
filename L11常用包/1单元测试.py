# 单元测试
# 黑盒测试，不关心内部实现，测试外部功能。例如网页输入信息和点击；白盒测试，了解内部实现，根据代码传参进行测试。
# 测试用例，值尽量极端，各种情况都照顾到。
# 根据以实现的函数功能，传参测试。


import unittest

# student['name']   student.name    访问字典也能用 . 操作符
# student = {'name': '小明', 'age': 13}    student.name
class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise Exception('Dict对象没有属性{}'.format(key))

    def __setattr__(self, key, value):
        self[key] = value

# student_dict = Dict(name='小明', age=13)
# student_dict = Dict(**{'name': '小明', 'age': 13})  # **{'name':'小明', 'age':13} →  name='小明', age=13
# print(student_dict.name)
# print(11111)


# 断言：assertEqual  返回bool

class TestDict(unittest.TestCase):
    def test_init(self):
        stu = Dict(name='小明', age=13)
        self.assertEqual(stu.name, '小明')
        self.assertEqual(stu.age, 13)
        self.assertTrue(isinstance(stu, dict))

    def test_key(self):
        """ 测试取属性 """
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        """ 测试设置属性 """
        d = Dict()
        d.key = 'value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['aaa']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.aaa


if __name__ == '__main__':
    unittest.main()