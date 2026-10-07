# J0HH · 塞壬之手杖

> **分类**：副武器　**品质**：传说　**类型**：Permanent　**物品等级**：8　**价格**：1000 金

**物品 ID**：`J0HH`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

> 🔒 **英雄专属**：仅 优库里伍德(`H01Z`) 可以拾取，其他英雄拾取会被立即移除（`war3map.j:87207`）。
> 同时属于 `EXEQ_DropPool[31]`（英雄专属掉落池，`war3map.j:88781-88814`）。

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 跟随时间 | 0.1 | `Z0MT` | `Ncl1` | 1 |
| 目标类型 | 2 | `Z0MT` | `Ncl2` | 1 |
| 技术持续时间 | 0.1 | `Z0MT` | `Ncl4` | 1 |
| 使其他技能无效 | 1 | `Z0MT` | `Ncl5` | 1 |
| 基本顺序 ID | monsoon | `Z0MT` | `Ncl6` | 1 |
| 选项 | 1 | `Z0MT` | `Ncl3` | 1 |
| 取得最大生命值 | 15000 | `Z0KR` | `Ilif` | 1 |
| 敏捷奖励 | 0 | `Z0DS` | `Iagi` | 1 |
| 智力奖励 | 250 | `Z0DS` | `Iint` | 1 |
| 力量奖励 | 0 | `Z0DS` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z0DS` | `Ihid` | 1 |
| 每秒生命值回复 | 200 | `Z0FB` | `Ihpr` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z0MT` | 手杖 | 魔法施放时间间隔=20, 魔法消耗=0, 跟随时间=0.1, 目标类型=2, 技术持续时间=0.1, 使其他技能无效=1, 基本顺序 ID=monsoon, 选项=1 | 通向强大的守卫魔法力量。 |
| `Z0KR` | 增加最大生命1.5W | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=15000 | — |
| `Z0DS` | 增加体力250 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=0, 智力奖励=250, 力量奖励=0, 隐藏按钮=0 | — |
| `Z0FB` | 生命恢复100 | 魔法施放时间间隔=0, 魔法消耗=0, 每秒生命值回复=200 | — |

### 游戏内说明（原文）

> -副武器
>
>
> 体力:250
> 生命值:15000
> 能力:水属性Lv2
> 能力:生命恢复Lv10
> 能力:任塞之唤(S级)Cd:20）
> 品质:传说
>
> 由毁灭钻石所打造出来的武器,极为神秘

**提示工具（Tip）**：

```text
塞壬之手杖
```

## 获取方式

**BOSS 专属掉落池（`HF22SD_Pool`）**

| 池 | 序号 | 来源 BOSS | 池定义行 | 掉落行 |
| --- | --- | --- | --- | --- |
| HF22SD_Pool | 31 | `n028` Lv50:花姬 | `109624` | `109207` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_f0f0b3f97363edb6dffe.blp`　*(界面图标)*
    - `ides` Description = `|cff99b4d1-副武器|r|cff8a2be2|n|n|r|cffffd700|n体力:250|n生命值:15000|n能力:水属性Lv2|n能力:生命恢复Lv10|n能力:任塞之唤(S级)Cd:20）|n品质:传说|n|n由毁灭钻石所打造出来的武器,极为神秘|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|cffffd700塞壬之手杖|r`　*(名字)*
    - `utip` Tip = `|cffffd700塞壬之手杖|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff99b4d1-副武器|r|cff8a2be2|n|n|r|cffffd700|n体力:250|n生命值:15000|n能力:水属性Lv2|n能力:生命恢复Lv10|n能力:任塞之唤(S级)Cd:20）|n品质:传说|n|n由毁灭钻石所打造出来的武器,极为神秘|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z0MT,Z0KR,Z0DS,Z0FB`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Permanent`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z0MT`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `P2\war3mapImported\wuqi2.mdx`　*(已使用的模型)*
    - `igol` goldcost = `1000`　*(金子消耗)*
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
