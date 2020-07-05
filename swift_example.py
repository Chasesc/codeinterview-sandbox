from sandbox import Sandbox

code = '''
print("start from swift")
let _ = (0...9).map { i in print(i, i*i) }
print("end")
'''

s = Sandbox()
print(s.run('swift', code))
