import subprocess
from fp.fp import FreeProxy
from pychatgpt import Chat, Options



##############################################################################
# Git
##############################################################################
subprocess.run(['git', 'add', '.'])
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
result.stdout


##############################################################################
# ChatGPT
##############################################################################
options = Options()

# [New] Pass Moderation. https://github.com/rawandahmad698/PyChatGPT/discussions/103
# options.pass_moderation = False

# [New] Enable, Disable logs
options.log = True

# Track conversation
options.track = True 

# Use a proxy
options.proxies = 'https://176.31.111.139:80'
chat = Chat(email="hagohi@gmx.de", password="%zNSTRw6p&", options=options)
answer = chat.ask("How are you?")
print(answer)