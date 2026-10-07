# J00F · HP小型恢复药水

> **分类**：消耗品　**品质**：—　**类型**：Charged　**物品等级**：3　**价格**：100 金

**物品 ID**：`J00F`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`Q`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 生命值取得 | 500 | `Z03O` | `Ihpg` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z03O` | +增加HP500 | 魔法施放时间间隔=7, 魔法消耗=0, 生命值取得=500 | — |

### 游戏内说明（原文）

> 能力:恢复自身生命点500+（筋力*1）
>
> CD时间:7秒
> 施法距离:自身

**提示工具（Tip）**：

```text
购买HP小型恢复药水(Q)
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNPotionGreenSmall.blp`　*(界面图标)*
    - `ides` Description = `|cff00ffff能力:恢复自身生命点500+（筋力*1）|n|nCD时间:7秒|n施法距离:自身|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `Q`　*(热键)*
    - `ilev` Level = `3`　*(等级)*
    - `unam` Name = `HP小型恢复药水`　*(名字)*
    - `utip` Tip = `购买HP小型恢复药水(|cffffcc00Q|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff00ffff能力:恢复自身生命点500+（筋力*1）|n|nCD时间:7秒|n施法距离:自身|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z03O`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Charged`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z03O`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `100`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `3`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `1`　*(易腐烂的)*
    - `iprn` pickRandom = `1`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `121`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `1`　*(最大储存)*
    - `istr` stockRegen = `0`　*(佣兵招募间隔)*
    - `isst` stockStart = `0`　*(佣兵招募时间)*
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `10`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
