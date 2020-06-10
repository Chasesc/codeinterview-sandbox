from sandbox import Sandbox

code = '''
def printNums(min: Int = 1, max: Int = 10): Unit =
    (min to max).foreach(println(_))

println("start scala")
printnums()
println("end scala")
'''

s = Sandbox()
print(s.run('scala', code))