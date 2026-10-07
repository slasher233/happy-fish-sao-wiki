# I0GE · 红鼻子面具

> **分类**：不归类　**品质**：稀有　**类型**：Campaign　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0GE`　·　**原型**：`rde1`（守护指环 +2）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击速度增加 | 0.15 | `A083` | `Isx1` | 1 |
| 力量奖励 | 20 | `A0DC` | `Istr` | 1 |
| 敏捷奖励 | 20 | `A0DC` | `Iagi` | 1 |
| 智力奖励 | 20 | `A0DC` | `Iint` | 1 |
| 闪避几率 | 0.5 | `A0LM` | `Eev1` | 1 |
| 装甲奖励 | 10 | `A0AK` | `Had1` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A083` | 增加攻击速度15 | 攻击速度增加=0.15 | — |
| `A0DC` | 全能力增加20 | 力量奖励=20, 敏捷奖励=20, 智力奖励=20 | — |
| `A0LM` | 天赋 斯托蕾雅 | 闪避几率=0.5 | — |
| `A0AK` | 战斗指挥Lv5 | 装甲奖励=10 | — |

### 游戏内说明（原文）

> 道具(项链,手套,戒指,鞋子,灵魂)
>
> 筋力:20
> 敏捷:20
> 体力:20
> 攻击速度:15
> 闪避值:45
> 能力:战斗指挥Lv5(D级)
> 品质:稀有
>
> 让身边的朋友能时时微笑而做出来的道具

**提示工具（Tip）**：

```text
红鼻子面具
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN201405.blp`　*(界面图标)*
    - `ides` Description = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|cffffd700|n|r|cff8a2be2筋力:20|n敏捷:20|n体力:20|n攻击速度:15|n闪避值:45|n能力:战斗指挥Lv5(D级)|n品质:稀有|n|n让身边的朋友能时时微笑而做出来的道具|r`　*(描述)*
    - `unam` Name = `|cff9932cc红鼻子面具|r`　*(名字)*
    - `utip` Tip = `|cff00ffff红鼻子面具|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|cffffd700|n|r|cff8a2be2筋力:20|n敏捷:20|n体力:20|n攻击速度:15|n闪避值:45|n能力:战斗指挥Lv5(D级)|n品质:稀有|n|n让身边的朋友能时时微笑而做出来的道具|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A083,A0DC,A0LM,A0AK`　*(技能)*
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
