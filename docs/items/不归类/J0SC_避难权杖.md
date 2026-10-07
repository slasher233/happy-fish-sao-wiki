# J0SC · 避难权杖

> **分类**：不归类　**品质**：—　**类型**：Purchasable　**物品等级**：0　**价格**：250 金

**物品 ID**：`J0SC`　·　**原型**：`ssan`（避难权杖）　·　**版本**：v1.0 正式版

**热键**：`N`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 建造类型允许 | 15 | `Z1D1` | `Nsa1` | 1 |
| 英雄回复延迟 | 1 | `Z1D1` | `Nsa2` | 1 |
| 单位回复延迟 | 5 | `Z1D1` | `Nsa3` | 1 |
| 魔法伤害减少 | 10 | `Z1D1` | `Nsa4` | 1 |
| 每秒生命值 | 15 | `Z1D1` | `Nsa5` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z1D1` | 避难权杖 | 魔法施放时间间隔=45, 魔法消耗=0, 建造类型允许=15, 英雄回复延迟=1, 单位回复延迟=5, 魔法伤害减少=10, 每秒生命值=15 | — |

### 游戏内说明（原文）

> T将目标单位传送到你最高等级的主基地,让其处于昏晕状态并以每秒15点的速度来恢复其生命值直到该单位补满生命值为止。

**提示工具（Tip）**：

```text
购买避难权杖(N)
```

## 获取方式

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 神秘藏宝室 | `u0DK` | `umki` | Makeitems 人造的物品 | note_log/index/w3u_verify.txt:515160 |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNStaffOfSanctuary.blp`　*(界面图标)*
    - `ubpx` Buttonpos = `1`　*(按钮位置(X))*
    - `ubpy` Buttonpos = `2`　*(按钮位置(Y))*
    - `ides` Description = `传送并医疗某个单位。`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `N`　*(热键)*
    - `ilev` Level = `0`　*(等级)*
    - `unam` Name = `避难权杖`　*(名字)*
    - `ureq` Requires = `u0CW`　*(要求)*
    - `utip` Tip = `购买避难权杖(|cffffcc00N|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `T将目标单位传送到你最高等级的主基地,让其处于昏晕状态并以每秒15点的速度来恢复其生命值直到该单位补满生命值为止。`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z1D1`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Purchasable`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z1D1`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `250`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `0`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `0`　*(易腐烂的)*
    - `iprn` pickRandom = `0`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `3`　*(优先权)*
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
