# I0GC · 黑煌玫瑰

> **分类**：不归类　**品质**：普通　**类型**：Campaign　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0GC`　·　**原型**：`rde1`（守护指环 +2）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 伤害减少 | 0.22 | `A07B` | `isr2` | 1 |
| 防御奖励 | 30 | `A05O` | `Idef` | 1 |
| 敏捷奖励 | 144 | `A038` | `Iagi` | 1 |
| 魔法点取得 | -1111 | `A0O3` | `Impg` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A07B` | 减少魔伤22 | 伤害减少=0.22 | — |
| `A05O` | 增加防御30 | 防御奖励=30 | — |
| `A038` | 增加敏捷144 | 敏捷奖励=144 | — |
| `A0O3` | ..湮灭光环 | 魔法点取得=-1111, 魔法施放时间间隔=0 | — |

### 游戏内说明（原文）

> 道具(项链,手套,戒指,鞋子,灵魂)
>
> 敏捷:144
> 防御值:30
> 魔法防御:22
> 能力:黑煌之力(D级)
> 品质:普通
>
> 玫瑰自动吸收了黑煌的力量,所变成的道具

**提示工具（Tip）**：

```text
黑煌玫瑰
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN201402.blp`　*(界面图标)*
    - `ides` Description = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|cffffd700|n|r|cff00ffff敏捷:144|n防御值:30|n魔法防御:22|n能力:黑煌之力(D级)|n品质:普通|n|n玫瑰自动吸收了黑煌的力量,所变成的道具|r`　*(描述)*
    - `unam` Name = `|cff00ffff黑煌玫瑰|r`　*(名字)*
    - `utip` Tip = `|cff00ffff黑煌玫瑰|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|cffffd700|n|r|cff00ffff敏捷:144|n防御值:30|n魔法防御:22|n能力:黑煌之力(D级)|n品质:普通|n|n玫瑰自动吸收了黑煌的力量,所变成的道具|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A07B,A05O,A038,A0O3`　*(技能)*
    - `icla` class = `Campaign`　*(分类)*
    - `icid` cooldownID = `A0O3`　*(魔法施放间隔时间组)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
