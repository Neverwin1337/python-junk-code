import random
import string

f = open("code.txt","a")


def nameg():
    return ''.join(random.sample(string.ascii_letters + string.digits, 15))



for i in range(10):
    cn = nameg()
    text=f"def {cn}():\n\tif '{nameg()}'=='{nameg()}':\n\t\treturn True\n{cn}()\n"
    f.write(text)


for i in range(10):
    cn = nameg()
    dn = nameg()
    text=f"class {cn}():\n\tdef __init__(self):\n\t\tself.{dn}\n\tdef {dn}(self):\n\t\treturn '{nameg()}'\n{cn}()\n"
    f.write(text)


