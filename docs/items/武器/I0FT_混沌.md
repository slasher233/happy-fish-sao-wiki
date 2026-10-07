# I0FT · 混沌

> **分类**：武器　**品质**：—　**类型**：—　**物品等级**：—　**价格**：0 金

**物品 ID**：`I0FT`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 敏捷奖励 | 400 | `A0UH` | `Iagi` | 1 |
| 力量奖励 | 400 | `A0UH` | `Istr` | 1 |
| 智力奖励 | 400 | `A0UH` | `Iint` | 1 |
| 取得最大生命值 | 20000 | `A0S2` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0UH` | 筋力400/敏捷400/体力400 | 敏捷奖励=400, 力量奖励=400, 智力奖励=400 | — |
| `A0S2` | 生命值2W | 取得最大生命值=20000 | — |

### 游戏内说明（原文）

> 武器
>
> 生命值:20000
> 筋力:400
> 敏捷:400
> 体力:400
>
> 不存在于此世间的武器

**提示工具（Tip）**：

```text
混沌
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I06S` | 混沌 |
| `J0L9` | 混沌 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNZZ40.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|n|cffffd700生命值:20000|n筋力:400|n敏捷:400|n体力:400|n|n不存在于此世间的武器|r`　*(描述)*
    - `unam` Name = `|cffffd700混|r|cffff0000沌|r`　*(名字)*
    - `utip` Tip = `|cffffd700混|r|cffff0000沌|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|n|cffffd700生命值:20000|n筋力:400|n敏捷:400|n体力:400|n|n不存在于此世间的武器|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0UH,A0S2`　*(技能)*
    - `icid` cooldownID = ``　*(魔法施放间隔时间组)*
    - `igol` goldcost = `0`　*(金子消耗)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
