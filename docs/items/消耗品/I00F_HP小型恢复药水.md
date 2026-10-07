# I00F · HP小型恢复药水

> **分类**：消耗品　**品质**：—　**类型**：Permanent　**物品等级**：—　**价格**：20 金

**物品 ID**：`I00F`　·　**原型**：`pghe`（大生命药水）　·　**版本**：v1.0 正式版

**热键**：`Q`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 生命值取得 | 100 | `A06F` | `Ihpg` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A06F` | 增加HP100 | 魔法施放时间间隔=0, 生命值取得=100 | — |

### 游戏内说明（原文）

> 能力:恢复自身生命点100
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
    - `ides` Description = `|cff00ffff能力:恢复自身生命点100|n|nCD时间:7秒|n施法距离:自身|r`　*(描述)*
    - `uhot` Hotkey = `Q`　*(热键)*
    - `unam` Name = `HP小型恢复药水`　*(名字)*
    - `utip` Tip = `购买HP小型恢复药水(|cffffcc00Q|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff00ffff能力:恢复自身生命点100|n|nCD时间:7秒|n施法距离:自身|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A06F`　*(技能)*
    - `icla` class = `Permanent`　*(分类)*
    - `icid` cooldownID = `A06F`　*(魔法施放间隔时间组)*
    - `igol` goldcost = `20`　*(金子消耗)*
    - `istr` stockRegen = `0`　*(佣兵招募间隔)*
    - `iuse` uses = `30`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
