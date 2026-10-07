# K0DX · |Cffffff00八云之盾

> **分类**：副武器　**品质**：传说　**类型**：Permanent　**物品等级**：82　**价格**：50000 金

**物品 ID**：`K0DX`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 防御奖励 | 50 | `V0DW` | `Idef` | 1 |
| 生命值取得 | 10000 | `V0E1` | `Ihpg` | 1 |
| 敏捷奖励 | 100 | `V0DY` | `Iagi` | 1 |
| 智力奖励 | 100 | `V0DY` | `Iint` | 1 |
| 力量奖励 | 100 | `V0DY` | `Istr` | 1 |
| 隐藏按钮 | 0 | `V0DY` | `Ihid` | 1 |
| 取得最大生命值 | 10000 | `V0E0` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `V0DW` | 增加防御50 | 魔法施放时间间隔=0, 魔法消耗=0, 防御奖励=50 | — |
| `V0E1` | 全体治疗1 | 魔法施放时间间隔=7, 魔法消耗=500, 生命值取得=10000 | — |
| `V0DY` | 筋力/敏捷/体力100 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=100, 智力奖励=100, 力量奖励=100, 隐藏按钮=0 | — |
| `V0E0` | 增加最大生命值10000 | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=10000 | — |

### 游戏内说明（原文）

> -副武器
>
> |Cffffff00筋力:100
> 敏捷:100
> 体力:100
> 防御值:50
> 生命值:10000
> 能力:誓言の守护(SR级)Cd:7）
> 品质:传说
>
> 由八云国所为公主精心打造的盾,外观非常精美,能力也非常强,曾经八云姬用此盾抵挡千敌,盾依然毫无损坏

**提示工具（Tip）**：

```text
|Cffffff00八云之盾
```

## 获取方式

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 工会:命运之夜 玩家:CD | `x0E6` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:831975 |


**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `n029` Lv30:沙漠害虫 | ChooseRandomItemExBJ(level, itemClass) | — | `33426` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `NB22\ReplaceableTextures\CommandButtons\BTNZBCT218.blp`　*(界面图标)*
    - `ides` Description = `|cff9db9eb-副武器|r|n|n|Cffffff00筋力:100|n敏捷:100|n体力:100|n防御值:50|n生命值:10000|n能力:誓言の守护(SR级)Cd:7）|n品质:传说|n|n由八云国所为公主精心打造的盾,外观非常精美,能力也非常强,曾经八云姬用此盾抵挡千敌,盾依然毫无损坏|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `82`　*(等级)*
    - `unam` Name = `|Cffffff00八云之盾|r`　*(名字)*
    - `utip` Tip = `|Cffffff00八云之盾|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff9db9eb-副武器|r|n|n|Cffffff00筋力:100|n敏捷:100|n体力:100|n防御值:50|n生命值:10000|n能力:誓言の守护(SR级)Cd:7）|n品质:传说|n|n由八云国所为公主精心打造的盾,外观非常精美,能力也非常强,曾经八云姬用此盾抵挡千敌,盾依然毫无损坏|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `V0DW,V0E1,V0DY,V0E0`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Permanent`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `V0E1`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `NB22\war3mapImported\dunpai2.mdx`　*(已使用的模型)*
    - `igol` goldcost = `50000`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `500`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `82`　*(等级(无类别的))*
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
