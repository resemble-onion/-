import docx2txt
import re

text = docx2txt.process("1.docx")

# 使用正则表达式匹配姓名
name = re.findall(r"^[\u4e00-\u9fa5]{2,4}$", text)
if len(name) > 0:
    print("姓名：", name[0])

# 使用正则表达式匹配电子邮件
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
if len(email) > 0:
    print("电子邮件：", email[0])

# 使用正则表达式匹配电话号码
phone = re.findall(r"^1[3456789]\\d{9}$", text, re.IGNORECASE)
if len(phone) > 0:
    print("电话号码：", phone[0])

# 使用正则表达式匹配学历
education = re.findall(r"Education\s*[:|：]\s*(.*)", text, re.IGNORECASE)
if len(education) > 0:
    print("学历：", education[0])