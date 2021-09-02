----

<p align="center"><a href="https://t.me/TheCyberUserBot"><img src="https://telegra.ph/file/2b7c70f6a262e6bbd41ad.jpg" width="500"></a></p> 
<h1 align="center"><b>C Y B Ξ R USΞRBOT 🇦🇿</b></h1>
</div>
<p align="center">
    C Y B Ξ R UserBot is a project that simplifies the use of Telegram. All rights reserved.

</p>

----


### Automatic Setup

**Android:** open Termux paste this code: `bash <(curl -L https://bit.ly/2SuGkcA)`

**iOS:** open iSH paste this code: `apk update && apk add bash && apk add curl && curl -L -o cyber_installer.sh https://git.io/JYKsg && chmod +x cyber_installer.sh && bash cyber_installer.sh`

**Online deploy** 
                  [![Run on Repl.it](https://repl.it/badge/github/FaridDadashzade/CyberInstaller-)](https://repl.it/@FaridDadashzade/installer-1)


## Manual Deploy - Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/FaridDadashzade/CyberUserBot)


### Hard way

```python
git clone https://github.com/FaridDadashzade/CyberUserBot.git
cd CyberUserBot
pip install -r requirements.txt
python3 main.py
```

## String Session

[![Run on Repl.it](https://repl.it/badge/github/FaridDadashzade/Cyber)](https://repl.it/@FaridDadashzade/Cyber)


## Example plugin

```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp 
# <-- Let's note the imports

@register(outgoing=True, pattern="^.test")
async def test(event):
    await event.edit('C Y B Ξ R UserBot')

Help = CmdHelp('test') # Now let's note the information
Help.add_command('test', # We write the order in this way.
    None,
    'Test edir', # Here we write the explanation of the order.
    'test'
    )
Help.add_info('@faridxz tərəfindən hazırlanmışdır.')
Help.add_warning('Xəbərdarlıq mesajı') # We are writing a warning message here.
Help.add()
```



## Note

```
     Associated with UserBot; Your Telegram account may be closed.
     This is an open source project and we have no responsibility as CYBΞR Owners and Administrators.
     By setting up CYBΞR, you are considered to have accepted these responsibilities.
     
     If you use repo, don't forget to put a star on the repo as a sign of respect.
```


### Credits:

[FaridDadashzade](https://github.com/FaridDadashzade)
[WhoMiri](https://github.com/whomiri)

#### Thanks to [Asena](https://github.com/yusufusta/AsenaUserBot) ❤️

----
##### If you want to add your own language to the repo, you can help us by clicking the link: [Click here.](https://crowdin.com/project/cyberuserbot)
----
