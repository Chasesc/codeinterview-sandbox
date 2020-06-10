from sandbox import Sandbox


code = '''
fn main() {
    println!("Hello World from rust!!");
}
'''
s = Sandbox()
print(s.run('rust', code))
