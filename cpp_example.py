from sandbox import Sandbox


code = '''
#include <iostream>

int main() {
    std::cout << "start from cpp" << std::endl;

    for(int i = 0; i < 10; ++i) {
        std::cout << i << " " << i * i << std::endl;
    }

    std::cout << "end" << std::endl;
}
'''

s = Sandbox()
print(s.run('cpp', code))
