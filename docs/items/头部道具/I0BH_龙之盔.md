# I0BH · 龙之盔

> **分类**：头部道具　**品质**：传说　**类型**：Purchasable　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0BH`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 防御奖励 | 30 | `A05O` | `Idef` | 1 |
| 力量奖励 | 80 | `A028` | `Istr` | 1 |
| 取得最大生命值 | 2000 | `A0H4` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A05O` | 增加防御30 | 防御奖励=30 | — |
| `A028` | 增加筋力80 | 力量奖励=80 | — |
| `A0H4` | 增加最大生命2000 | 取得最大生命值=2000 | — |

### 游戏内说明（原文）

> 头部道具
>
> 筋力:80
> 防御值:30
> 生命:2000
> 品质:传说
>
> 用龙材料所做出的防具,坚硬无比,非常具有震撼力,看上去朴素,却又高贵和优雅

**提示工具（Tip）**：

```text
龙之盔
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I08F` | 龙之盔 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN2013zz2.blp`　*(界面图标)*
    - `ides` Description = `|cff6495ed头部道具|r|n|n|cffffd700筋力:80|n防御值:30|n生命:2000|n品质:传说|n|n用龙材料所做出的防具,坚硬无比,非常具有震撼力,看上去朴素,却又高贵和优雅|r`　*(描述)*
    - `unam` Name = `|cffffd700龙之盔|r`　*(名字)*
    - `utip` Tip = `|cffffd700龙之盔|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff6495ed头部道具|r|n|n|cffffd700筋力:80|n防御值:30|n生命:2000|n品质:传说|n|n用龙材料所做出的防具,坚硬无比,非常具有震撼力,看上去朴素,却又高贵和优雅|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A05O,A028,A0H4`　*(技能)*
    - `icla` class = `Purchasable`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
