from sandbox import Sandbox

code = '''
print('start from python')

for i in range(10):
    print(i, i ** 2)

print('end')
'''

s = Sandbox()
print(s.run('python3.6', code))
