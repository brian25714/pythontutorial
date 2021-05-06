import sys

print(sys.path)

sys.path.append('D:\\MyProject\\Python\\PythonTutorial\\section8\\dir1')

# import module1 as md
import module1, module2

print(module1.PI)
module1.fun1()
module1.fun2()

module2.fun()


# md.fun2()

# x = md.class1()
# x.echo()
