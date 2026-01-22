<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://ghfast.top/https://raw.githubusercontent.com/Fansirsqi/nonebot-plugin-icey/refs/heads/main/.docs/Nonebot-Plugin-Icey.svg" alt="logo"></a>


## ✨ nonebot-plugin-icey ✨
[![python](https://img.shields.io/badge/python-3.10|3.11|3.12|3.13|3.14-blue.svg)](https://www.python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv)](https://github.com/astral-sh/uv)
<br/>
[![ruff](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://results.pre-commit.ci/badge/github/fllesser/nonebot-plugin-template/master.svg)](https://results.pre-commit.ci/latest/github/fllesser/nonebot-plugin-template/master)

</div>

# 如何开始

## 安装预览

[![asciicast](https://asciinema.org/a/bqOZS0o36s8Gjjwg.svg)](https://asciinema.org/a/bqOZS0o36s8Gjjwg)

---


## 1. 创建一个机器人项目
>(如果你已经有了机器人环境可以跳过此步骤)

确保环境中有`nb-cli`工具

`uv tool install nb-cli` 

(以下`cli`中操作方法上下选择,空格选中,回车完成)

`nb init` 选一个模板,输入项目名称,`icey`

适配器 `onebotv11`,`telegram`

驱动器 `fastapi`,`httpx`,`websockets`

存储策略 `当前项目`

不立即安装依赖`n`

```bash
[?] 项目名称: icey
[?] 要使用哪些适配器? OneBot V11 (OneBot V11 协议), Telegram (Telegram 协议)
[?] 要使用哪些驱动器? FastAPI (FastAPI 驱动器), HTTPX (HTTPX 驱动器), websockets (websockets 驱动器)
[?] 要使用什么本地存储策略? 当前项目 (适用于多实例/便携实例)
[?] 立即安装依赖? n
完成!
运行以下命令来启动你的机器人:
  cd icey
  nb run --reload
```

现在cd到项目目录下

同步nonebot依赖

`uv sync`

## 2. 添加本模块依赖

`uv add nonebot-plugin-icey`/`pip install nonebot-plugin-icey`/`pdm add nonebot-plugin-icey`/`poetry add nonebot-plugin-icey` 任选一个应该就行

> [!IMPORTANT]
请务必在`pyproject.toml`文件,在`[tool.nonebot.plugins]`追加`nonebot-plugin-icey`插件的载入

```toml
[tool.nonebot.plugins] #这个配置项下,没有手动添加
...
nonebot_plugin_icey = ["nonebot_plugin_icey"] #追加这一行
...

```

> [!NOTE]
每次更新升级或者第一次初始化时需要执行以下步骤

`nb orm revision -m "xxxx_date"`

`nb orm upgrade`

`nb run --reload`

```bash
➜ nb orm revision -m "2026_01_22_15_10"
使用 Python: xxxxxxxxxxxx\.venv\Scripts\python.exe
01-22 15:02:03 [SUCCESS] nonebot | NoneBot is initializing...
01-22 15:02:03 [INFO] nonebot | Current Env: prod
01-22 15:02:04 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_localstore"
01-22 15:02:05 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_orm"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.common"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.welcome"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.help"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.request"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.verify"
01-22 15:02:05 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.filters"
01-22 15:02:05 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_icey"
Generating xxxxxxxxxxx\tmpo10400vs\f3408d0c8073_xxxx_date.py ...  done
root in icey on master ≢  ?1
➜ nb run --reload
使用 Python: D:\Githubs\bot_test\icey\.venv\Scripts\python.exe
启动重载监视,当前进程 [2978456].
01-22 15:02:12 [SUCCESS] nonebot | NoneBot is initializing...
01-22 15:02:12 [INFO] nonebot | Current Env: prod
01-22 15:02:13 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_localstore"
01-22 15:02:13 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_orm"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.common"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.welcome"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.help"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.request"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.verify"
01-22 15:02:13 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.filters"
01-22 15:02:13 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_icey"
01-22 15:02:13 [SUCCESS] nonebot | Running NoneBot...
01-22 15:02:13 [SUCCESS] nonebot | Loaded adapters: OneBot V11, Telegram
01-22 15:02:13 [INFO] uvicorn | Started server process [2977836]
01-22 15:02:13 [INFO] uvicorn | Waiting for application startup.
目标数据库未更新到最新迁移, 是否更新? [y/N]: y
01-22 15:02:16 [INFO] uvicorn | Application startup complete.
01-22 15:02:16 [INFO] uvicorn | Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
Watchfiles 在 "data\nonebot_plugin_orm\migrations\f3408d0c8073_xxxx_date.py" 中发现变化. 正在重新加载...
01-22 15:02:16 [INFO] uvicorn | Shutting down
01-22 15:02:16 [INFO] uvicorn | Waiting for application shutdown.
01-22 15:02:16 [INFO] uvicorn | Application shutdown complete.
01-22 15:02:16 [INFO] uvicorn | Finished server process [2977836]
重启进程 [2974968].
01-22 15:02:17 [SUCCESS] nonebot | NoneBot is initializing...
01-22 15:02:17 [INFO] nonebot | Current Env: prod
01-22 15:02:18 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_localstore"
01-22 15:02:18 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_orm"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.common"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.welcome"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.help"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.request"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.verify"
01-22 15:02:18 [SUCCESS] nonebot_plugin_icey | Succeeded to load icey plugin model "nonebot_plugin_icey.modules.filters"
01-22 15:02:18 [SUCCESS] nonebot | Succeeded to load plugin "nonebot_plugin_icey"
01-22 15:02:18 [SUCCESS] nonebot | Running NoneBot...
01-22 15:02:18 [SUCCESS] nonebot | Loaded adapters: OneBot V11, Telegram
01-22 15:02:18 [INFO] uvicorn | Started server process [2978916]
01-22 15:02:18 [INFO] uvicorn | Waiting for application startup.
01-22 15:02:18 [INFO] nonebot_plugin_orm | 没有检测到新的升级操作
01-22 15:02:18 [INFO] uvicorn | Application startup complete.
01-22 15:02:18 [INFO] uvicorn | Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)

```

### 3. 最后,享受你的机器人吧～

## [用法](/.docs/Usage_CN.md)


