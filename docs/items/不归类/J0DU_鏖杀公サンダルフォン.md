# J0DU · 鏖杀公サンダルフォン

> **分类**：不归类　**品质**：—　**类型**：Miscellaneous　**物品等级**：8　**价格**：1000 金

**物品 ID**：`J0DU`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

> 🔒 **英雄专属**：仅 冬(`H014`) 可以拾取，其他英雄拾取会被立即移除（`war3map.j:87189`）。
> 同时属于 `EXEQ_DropPool[8]`（英雄专属掉落池，`war3map.j:88781-88814`）。

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 敏捷奖励 | 220 | `Z12W` | `Iagi` | 1 |
| 智力奖励 | 220 | `Z12W` | `Iint` | 1 |
| 力量奖励 | 220 | `Z12W` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z12W` | `Ihid` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z12W` | 筋力/敏捷/体力220 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=220, 智力奖励=220, 力量奖励=220, 隐藏按钮=0 | — |

### 游戏内说明（原文）

> 专属道具(不归类任何)
>
> 筋力:100
> 敏捷:100
> 体力:100
> 能力:神裂威力上升100%
> 能力:乱舞威力上升100%
>
> 十香的专属武器

**提示工具（Tip）**：

```text
鏖杀公サンダルフォン
```

## 获取方式

**BOSS 专属掉落池（`HF22SD_Pool`）**

| 池 | 序号 | 来源 BOSS | 池定义行 | 掉落行 |
| --- | --- | --- | --- | --- |
| HF22SD_Pool | 8 | `n028` Lv50:花姬 | `109601` | `109207` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_21721a75f391875fc4e0.blp`　*(界面图标)*
    - `ides` Description = `|cffff0000专属道具(不归类任何)|n|n筋力:220|n敏捷:220|n体力:220|n能力:神裂威力上升100%|n能力:乱舞威力上升100%|n|n十香的专属武器|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|cffff0000鏖杀公サンダルフォン|r`　*(名字)*
    - `utip` Tip = `|cffff0000鏖杀公サンダルフォン|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffff0000专属道具(不归类任何)|n|n筋力:100|n敏捷:100|n体力:100|n能力:神裂威力上升100%|n能力:乱舞威力上升100%|n|n十香的专属武器|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z12W`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `iclb` colorB = `0`　*(染色 3 (蓝色))*
    - `iclg` colorG = `55`　*(染色 2 (绿色))*
    - `iclr` colorR = `55`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z1CR`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `P2\war3mapImported\quantao2.mdx`　*(已使用的模型)*
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
    - `iusa` usable = `0`　*(主动使用)*
    - `iuse` uses = `0`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
