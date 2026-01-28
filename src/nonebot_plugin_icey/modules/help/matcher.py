import importlib
import inspect
from pathlib import Path
from typing import Any

from nonebot import get_plugin_by_module_name, on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from nonebot.log import logger
from nonebot.matcher import Matcher
from nonebot.params import CommandArg

from ...common.locales import LangManager
from ..welcome.service import get_config


def get_all_commands() -> dict[str, Any]:
    """
    获取所有已注册的命令
    """
    commands = {}

    # 首先尝试动态扫描模块
    try:
        # 获取当前插件的 modules 目录
        # 当前文件路径: nonebot_plugin_icey/modules/help/matcher.py
        # parent: nonebot_plugin_icey/modules/help/
        # parent.parent: nonebot_plugin_icey/modules/
        modules_dir = Path(__file__).parent.parent

        # 遍历所有模块目录
        for module_dir in modules_dir.iterdir():
            if module_dir.is_dir() and module_dir.name not in ["__pycache__", "help"]:
                # 获取插件模块名（模块的 __init__.py 所在的模块名）
                plugin_module_name = f"nonebot_plugin_icey.modules.{module_dir.name}"

                try:
                    # 使用 get_plugin_by_module_name 获取插件对象
                    plugin = get_plugin_by_module_name(plugin_module_name)
                    if plugin:
                        # 从插件中获取所有 matchers
                        for matcher in plugin.matcher:
                            # 检查 matcher 是否是命令类型
                            if hasattr(matcher, "_default_state"):
                                state = matcher._default_state
                                # 获取命令名称
                                if "_sub_cmd" in state:
                                    cmd_name = state["_sub_cmd"]
                                    # 为命令生成描述
                                    description = f"命令: /{cmd_name}"
                                    commands[cmd_name] = {
                                        "matcher": matcher,
                                        "description": description,
                                    }
                                # 检查别名
                                if "_aliases" in state:
                                    aliases = state["_aliases"]
                                    for alias in aliases:
                                        if isinstance(alias, (str, tuple)):
                                            # 如果是元组，取第一个元素作为命令名
                                            if isinstance(alias, tuple):
                                                alias = alias[0]
                                            if isinstance(alias, str):
                                                description = f"命令: /{alias}"
                                                commands[alias] = {
                                                    "matcher": matcher,
                                                    "description": description,
                                                }
                    else:
                        # 如果无法通过 get_plugin_by_module_name 获取插件，回退到原来的导入方式
                        matcher_file = module_dir / "matcher.py"
                        if matcher_file.exists():
                            module_name = f"nonebot_plugin_icey.modules.{module_dir.name}.matcher"
                            try:
                                module = importlib.import_module(module_name)

                                # 遍历模块中的所有对象，查找 Matcher 对象
                                for name, obj in inspect.getmembers(module):
                                    if hasattr(obj, "__class__") and obj.__class__.__name__ == "Matcher":
                                        # 检查对象名是否以 cmd_ 开头，这通常是命令匹配器的命名约定
                                        if name.startswith("cmd_") or name.startswith("command_"):
                                            # 尝试获取命令名称
                                            if hasattr(obj, "_default_state"):
                                                state = obj._default_state
                                                # 获取命令名称
                                                if "_sub_cmd" in state:
                                                    cmd_name = state["_sub_cmd"]
                                                    # 为命令生成描述
                                                    description = f"命令: /{cmd_name}"
                                                    commands[cmd_name] = {
                                                        "matcher": obj,
                                                        "description": description,
                                                    }
                                                # 检查别名
                                                if "_aliases" in state:
                                                    aliases = state["_aliases"]
                                                    for alias in aliases:
                                                        if isinstance(alias, (str, tuple)):
                                                            # 如果是元组，取第一个元素作为命令名
                                                            if isinstance(alias, tuple):
                                                                alias = alias[0]
                                                            if isinstance(alias, str):
                                                                description = f"命令: /{alias}"
                                                                commands[alias] = {
                                                                    "matcher": obj,
                                                                    "description": description,
                                                                }
                            except ImportError as e:
                                # 如果导入失败，跳过该模块
                                logger.error(f"无法导入模块 {module_name}: {e}")
                                continue
                            except Exception as e:
                                # 其他错误也跳过
                                logger.error(f"扫描模块 {module_name} 时出错: {e}")
                                continue
                except Exception as e:
                    # 如果 get_plugin_by_module_name 失败，记录错误并跳过
                    logger.error(f"无法获取插件 {plugin_module_name}: {e}")
                    continue
    except Exception as e:
        logger.error(f"动态扫描模块时出错: {e}")

    # 然后手动导入已知的命令作为补充
    # welcome 模块命令
    try:
        from ..welcome.matcher import (
            cmd_cleanwelcome,
            cmd_goodbye,
            cmd_reset_goodbye,
            cmd_reset_welcome,
            cmd_set_goodbye,
            cmd_set_welcome,
            cmd_welcome,
        )

        commands["welcome"] = {
            "matcher": cmd_welcome,
            "description": "入群欢迎功能开关，用法: /welcome [on/off]",
        }
        commands["goodbye"] = {
            "matcher": cmd_goodbye,
            "description": "退群通知功能开关，用法: /goodbye [on/off]",
        }
        commands["setwelcome"] = {
            "matcher": cmd_set_welcome,
            "description": "设置欢迎消息，用法: /setwelcome <消息内容>",
        }
        commands["setgoodbye"] = {
            "matcher": cmd_set_goodbye,
            "description": "设置退群消息，用法: /setgoodbye <消息内容>",
        }
        commands["cleanwelcometime"] = {
            "matcher": cmd_cleanwelcome,
            "description": "设置自动删除时间，用法: /cleanwelcometime <秒数>",
        }
        commands["resetwelcome"] = {
            "matcher": cmd_reset_welcome,
            "description": "重置欢迎消息为默认值，用法: /resetwelcome",
        }
        commands["resetgoodbye"] = {
            "matcher": cmd_reset_goodbye,
            "description": "重置退群消息为默认值，用法: /resetgoodbye",
        }
    except ImportError:
        pass

    # verify 模块命令
    try:
        from ..verify.matcher import (
            clear_group,
            cmd_join_level_set,
            cmd_level_check,
            cmd_set_verify_timeout,
            cmd_verify,
        )

        commands["verify"] = {
            "matcher": cmd_verify,
            "description": "验证功能开关，用法: /verify [on/off]",
        }
        commands["levelcheck"] = {
            "matcher": cmd_level_check,
            "description": "QQ等级检查开关，用法: /levelcheck [on/off]",
        }
        commands["levelset"] = {
            "matcher": cmd_join_level_set,
            "description": "设置允许入群的最低QQ等级，用法: /levelset <等级>",
        }
        commands["verifytime"] = {
            "matcher": cmd_set_verify_timeout,
            "description": "设置验证超时时间，用法: /verifytime <秒数>",
        }
        commands["cler"] = {
            "matcher": clear_group,
            "description": "清理等级不足的群成员，用法: /cler",
        }
    except ImportError:
        pass

    # common 模块命令
    try:
        from ...common.matcher import cmd_set_lang

        commands["setlang"] = {
            "matcher": cmd_set_lang,
            "description": "设置群语言，用法: /setlang <语言代码>",
        }
    except ImportError:
        pass

    # 为已知命令添加更详细的描述（如果还没有的话）
    detailed_descriptions = {
        "welcome": "入群欢迎功能开关，用法: /welcome [on/off]",
        "goodbye": "退群通知功能开关，用法: /goodbye [on/off]",
        "setwelcome": "设置欢迎消息，用法: /setwelcome <消息内容>",
        "setgoodbye": "设置退群消息，用法: /setgoodbye <消息内容>",
        "setautodel": "设置自动删除时间，用法: /setautodel <秒数>",
        "resetwelcome": "重置欢迎消息为默认值，用法: /resetwelcome",
        "resetgoodbye": "重置退群消息为默认值，用法: /resetgoodbye",
        "verify": "验证功能开关，用法: /verify [on/off]",
        "levelcheck": "QQ等级检查开关，用法: /levelcheck [on/off]",
        "levelset": "设置允许入群的最低QQ等级，用法: /levelset <等级>",
        "verifytime": "设置验证超时时间，用法: /verifytime <秒数>",
        "cler": "清理等级不足的群成员，用法: /cler",
        "setlang": "设置群语言，用法: /setlang <语言代码>",
    }

    for cmd_name, description in detailed_descriptions.items():
        if cmd_name in commands and commands[cmd_name]["description"].startswith("命令:"):
            commands[cmd_name]["description"] = description

    return commands


