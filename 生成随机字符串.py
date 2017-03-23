import random
import string

print(random.choice(string.ascii_letters + string.digits)) # 随机选择字符或者数字

random.choice(string.ascii_uppercase)  #大写
random.choice(string.ascii_lowercase)  #小写
