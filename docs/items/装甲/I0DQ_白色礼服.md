# I0DQ · 白色礼服

> **分类**：装甲　**品质**：传说　**类型**：PowerUp　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0DQ`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 防御奖励 | 45 | `A05V` | `Idef` | 1 |
| 力量奖励 | 150 | `A0JA` | `Istr` | 1 |
| 敏捷奖励 | 200 | `A0JA` | `Iagi` | 1 |
| 智力奖励 | 50 | `A0JA` | `Iint` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A05V` | 增加防御45 | 防御奖励=45 | — |
| `A0JA` | 筋力150/敏捷200/体力50 | 力量奖励=150, 敏捷奖励=200, 智力奖励=50 | — |

### 游戏内说明（原文）

> 装甲
>
> 筋力:150
> 敏捷:200
> 体力:50
> 防御值:45
> 品质:传说
>
> 非常美丽的服饰,千言万语盖不住它的魅力

**提示工具（Tip）**：

```text
白色礼服
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I0DA` | 白色礼服 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNabb09.blp`　*(界面图标)*
    - `ides` Description = `|cfff0e68c装甲|r|n|n|cffffd700筋力:150|n敏捷:200|n体力:50|n防御值:45|n品质:传说|n|n非常美丽的服饰,千言万语盖不住它的魅力|r`　*(描述)*
    - `unam` Name = `|cffff1493白色礼服|r`　*(名字)*
    - `utip` Tip = `|cffff1493白色礼服|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cfff0e68c装甲|r|n|n|cffffd700筋力:150|n敏捷:200|n体力:50|n防御值:45|n品质:传说|n|n非常美丽的服饰,千言万语盖不住它的魅力|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A05V,A0JA`　*(技能)*
    - `icla` class = `PowerUp`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
