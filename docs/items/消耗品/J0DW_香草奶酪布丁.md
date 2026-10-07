# J0DW · 香草奶酪布丁

> **分类**：消耗品　**品质**：—　**类型**：Charged　**物品等级**：8　**价格**：1500 金

**物品 ID**：`J0DW`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 敏捷奖励 | 0 | `Z0D9` | `Iagi` | 1 |
| 智力奖励 | 0 | `Z0D9` | `Iint` | 1 |
| 力量奖励 | 1 | `Z0D9` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z0D9` | `Ihid` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z0D9` | 食物筋力+1 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=0, 智力奖励=0, 力量奖励=1, 隐藏按钮=0 | — |

### 游戏内说明（原文）

> 能力:永久提升自身属性筋力+1
>
>
> 香草和奶酪的搭配很完美啊

**提示工具（Tip）**：

```text
香草奶酪布丁
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I0E5` | 香草奶酪布丁 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_8a19f4dbb9e789ed895e.blp`　*(界面图标)*
    - `ides` Description = `|cff00ffff能力:永久提升自身属性筋力+1|n|r|n|n|cffff69b4香草和奶酪的搭配很完美啊|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `香草奶酪布丁`　*(名字)*
    - `utip` Tip = `香草奶酪布丁`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff00ffff能力:永久提升自身属性筋力+1|n|r|n|n|cffff69b4香草和奶酪的搭配很完美啊|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z0D9`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Charged`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z0D9`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `1500`　*(金子消耗)*
    - `iicd` ignoreCD = `1`　*(忽视延迟)*
    - `ilum` lumbercost = `2`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `10`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `1`　*(易腐烂的)*
    - `iprn` pickRandom = `1`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `126`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `1`　*(最大储存)*
    - `istr` stockRegen = `0`　*(佣兵招募间隔)*
    - `isst` stockStart = `0`　*(佣兵招募时间)*
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `1`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
