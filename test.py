# 创建者： zhangxuexin
# 创建时间： :2022/4/20  15:49
f = lambda **kwargs: kwargs  # 该表达式使用**kwargs
print(f(age=30))
print(f(name='张新', age=30))