# 创建 help 命令
cmd_help = on_command("help", aliases={"帮助"}, priority=29, block=True)


@cmd_help.handle()
async def handle_help(bot: Bot, event: GroupMessageEvent, matcher: Matcher, args: Message = CommandArg()):
    """
    处理 /help 命令
    """
    all_commands = get_all_commands()

    # 获取群组语言设置
    group_id = str(event.group_id)
    conf = await get_config(group_id)
    lang = conf.group.language if conf and conf.group else "zh"

    # 如果有参数，显示特定命令的帮助
    arg = args.extract_plain_text().strip()
    if arg:
        if arg in all_commands:
            cmd_info = all_commands[arg]
            response = LangManager.get(lang, "help_specific_cmd", cmd=arg, desc=cmd_info["description"])
            await matcher.finish(response)
        else:
            response = LangManager.get(lang, "help_cmd_not_found", cmd=arg)
            await matcher.finish(response)
    # 显示所有命令
    elif all_commands:
        help_text = LangManager.get(lang, "help_title") + "\n\n"

        # 按模块分组显示命令
        welcome_cmds = {}
        verify_cmds = {}
        common_cmds = {}
        other_cmds = {}

        for cmd_name, cmd_info in all_commands.items():
            desc = cmd_info["description"]
            if any(w in desc.lower() for w in ["welcome", "wel", "gdb", "goodbye"]):
                welcome_cmds[cmd_name] = desc
            elif any(w in desc.lower() for w in ["verify", "vy", "level", "check", "cler", "cl"]):
                verify_cmds[cmd_name] = desc
            elif "lang" in desc.lower():
                common_cmds[cmd_name] = desc
            else:
                other_cmds[cmd_name] = desc

        # 显示欢迎模块命令
        if welcome_cmds:
            help_text += LangManager.get(lang, "help_welcome_section") + "\n"
            for cmd_name, desc in welcome_cmds.items():
                usage = desc.split("，用法:")[1] if "，用法:" in desc else desc
                help_text += LangManager.get(lang, "help_cmd_format", cmd_name=cmd_name, usage=usage) + "\n"
            help_text += "\n"

        # 显示验证模块命令
        if verify_cmds:
            help_text += LangManager.get(lang, "help_verify_section") + "\n"
            for cmd_name, desc in verify_cmds.items():
                usage = desc.split("，用法:")[1] if "，用法:" in desc else desc
                help_text += LangManager.get(lang, "help_cmd_format", cmd_name=cmd_name, usage=usage) + "\n"
            help_text += "\n"

        # 显示通用模块命令
        if common_cmds:
            help_text += LangManager.get(lang, "help_common_section") + "\n"
            for cmd_name, desc in common_cmds.items():
                usage = desc.split("，用法:")[1] if "，用法:" in desc else desc
                help_text += LangManager.get(lang, "help_cmd_format", cmd_name=cmd_name, usage=usage) + "\n"
            help_text += "\n"

        # 显示其他命令
        if other_cmds:
            help_text += LangManager.get(lang, "help_other_section") + "\n"
            for cmd_name, desc in other_cmds.items():
                usage = desc.split("，用法:")[1] if "，用法:" in desc else desc
                help_text += LangManager.get(lang, "help_cmd_format", cmd_name=cmd_name, usage=usage) + "\n"
            help_text += "\n"

        help_text += LangManager.get(lang, "help_tip")
        await matcher.finish(help_text)
    else:
        response = LangManager.get(lang, "help_no_commands")
        await matcher.finish(response)
