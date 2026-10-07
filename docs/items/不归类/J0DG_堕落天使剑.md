# J0DG · 堕落天使剑

> **分类**：不归类　**品质**：传说　**类型**：Permanent　**物品等级**：8　**价格**：1000 金

**物品 ID**：`J0DG`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击奖励 | 300 | `Z00P` | `Iatt` | 1 |
| 攻击速度增加 | 100 | `Z09F` | `Isx1` | 1 |
| 敏捷奖励 | 120 | `Z0C9` | `Iagi` | 1 |
| 智力奖励 | 120 | `Z0C9` | `Iint` | 1 |
| 力量奖励 | 120 | `Z0C9` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z0C9` | `Ihid` | 1 |
| 生命值取得 | 10000 | `Z0AZ` | `Ihpg` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z00P` | 增加攻击300 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击奖励=300 | — |
| `Z09F` | 增加攻击速度100 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击速度增加=100 | — |
| `Z0C9` | 筋力/敏捷/体力120 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=120, 智力奖励=120, 力量奖励=120, 隐藏按钮=0 | — |
| `Z0AZ` | 降临天使 | 魔法施放时间间隔=10, 魔法消耗=0, 生命值取得=10000 | — |

### 游戏内说明（原文）

> -副武器
>
> 攻击力:300
> 筋力:120
> 敏捷:120
> 体力:120
> 攻击速度:100
> 能力:降临天使(B级)
> 能力:神判(S级)
> 品质:传说
>
> 若天使降临到你面前,那并不是所谓的天使,那只是披着天使面具的恶魔（当天使失去了心,就会变为堕落天使,也是所谓的降临天使）

**提示工具（Tip）**：

```text
堕落天使剑
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_0fa806811e19561d98fc.blp`　*(界面图标)*
    - `ides` Description = `-副武器|n|n|cffffd700攻击力:300|n筋力:120|n敏捷:120|n体力:120|n攻击速度:100|n能力:降临天使(B级)|n能力:神判(S级)|n品质:传说|n|r|n|cff3399ff若天使降临到你面前,那并不是所谓的天使,那只是披着天使面具的恶魔（当天使失去了心,就会变为堕落天使,也是所谓的降临天使）|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|cffff69b4堕落天使剑|r`　*(名字)*
    - `utip` Tip = `|cffff69b4堕落天使剑|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `-副武器|n|n|cffffd700攻击力:300|n筋力:120|n敏捷:120|n体力:120|n攻击速度:100|n能力:降临天使(B级)|n能力:神判(S级)|n品质:传说|n|r|n|cff3399ff若天使降临到你面前,那并不是所谓的天使,那只是披着天使面具的恶魔（当天使失去了心,就会变为堕落天使,也是所谓的降临天使）|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z00P,Z09F,Z0C9,Z0AZ`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Permanent`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z0AZ`　*(魔法施放间隔时间组)*
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
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `0`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
