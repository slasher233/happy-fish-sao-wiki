# I0AT · 水晶石盾

> **分类**：不归类　**品质**：—　**类型**：Charged　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0AT`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 装甲奖励 | 9 | `A0AO` | `Had1` | 1 |
| 防御奖励 | 42 | `A05U` | `Idef` | 1 |
| 取得最大生命值 | 500 | `A06N` | `Ilif` | 1 |
| 每秒生命值回复 | 30 | `A07N` | `Ihpr` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0AO` | 战斗指挥Lv4 | 装甲奖励=9 | — |
| `A05U` | 增加防御42 | 防御奖励=42 | — |
| `A06N` | 增加最大生命500 | 取得最大生命值=500 | — |
| `A07N` | 生命恢复30 | 每秒生命值回复=30 | — |

### 游戏内说明（原文）

> 防御值:42
> 生命值:500
> 能力:生命恢复Lv5(E级)
> 能力:战斗指挥Lv4(D级)
> 品质;劣质
>
> 非常坚固的盾,盾的造型很漂亮

**提示工具（Tip）**：

```text
水晶石盾
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN4.blp`　*(界面图标)*
    - `ides` Description = `|cff00ffff防御值:42|n生命值:500|n能力:生命恢复Lv5(E级)|n能力:战斗指挥Lv4(D级)|n品质;劣质|n|n非常坚固的盾,盾的造型很漂亮|r`　*(描述)*
    - `unam` Name = `水晶石盾`　*(名字)*
    - `utip` Tip = `水晶石盾`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff00ffff防御值:42|n生命值:500|n能力:生命恢复Lv5(E级)|n能力:战斗指挥Lv4(D级)|n品质;劣质|n|n非常坚固的盾,盾的造型很漂亮|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0AO,A05U,A06N,A07N`　*(技能)*
    - `icla` class = `Charged`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
