# IceyGroupManager User Guide

## Introduction

IceyGroupManager is a powerful NoneBot2 QQ group management plugin that provides various group management features such as welcome messages for new members, departure notifications, member verification, message filtering, and more. (More features coming soon...)

## Configuration

The following options can be configured in the `.env` file:

```env
# Welcome message template. {user} will be replaced with a user mention.
welcome_message="🎉 Welcome {user} to the group!"

# Goodbye message template. {user} will be replaced with a user mention.
goodbye_message="Sadly, {user} has left the group."

# Automatic deletion time for welcome messages (in seconds). 0 means no deletion.
welcome_auto_delete_time=30

# Default language
lang=en
```

## Feature Modules

### 1. Welcome Module

#### Basic Commands

| Command | Description | Usage |
|------|------|------|
| `/welcome` | Toggle welcome feature | `/welcome [on/off]` |
| `/goodbye` | Toggle goodbye notification feature | `/goodbye [on/off]` |
| `/setwelcome` | Set welcome message | `/setwelcome <message>` |
| `/setgoodbye` | Set goodbye message | `/setgoodbye <message>` |
| `/cleanwelcometime` | Set automatic deletion time | `/cleanwelcometime <seconds>` |
| `/resetwelcome` | Reset welcome message to default | `/resetwelcome` |
| `/resetgoodbye` | Reset goodbye message to default | `/resetgoodbye` |

#### Usage Examples

1. Enable welcome messages:
```
/welcome on
```

2. Set a custom welcome message:
```
/setwelcome Welcome new friend {user}! Please read the group rules in the announcement.
```

3. Set welcome message auto-deletion time to 60 seconds:
```
/cleanwelcometime 60
```

4. View current welcome settings:
```
/welcome
```

### 2. Verification Module

#### Basic Commands

| Command | Description | Usage |
|------|------|------|
| `/verify` | Toggle verification feature | `/verify [on/off]` |
| `/levelcheck` | Toggle QQ level check | `/levelcheck [on/off]` |
| `/levelset` | Set minimum QQ level required to join | `/levelset <level>` |
| `/verifytime` | Set verification timeout | `/verifytime <seconds>` |
| `/clear` | Clean up members with insufficient QQ level | `/clear` |

#### Usage Examples

1. Enable join verification:
```
/verify on
```

2. Enable QQ level check and set minimum level to 10:
```
/levelcheck on
/levelset 10
```

3. Set verification timeout to 120 seconds:
```
/verifytime 120
```

4. View current verification settings:
```
/verify
```

#### Verification Process

1. When a user joins the group, if verification is enabled, the bot sends a math problem.
2. The user must answer correctly within the specified time.
3. After a correct answer, the user receives a welcome message.
4. If the answer is wrong or times out, the user is kicked from the group.

### 3. Filter Module

#### Basic Commands

| Command | Description | Usage |
|------|------|------|
| `/filter` | Add a filter rule | `/filter <trigger> <reply>` |
| `/stop` | Delete a filter rule | `/stop <trigger>` |
| `/stopall` | Delete all filter rules | `/stopall` |
| `/filters` | View all filter rules | `/filters` |

#### Usage Examples

1. Add a text reply rule:
```
/filter Hello Hi! I'm the Icey bot.
```

2. Add a prefix matching rule:
```
/filter prefix:weather The weather is nice today.
```

3. Add an exact matching rule:
```
/filter exact:bot I am a bot.
```

4. Add multiple triggers:
```
/filter (Hello,hi,hello) Hi there!
```

5. Add an image reply (reply to an image message):
```
/filter sticker
```

6. View all filter rules:
```
/filters
```

7. Delete a specific filter rule:
```
/stop Hello
```

#### Advanced Usage

1. Use the `{user}` variable to mention the user in replies:
```
/filter welcome Welcome {user}!
```

2. Use the `{replytag}` variable to reply to the mentioned user:
```
/filter thanks You're welcome {replytag}
```

### 4. General Module

#### Basic Commands

| Command | Description | Usage |
|------|------|------|
| `/setlang` | Set group language | `/setlang <language code>` |
| `/help` | View help information | `/help [command name]` |

#### Usage Examples

1. Set group language to Chinese:
```
/setlang zh
```

2. View all available commands:
```
/help
```

3. View help for a specific command:
```
/help welcome
```

## Permissions

Most management commands require administrator permissions, including:
- Group owner
- Group administrator
- Bot superusers

>Non authorized users who match instructions will be banned for 10 minutes, and further attempts will be made to expand more configurations

## FAQ

### Q: What if verification conflicts with welcome features?

A: The plugin automatically handles priority. Verification takes precedence over welcome messages. Welcome messages are sent only after successful verification.

### Q: How to set different configurations for different groups?

A: All configurations are stored independently per group. Each group can have different settings.

### Q: Does the filter support regular expressions?

A: Regular expressions are not currently supported, but three matching modes are available:
- Contains match (default)
- Exact match (use `exact:` prefix)
- Prefix match (use `prefix:` prefix)

### Q: How to backup or migrate configurations?

A: Configurations are stored in the database and can be migrated by backing up the database.

## Technical Support

For issues or suggestions, please visit:
- GitHub: https://github.com/Fansirsqi/nonebot-plugin-icey
- Issues: https://github.com/Fansirsqi/nonebot-plugin-icey/issues
