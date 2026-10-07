# J0KJ · 异次融合枪·◆◆◆

> **分类**：武器　**品质**：优越　**类型**：Artifact　**物品等级**：44　**价格**：1000 金

**物品 ID**：`J0KJ`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 法术列表 | Z053,Z0LK,Z01P,Z04U,Z0MP | `Z0Q4` | `spb1` | 1 |
| 共享法术施放时间间隔 | 1 | `Z0Q4` | `spb2` | 1 |
| 最小法术 | 10 | `Z0Q4` | `spb3` | 1 |
| 最大法术 | 10 | `Z0Q4` | `spb4` | 1 |
| 基本顺序 ID | spellbook | `Z0Q4` | `spb5` | 1 |
| 攻击速度增加 | 0.5 | `Z04T` | `Isx1` | 1 |
| 取得最大生命值 | 10000 | `Z0J0` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z0Q4` | 异次融合枪·◆◆◆ | 魔法施放时间间隔=0, 魔法消耗=0, 法术列表=Z053,Z0LK,Z01P,Z04U,Z0MP, 共享法术施放时间间隔=1, 最小法术=10, 最大法术=10, 基本顺序 ID=spellbook | — |
| `Z04T` | 增加攻击速度50 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击速度增加=0.5 | — |
| `Z0J0` | 增加最大生命值10000 | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=10000 | — |

### 游戏内说明（原文）

> 武器
>
> 攻击力:310
> 筋力:112
> 品质:优越
>
> 提升
> 筋力追加:68
> 攻击追加:890
> 攻击速度:109
> 生命值:10000
> Max提升
> 能力:普通致命Lv4
> 次元突破Lv2

**提示工具（Tip）**：

```text
异次融合枪·◆◆◆
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_f11e1d2be632bfd17d46.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|n|cff8a2be2攻击力:310|n筋力:112|n品质:优越|n|n提升|n筋力追加:68|n攻击追加:890|n攻击速度:109|n生命值:10000|nMax提升|n能力:普通致命Lv4|n次元突破Lv2|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `44`　*(等级)*
    - `unam` Name = `|cff8a2be2异次融合枪·◆◆◆|r`　*(名字)*
    - `utip` Tip = `|cff8a2be2异次融合枪·◆◆◆|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|n|cff8a2be2攻击力:310|n筋力:112|n品质:优越|n|n提升|n筋力追加:68|n攻击追加:890|n攻击速度:109|n生命值:10000|nMax提升|n能力:普通致命Lv4|n次元突破Lv2|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z0Q4,Z04T,Z0J0`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Artifact`　*(分类)*
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
    - `ilvo` oldLevel = `44`　*(等级(无类别的))*
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
