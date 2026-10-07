# I0DV · 姬剑★★☆

> **分类**：副武器　**品质**：究极　**类型**：Charged　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0DV`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 力量奖励 | 45 | `A0DD` | `Istr` | 1 |
| 敏捷奖励 | 45 | `A0DD` | `Iagi` | 1 |
| 智力奖励 | 45 | `A0DD` | `Iint` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0DD` | 全能力增加45 | 力量奖励=45, 敏捷奖励=45, 智力奖励=45 | — |

### 游戏内说明（原文）

> -副武器
>
> 筋力:45
> 敏捷:45
> 体力:45
> 品质:究极
> 被赐予的力量:2/3
>
> 一把很让人安心的剑

**提示工具（Tip）**：

```text
姬剑★★☆
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNabb12.blp`　*(界面图标)*
    - `ides` Description = `|cff9db9eb-副武器|r|n|n|cffff8c00筋力:45|n敏捷:45|n体力:45|n品质:究极|n被赐予的力量:2/3|n|n一把很让人安心的剑|r`　*(描述)*
    - `unam` Name = `|cffff8c00姬剑|r|cffffe4c4★★☆|r`　*(名字)*
    - `utip` Tip = `|cffff8c00姬剑|r|cffffe4c4★★☆|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff9db9eb-副武器|r|n|n|cffff8c00筋力:45|n敏捷:45|n体力:45|n品质:究极|n被赐予的力量:2/3|n|n一把很让人安心的剑|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0DD`　*(技能)*
    - `icla` class = `Charged`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
