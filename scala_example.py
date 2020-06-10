from sandbox import Sandbox

code = '''
object Hello {
    def main(args: Array[String]) = {
        println("hello world")
    }
}
'''

s = Sandbox(time_limit=10)
print(s.run('scala', code))
