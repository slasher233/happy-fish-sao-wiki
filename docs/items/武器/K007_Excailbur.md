# K007 · Excailbur

> **分类**：武器　**品质**：传闻　**类型**：Artifact　**物品等级**：8　**价格**：0 金

**物品 ID**：`K007`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 伤害增加 (%) | 0.1 | `X00T` | `Roa1` | 1 |
| 防御增加 | 0 | `X00T` | `Roa2` | 1 |
| 生命值恢复速度 | 0 | `X00T` | `Roa3` | 1 |
| 魔法再生 | 0 | `X00T` | `Roa4` | 1 |
| 喜欢进攻 | 0 | `X00T` | `Roa5` | 1 |
| 喜欢友好 | 0 | `X00T` | `Roa6` | 1 |
| 最多单位 | 0 | `X00T` | `Roa7` | 1 |
| 敏捷奖励 | 333 | `X00L` | `Iagi` | 1 |
| 智力奖励 | 333 | `X00L` | `Iint` | 1 |
| 力量奖励 | 333 | `X00L` | `Istr` | 1 |
| 隐藏按钮 | 0 | `X00L` | `Ihid` | 1 |
| 取得最大生命值 | 30000 | `X00S` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `X00T` | 物品_阿瓦隆 | 魔法施放时间间隔=60, 魔法消耗=100, 伤害增加 (%)=0.1, 防御增加=0, 生命值恢复速度=0, 魔法再生=0, 喜欢进攻=0, 喜欢友好=0, 最多单位=0 | 增加周围友军单位25%的攻击力。 / 持续45秒。 |
| `X00L` | 全能力增加333 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=333, 智力奖励=333, 力量奖励=333, 隐藏按钮=0 | — |
| `X00S` | 生命值3W | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=30000 | — |

### 游戏内说明（原文）

> 武器
>
> 筋力:333
> 敏捷:333
> 体力:333
> 攻速:120
> 生命值:30000
> 能力:阿瓦隆(SSR级)(CD:60s)
> 能力:遥远的理想乡(SSR级)(CD:120s)
> 品质:传闻
>
> 王者只是历史所记载的故事,没有人知道那英勇的事迹!

**提示工具（Tip）**：

```text
Excailbur
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `P2EX\saberex.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|n|cffffd700筋力:333|n敏捷:333|n体力:333|n攻速:120|n生命值:30000|n能力:阿瓦隆(SSR级)(CD:60s)|n能力:遥远的理想乡(SSR级)(CD:120s)|n品质:传闻|n|n王者只是历史所记载的故事,没有人知道那英勇的事迹!|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|cffff6600Excailbur|r`　*(名字)*
    - `utip` Tip = `|cffff6600Excailbur|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|n|cffffd700筋力:333|n敏捷:333|n体力:333|n攻速:120|n生命值:30000|n能力:阿瓦隆(SSR级)(CD:60s)|n能力:遥远的理想乡(SSR级)(CD:120s)|n品质:传闻|n|n王者只是历史所记载的故事,没有人知道那英勇的事迹!|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `X00T,X00L,X00S`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Artifact`　*(分类)*
    - `iclb` colorB = `20`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `X00T`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `P2EX\war3mapImported\wuqi2.mdx`　*(已使用的模型)*
    - `igol` goldcost = `0`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `10`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `0`　*(易腐烂的)*
    - `iprn` pickRandom = `1`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `126`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `1`　*(最大储存)*
    - `istr` stockRegen = `120`　*(佣兵招募间隔)*
    - `isst` stockStart = `0`　*(佣兵招募时间)*
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `0`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
