# I0HG · 灵魂道具◆(黄昏)

> **分类**：不归类　**品质**：灵魂(King's level)　**类型**：Campaign　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0HG`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 移动速度奖励 | 100 | `A08T` | `Imvb` | 1 |
| 智力奖励 | 150 | `A04K` | `Iint` | 1 |
| 攻击奖励 | 155 | `A01E` | `Iatt` | 1 |
| 取得最大生命值 | 1500 | `A0H2` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A08T` | 移动速度100 | 移动速度奖励=100 | — |
| `A04K` | 增加体力150 | 智力奖励=150 | — |
| `A01E` | 增加攻击155 | 攻击奖励=155 | — |
| `A0H2` | 增加最大生命1500 | 取得最大生命值=1500 | — |

### 游戏内说明（原文）

> 道具(项链,手套,戒指,鞋子,灵魂)
>
> 攻击力:155
> 体力:150
> 生命值:1500
> 移动速度:100
> 品质:灵魂(King's level)
>
> 无法理解的灵魂之剑!

**提示工具（Tip）**：

```text
灵魂道具◆(黄昏)
```

## 获取方式

**击杀成长（本物品是**升级后**的形态）**

| 另一形态 | 击杀阈值 | j 行号 |
| --- | --- | --- |
| `I0HE` 灵魂武器(黄昏) | `vh` ≥ 1 | `30737` |


**触发时赠予**

| 方式 | 给谁 | j 行号 |
| --- | --- | --- |
| unclassified_give | GetKillingUnit( | `30739` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNZZ41.blp`　*(界面图标)*
    - `ides` Description = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cffff1493攻击力:155|n体力:150|n生命值:1500|n移动速度:100|n品质:灵魂(King's level)|n|r|n|cffb22222无法理解的灵魂之剑!|r`　*(描述)*
    - `unam` Name = `|cffdc143c灵魂道具|r|cffff8c00◆|r(|cffd2691e黄昏|r)`　*(名字)*
    - `utip` Tip = `|cffdc143c灵魂道具|r|cffff8c00◆|r(|cffd2691e黄昏|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cffff1493攻击力:155|n体力:150|n生命值:1500|n移动速度:100|n品质:灵魂(King's level)|n|r|n|cffb22222无法理解的灵魂之剑!|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A08T,A04K,A01E,A0H2`　*(技能)*
    - `icla` class = `Campaign`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
