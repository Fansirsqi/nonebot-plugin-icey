# IceyGroupManager 食用指南

## 简介

IceyGroupManager 是一个功能强大的 NoneBot2 QQ群管理插件，提供入群欢迎、退群通知、入群验证、消息过滤等多种群管理功能。(更多功能敬请期待...)


## 配置

在 `.env` 文件中可以配置以下选项：

```env
# 欢迎消息模板，{user} 会被替换为用户@
welcome_message="🎉 欢迎 {user} 加入本群！"

# 退群消息模板，{user} 会被替换为用户@
goodbye_message="很遗憾 {user} 已离开本群。"

# 欢迎消息自动撤回时间（秒），0 表示不撤回
welcome_auto_delete_time=30

# 默认语言
lang=zh
```

## 功能模块

### 1. 欢迎模块

#### 基本命令

| 命令 | 说明 | 用法 |
|------|------|------|
| `/welcome` | 入群欢迎功能开关 | `/welcome [on/off]` |
| `/goodbye` | 退群通知功能开关 | `/goodbye [on/off]` |
| `/setwelcome` | 设置欢迎消息 | `/setwelcome <消息内容>` |
| `/setgoodbye` | 设置退群消息 | `/setgoodbye <消息内容>` |
| `/cleanwelcometime` | 设置自动删除时间 | `/cleanwelcometime <秒数>` |
| `/resetwelcome` | 重置欢迎消息为默认值 | `/resetwelcome` |
| `/resetgoodbye` | 重置退群消息为默认值 | `/resetgoodbye` |

#### 使用示例

1. 开启入群欢迎：
```
/welcome on
```

2. 设置自定义欢迎消息：
```
/setwelcome 欢迎新朋友 {user}！请阅读群公告了解群规。
```

3. 设置欢迎消息自动撤回时间为 60 秒：
```
/cleanwelcometime 60
```

4. 查看当前欢迎设置：
```
/welcome
```

### 2. 验证模块

#### 基本命令

| 命令 | 说明 | 用法 |
|------|------|------|
| `/verify` | 验证功能开关 | `/verify [on/off]` |
| `/levelcheck` | QQ等级检查开关 | `/levelcheck [on/off]` |
| `/levelset` | 设置允许入群的最低QQ等级 | `/levelset <等级>` |
| `/verifytime` | 设置验证超时时间 | `/verifytime <秒数>` |
| `/clear` | 清理等级不足的群成员 | `/clear` |

#### 使用示例

1. 开启入群验证：
```
/verify on
```

2. 开启QQ等级检查，并设置最低等级为10级：
```
/levelcheck on
/levelset 10
```

3. 设置验证超时时间为120秒：
```
/verifytime 120
```

4. 查看当前验证设置：
```
/verify
```

#### 验证流程

1. 用户加入群组时，如果开启了验证功能，机器人会发送一道数学题
2. 用户需要在指定时间内回答正确
3. 回答正确后，用户会收到欢迎消息
4. 回答错误或超时，用户会被踢出群组

### 3. 过滤器模块

#### 基本命令

| 命令 | 说明 | 用法 |
|------|------|------|
| `/filter` | 添加过滤规则 | `/filter <触发词> <回复内容>` |
| `/stop` | 删除过滤规则 | `/stop <触发词>` |
| `/stopall` | 删除所有过滤规则 | `/stopall` |
| `/filters` | 查看所有过滤规则 | `/filters` |

#### 使用示例

1. 添加文本回复规则：
```
/filter 你好 你好！我是Icey机器人
```

2. 添加前缀匹配规则：
```
/filter prefix:天气 今天天气不错
```

3. 添加精确匹配规则：
```
/filter exact:机器人 我是机器人
```

4. 添加多个触发词：
```
/filter (你好,hi,hello) 你好！
```

5. 添加图片回复（回复一条图片消息）：
```
/filter 表情包
```

6. 查看所有过滤规则：
```
/filters
```

7. 删除特定过滤规则：
```
/stop 你好
```

#### 高级用法

1. 使用 `{user}` 变量在回复中提及用户：
```
/filter 欢迎 欢迎 {user}！
```

2. 使用 `{replytag}` 变量回复被回复的用户：
```
/filter 谢谢 不客气 {replytag}
```

### 4. 通用模块

#### 基本命令

| 命令 | 说明 | 用法 |
|------|------|------|
| `/setlang` | 设置群语言 | `/setlang <语言代码>` |
| `/help` | 查看帮助信息 | `/help [命令名]` |

#### 使用示例

1. 设置群语言为中文：
```
/setlang zh
```

2. 查看所有可用命令：
```
/help
```

3. 查看特定命令的帮助：
```
/help welcome
```

## 权限说明

大部分管理命令需要管理员权限，包括：
- 群主
- 群管理员
- 机器人超级用户

> 非权限允许的用户匹配到指令，会被禁言10分钟，后续将尝试扩展更多配置

## 常见问题

### Q: 验证功能与欢迎功能冲突怎么办？

A: 插件已自动处理优先级，验证功能会优先于欢迎功能执行。只有验证通过后才会发送欢迎消息。

### Q: 如何设置不同群的不同配置？

A: 所有配置都是按群组独立存储的，每个群可以有不同的设置。

### Q: 过滤器支持正则表达式吗？

A: 目前不支持正则表达式，但支持三种匹配模式：
- 包含匹配（默认）
- 精确匹配（使用 `exact:` 前缀）
- 前缀匹配（使用 `prefix:` 前缀）

### Q: 如何备份或迁移配置？

A: 配置存储在数据库中，可以通过备份数据库来迁移配置。


## 技术支持

如有问题或建议，请访问：
- GitHub: https://github.com/Fansirsqi/nonebot-plugin-icey
- Issues: https://github.com/Fansirsqi/nonebot-plugin-icey/issues
