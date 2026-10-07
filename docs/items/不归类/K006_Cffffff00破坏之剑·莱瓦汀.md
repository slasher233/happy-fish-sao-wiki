# K006 · |Cffffff00破坏之剑·莱瓦汀

> **分类**：不归类　**品质**：礼物　**类型**：Permanent　**物品等级**：8　**价格**：1000 金

**物品 ID**：`K006`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击奖励 | 100 | `X009` | `Iatt` | 1 |
| 攻击速度增加 | 0.5 | `Z04T` | `Isx1` | 1 |
| 敏捷奖励 | 30 | `Z07R` | `Iagi` | 1 |
| 智力奖励 | 30 | `Z07R` | `Iint` | 1 |
| 力量奖励 | 30 | `Z07R` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z07R` | `Ihid` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `X009` | 增加攻击100 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击奖励=100 | — |
| `Z04T` | 增加攻击速度50 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击速度增加=0.5 | — |
| `Z07R` | 全能力30 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=30, 智力奖励=30, 力量奖励=30, 隐藏按钮=0 | — |

### 游戏内说明（原文）

> -副武器
> 攻击:100
> 攻速:50
> 筋力:30
> 敏捷:30
> 体力:30
> 能力:破坏之剑（S）
> 能力:鲜血之拥（S）
> 能力:吸血鬼的病原体LV5（B)
> 能力:隔绝斩击LV5(C)
> 品质:礼物
>
> 传说中破坏一切的魔剑，拥有能令红魔馆瞬间爆炸的力量.(专属ID:蕾米莉亚·斯卡雷特)

**提示工具（Tip）**：

```text
|Cffffff00破坏之剑·莱瓦汀
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `P2EX\ReplaceableTextures\CommandButtons\BTN201620.blp`　*(界面图标)*
    - `ides` Description = `|cff9db9eb-副武器|n攻击:100|n攻速:50|n筋力:30|n敏捷:30|n体力:30|n能力:破坏之剑（S）|n能力:鲜血之拥（S）|n能力:吸血鬼的病原体LV5（B)|n能力:隔绝斩击LV5(C)|n品质:礼物|n|n传说中破坏一切的魔剑，拥有能令红魔馆瞬间爆炸的力量.(专属ID:蕾米莉亚·斯卡雷特)`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|Cffffff00破坏之剑·莱瓦汀|r`　*(名字)*
    - `utip` Tip = `|Cffffff00破坏之剑·莱瓦汀|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff9db9eb-副武器|n攻击:100|n攻速:50|n筋力:30|n敏捷:30|n体力:30|n能力:破坏之剑（S）|n能力:鲜血之拥（S）|n能力:吸血鬼的病原体LV5（B)|n能力:隔绝斩击LV5(C)|n品质:礼物|n|n传说中破坏一切的魔剑，拥有能令红魔馆瞬间爆炸的力量.(专属ID:蕾米莉亚·斯卡雷特)`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `X009,Z04T,Z07R`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Permanent`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z1CR`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
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
