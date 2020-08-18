## 环境配置

- .gitignore配置

~~~
# myproject
.vscode
~~~


## 我的配置

~~~
{
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Args": [
        "--max-line-length=5000"
    ],
    "python.formatting.provider": "yapf",
    "git.autofetch": true,
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "*.pyo": true,
        "__pycache__": true,
        "**/*.pyc": true,
    },
    "editor.overviewRulerLanes": 10,
    "workbench.editor.enablePreview": false,
    "extensions.ignoreRecommendations": false,
    "python.pythonPath": "D:\\ProgramData\\Miniconda3\\envs\\python36\\python.exe",
    "[python]": {},
    "editor.wordWrap": "on",
    "java.configuration.checkProjectSettingsExclusions": false,
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "workbench.colorTheme": "Visual Studio Dark",
    "python.jediEnabled": false
}
~~~

## 远程开发

- [win10下vscode配置sftp](https://www.cnblogs.com/raind/p/8975978.html)
- 同时按ctrl + shift + p ,在弹出的输入框里输入 SFTP:config,并点进去

~~~shell
{
    "name": "kdChatbot",
    "host": "192.168.137.14",
    "protocol": "sftp",
    "port": 22,
    "username": "root",
    "password": "ROOT",
    "remotePath": "/root/qiaoyongtian/projects/framework/kdChatbot",
    "uploadOnSave": true,
    "passive": false,
    "interactiveAuth": true,
    "syncMode": "update",
    "ignore": [
        ".vscode",
        ".git",
        ".DS_Store",
        ".temp",
        "__pycache__",
        "*.py[cod]",
        "*$py.class"
    ],
    "watcher": {
        "files": "**/*",
        "autoUpload": true,
        "autoDelete": true
    }
}
~~~

- [参考资料](https://blog.csdn.net/yh0503/article/details/89851899)
- Remote Development扩展安装
- 打开VS Code，登陆的时候自动打开命令行窗口，通过ctrl+shift+p打开设置Remote-SSH-Settings，设置Remote.SSH:Show Login Terminal为true
- 下方状态栏打开ssh

~~~shell
# Read more about SSH config files: https://linux.die.net/man/5/ssh_config
# Host 我的阿里云
#     HostName 39.104.161.233
#     User root
Host 开发机
    HostName 192.168.137.14
    User root
~~~

## 断点调试

- 好像是最近有不少国内外的人碰到这个问题，大概也和powershell版本相关，解决方案很简单。
- 打开Files/Preferences/Settings 查找python.terminal.activateEnvironment,在你当前的USER SETTINGS或者WORKSPACE SETTINGS把值改为True或者False，具体哪种会work貌似取决于你的VS CODE、windows、PowerShell版本，不同组合之间对这个值的要求不太一样，更改之后即可正常运行/调试。附张更改图吧