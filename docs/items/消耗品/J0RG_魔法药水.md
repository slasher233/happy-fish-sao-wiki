# J0RG · 魔法药水

> **分类**：消耗品　**品质**：—　**类型**：Purchasable　**物品等级**：1　**价格**：200 金

**物品 ID**：`J0RG`　·　**原型**：`pman`（魔法药水）　·　**版本**：v1.0 正式版

**热键**：`M`

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z1BI` | 能增加魔法恢复速度的物品 | 魔法施放时间间隔=20, 魔法消耗=0 | — |

### 游戏内说明（原文）

> 恢复150点的魔法值。

**提示工具（Tip）**：

```text
购买魔法药水(M)
```

## 获取方式

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 神秘藏宝室 | `u0DK` | `umki` | Makeitems 人造的物品 | note_log/index/w3u_verify.txt:515160 |
| 巫毒商店 | `u0OK` | `umki` | Makeitems 人造的物品 | note_log/index/w3u_verify.txt:574460 |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNPotionBlueSmall.blp`　*(界面图标)*
    - `ubpx` Buttonpos = `1`　*(按钮位置(X))*
    - `ubpy` Buttonpos = `1`　*(按钮位置(Y))*
    - `ides` Description = `能恢复魔法值。`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `M`　*(热键)*
    - `ilev` Level = `1`　*(等级)*
    - `unam` Name = `魔法药水`　*(名字)*
    - `ureq` Requires = `TWN2`　*(要求)*
    - `utip` Tip = `购买魔法药水(|cffffcc00M|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `恢复150点的魔法值。`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z1BI`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Purchasable`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `AIma`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `200`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `0`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `1`　*(易腐烂的)*
    - `iprn` pickRandom = `0`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `66`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `2`　*(最大储存)*
    - `istr` stockRegen = `120`　*(佣兵招募间隔)*
    - `isst` stockStart = `440`　*(佣兵招募时间)*
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `1`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
