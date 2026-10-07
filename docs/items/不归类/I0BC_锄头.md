# I0BC · 锄头

> **分类**：不归类　**品质**：—　**类型**：Miscellaneous　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0BC`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 伤害 | 0 | `A0H1` | `Ctc1` | 1 |
| 攻击速度减少 | 0 | `A0H1` | `Ctc4` | 1 |
| 移动速度减少 | 0 | `A0H1` | `Ctc3` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0H1` | .挖矿 | 伤害=0, 攻击速度减少=0, 移动速度减少=0, 魔法消耗=0, 魔法施放时间间隔=10 | 挖矿 |

### 游戏内说明（原文）

> 能在某些地方进行采矿

**提示工具（Tip）**：

```text
锄头
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I05S` | 锄头 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNGatherGold.blp`　*(界面图标)*
    - `ides` Description = `能在某些地方进行采矿`　*(描述)*
    - `unam` Name = `锄头`　*(名字)*
    - `utip` Tip = `锄头`　*(提示工具 - 基础)*
    - `utub` Ubertip = `能在某些地方进行采矿`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0H1`　*(技能)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `icid` cooldownID = `A0H1`　*(魔法施放间隔时间组)*
    - `istr` stockRegen = `3`　*(佣兵招募间隔)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
