# I0HP · 黑剑·阐释者

> **分类**：武器　**品质**：传说　**类型**：—　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0HP`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 影响范围伤害 | 0 | `A0GO` | `Htc1` | 1 |
| 攻击速度减少 (%) | 0 | `A0GO` | `Htc4` | 1 |
| 移动速度减少 (%) | 0 | `A0GO` | `Htc3` | 1 |
| 攻击奖励 | 700 | `A0QF` | `Iatt` | 1 |
| 力量奖励 | 150 | `A0JA` | `Istr` | 1 |
| 敏捷奖励 | 200 | `A0JA` | `Iagi` | 1 |
| 智力奖励 | 50 | `A0JA` | `Iint` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0GO` | 传送盖亚之城 | 影响范围伤害=0, 攻击速度减少 (%)=0, 移动速度减少 (%)=0, 魔法施放时间间隔=5, 魔法消耗=0 | — |
| `A0QF` | 增加攻击700 | 攻击奖励=700 | — |
| `A0JA` | 筋力150/敏捷200/体力50 | 力量奖励=150, 敏捷奖励=200, 智力奖励=50 | — |

### 游戏内说明（原文）

> 武器
>
> 攻击力:700
> 筋力:150
> 敏捷:200
> 影流(提高桐人r技能系数)
> 传送盖亚之城
> 品质:传说
>
> 由50层BOSS掉落的武器,极度吸引大多数玩家的眼光,是非常具备争议性的武器

**提示工具（Tip）**：

```text
黑剑·阐释者
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNZZXX12.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|cffffd700|n攻击力:700|n筋力:150|n敏捷:200|n影流(提高桐人r技能系数)|n传送盖亚之城|n品质:传说|n|n由50层BOSS掉落的武器,极度吸引大多数玩家的眼光,是非常具备争议性的武器|r`　*(描述)*
    - `unam` Name = `|cffffd700黑剑|r·|cfffa8072阐释者|r`　*(名字)*
    - `utip` Tip = `|cffffd700黑剑|r·|cfffa8072阐释者|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|cffffd700|n攻击力:700|n筋力:150|n敏捷:200|n影流(提高桐人r技能系数)|n传送盖亚之城|n品质:传说|n|n由50层BOSS掉落的武器,极度吸引大多数玩家的眼光,是非常具备争议性的武器|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0GO,A0QF,A0JA`　*(技能)*
    - `icid` cooldownID = `A0GO`　*(魔法施放间隔时间组)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
