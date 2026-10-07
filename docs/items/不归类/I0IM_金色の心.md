# I0IM · 金色の心

> **分类**：不归类　**品质**：优越　**类型**：Campaign　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0IM`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 伤害减少 | 0.52 | `A0SN` | `isr2` | 1 |
| 防御奖励 | 50 | `A05X` | `Idef` | 1 |
| 取得最大生命值 | 10000 | `A0TE` | `Ilif` | 1 |
| 攻击奖励 | 0 | `A0BA` | `Iatt` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0SN` | 减少魔伤52 | 伤害减少=0.52 | — |
| `A05X` | 增加防御50 | 防御奖励=50 | — |
| `A0TE` | 增加最大生命值10000 | 取得最大生命值=10000 | — |
| `A0BA` | 吸血鬼之力Lv1 | 攻击奖励=0 | — |

### 游戏内说明（原文）

> 道具(项链,手套,戒指,鞋子,灵魂)
>
> 生命值:10000
> 魔法防御:52
> 防御:50
> 能力:吸血鬼王Lv1(C级)
> 圣女贞德之力（攻击时附带500伤害）
> 品质:优越
>
> 很精致的吊坠,显的非常入眼!

**提示工具（Tip）**：

```text
金色の心
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNEXS05.blp`　*(界面图标)*
    - `ides` Description = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cff7fff00生命值:10000|n魔法防御:52|n防御:50|n能力:吸血鬼王Lv1(C级)|n圣女贞德之力（攻击时附带500伤害）|n品质:优越|n|n很精致的吊坠,显的非常入眼!|r`　*(描述)*
    - `unam` Name = `|cffff0000金色の心|r`　*(名字)*
    - `utip` Tip = `|cffff0000金色の心|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cff7fff00生命值:10000|n魔法防御:52|n防御:50|n能力:吸血鬼王Lv1(C级)|n圣女贞德之力（攻击时附带500伤害）|n品质:优越|n|n很精致的吊坠,显的非常入眼!|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0SN,A05X,A0TE,A0BA`　*(技能)*
    - `icla` class = `Campaign`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
