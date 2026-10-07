# J0HE · 自然之剑

> **分类**：不归类　**品质**：专属　**类型**：Miscellaneous　**物品等级**：2　**价格**：150 金

**物品 ID**：`J0HE`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`2`

> 🔒 **英雄专属**：仅 兄控万岁(`H01U`) 可以拾取，其他英雄拾取会被立即移除（`war3map.j:87204`）。
> 同时属于 `EXEQ_DropPool[16]`（英雄专属掉落池，`war3map.j:88781-88814`）。

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击奖励 | 8000 | `Z0QK` | `Iatt` | 1 |
| 敏捷奖励 | 150 | `Z0PZ` | `Iagi` | 1 |
| 智力奖励 | 0 | `Z0PZ` | `Iint` | 1 |
| 力量奖励 | 150 | `Z0PZ` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z0PZ` | `Ihid` | 1 |
| 取得最大生命值 | 5000 | `Z0CO` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z0QK` | 增加攻击力8000 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击奖励=8000 | — |
| `Z0PZ` | 筋力150敏捷150 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=150, 智力奖励=0, 力量奖励=150, 隐藏按钮=0 | — |
| `Z0CO` | 增加最大生命5000 | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=5000 | — |

### 游戏内说明（原文）

> 不归类
>
> 攻击力:8000
> 筋力:150
> 敏捷:150
> 生命值:5000
> 能力:亚当之力Lv2(S级)
> 能力:夏娃之力Lv2(S级)
> 品质:专属
> 只能莉法所用
>
> 伟大的精灵王使用一生所学的魔法力量制造出的武器,自然之剑(精灵之剑),曾经一剑就将破坏之王致死,所有的人类包括神都震惊了,后放皇室保管,被神秘盗贼所盗走!无人知此剑归去

**提示工具（Tip）**：

```text
自然之剑(精灵之剑)
```

## 获取方式

**BOSS 专属掉落池（`HF22SD_Pool`）**

| 池 | 序号 | 来源 BOSS | 池定义行 | 掉落行 |
| --- | --- | --- | --- | --- |
| HF22SD_Pool | 16 | `n028` Lv50:花姬 | `109609` | `109207` |


## 合成与材料用途

**说明文本中提到本物品的物品**（文本匹配，不等于真实配方）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I0HI` | 自然之剑 |


??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNStaffOfPurification.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520不归类|r|n|n|cffdeb887攻击力:8000|n筋力:150|n敏捷:150|n生命值:5000|n能力:亚当之力Lv2(S级)|n能力:夏娃之力Lv2(S级)|n品质:专属|n只能莉法所用|n|r|n|cff0066cc伟大的精灵王使用一生所学的魔法力量制造出的武器,自然之剑(精灵之剑),曾经一剑就将破坏之王致死,所有的人类包括神都震惊了,后放皇室保管,被神秘盗贼所盗走!无人知此剑归去|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `2`　*(热键)*
    - `ilev` Level = `2`　*(等级)*
    - `unam` Name = `|cffbdb76b自然之剑|r`　*(名字)*
    - `utip` Tip = `|cffbdb76b自然之剑|r(|cffff0000精灵之剑|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520不归类|r|n|n|cffdeb887攻击力:8000|n筋力:150|n敏捷:150|n生命值:5000|n能力:亚当之力Lv2(S级)|n能力:夏娃之力Lv2(S级)|n品质:专属|n只能莉法所用|n|r|n|cff0066cc伟大的精灵王使用一生所学的魔法力量制造出的武器,自然之剑(精灵之剑),曾经一剑就将破坏之王致死,所有的人类包括神都震惊了,后放皇室保管,被神秘盗贼所盗走!无人知此剑归去|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z0QK,Z0PZ,Z0CO`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `AIde`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `150`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `2`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `0`　*(易腐烂的)*
    - `iprn` pickRandom = `1`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `80`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `1`　*(最大储存)*
    - `istr` stockRegen = `90`　*(佣兵招募间隔)*
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
