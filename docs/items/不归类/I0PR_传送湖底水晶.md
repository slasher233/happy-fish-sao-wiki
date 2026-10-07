# I0PR · 传送湖底水晶

> **分类**：不归类　**品质**：—　**类型**：Unknown　**物品等级**：8　**价格**：200 金

**物品 ID**：`I0PR`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`Q`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 跟随时间 | 0 | `ZRc0` | `Ncl1` | 1 |
| 目标类型 | 0 | `ZRc0` | `Ncl2` | 1 |
| 选项 | 2 | `ZRc0` | `Ncl3` | 1 |
| 技术持续时间 | 0 | `ZRc0` | `Ncl4` | 1 |
| 使其他技能无效 | 0 | `ZRc0` | `Ncl5` | 1 |
| 基本顺序 ID | channel | `ZRc0` | `Ncl6` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `ZRc0` | 传送水晶次数充值 | 魔法施放时间间隔=0, 魔法消耗=0, 跟随时间=0, 目标类型=0, 选项=2, 技术持续时间=0, 使其他技能无效=0, 基本顺序 ID=channel | — |

### 游戏内说明（原文）

> 不归类
>
> 使用后消耗水晶，增加湖底之城传送次数3000次。
> 回车输入 hc5 传送，每次消耗1次。
> 次数属于使用者，并随队伍存档保存。

**提示工具（Tip）**：

```text
购买传送湖底之城水晶(Q)
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNGlyph.blp`　*(界面图标)*
    - `ides` Description = `使用后消耗水晶，增加湖底之城传送次数3000次。|n回车输入 hc5 传送，每次消耗1次。|n次数属于使用者，并随队伍存档保存。`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `Q`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `传送湖底水晶`　*(名字)*
    - `utip` Tip = `购买传送湖底之城水晶(|cffffcc00Q|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520不归类|r|n|n使用后消耗水晶，增加湖底之城传送次数3000次。|n回车输入 hc5 传送，每次消耗1次。|n次数属于使用者，并随队伍存档保存。`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `ZRc0`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Unknown`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `ZRc0`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`　*(已使用的模型)*
    - `igol` goldcost = `200`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
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
    - `istr` stockRegen = `1`　*(佣兵招募间隔)*
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
