# I0HX · 战国元帅

> **分类**：装甲　**品质**：良好　**类型**：PowerUp　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0HX`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 力量奖励 | 20 | `A0DC` | `Istr` | 1 |
| 敏捷奖励 | 20 | `A0DC` | `Iagi` | 1 |
| 智力奖励 | 20 | `A0DC` | `Iint` | 1 |
| 攻击速度增加 | 100 | `A0F2` | `Isx1` | 1 |
| 防御奖励 | 55 | `A05Z` | `Idef` | 1 |
| 取得最大生命值 | 2500 | `A0H6` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0DC` | 全能力增加20 | 力量奖励=20, 敏捷奖励=20, 智力奖励=20 | — |
| `A0F2` | 增加攻击速度100 | 攻击速度增加=100 | — |
| `A05Z` | 增加防御55 | 防御奖励=55 | — |
| `A0H6` | 增加最大生命2500 | 取得最大生命值=2500 | — |

### 游戏内说明（原文）

> 装甲
>
> 筋力:20
> 敏捷:20
> 体力20
> 防御值:55
> 生命值:2500
> 攻击速度:100
> 品质:良好
>
> 在一场对抗魔族大战中,某个国加使用的装备

**提示工具（Tip）**：

```text
战国元帅
```

## 获取方式

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nrvl` 寂静之箱 | RandomDist (Blizzard.j 权重表) | 100% | `23031` |


**事件生成（`CreateItemLoc`）**

| 方式 | 触发单位 | j 行号 |
| --- | --- | --- |
| static_preplaced |  | `110798` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNZZXX07.blp`　*(界面图标)*
    - `ides` Description = `|cfff0e68c装甲|r|n|n|cff7fffd4筋力:20|n敏捷:20|n体力20|n防御值:55|n生命值:2500|n攻击速度:100|n品质:良好|r|n|n|cff3399ff在一场对抗魔族大战中,某个国加使用的装备|r`　*(描述)*
    - `unam` Name = `|cffff0000战国元帅|r`　*(名字)*
    - `utip` Tip = `|cffff0000战国元帅|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cfff0e68c装甲|r|n|n|cff7fffd4筋力:20|n敏捷:20|n体力20|n防御值:55|n生命值:2500|n攻击速度:100|n品质:良好|r|n|n|cff3399ff在一场对抗魔族大战中,某个国加使用的装备|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0DC,A0F2,A05Z,A0H6`　*(技能)*
    - `icla` class = `PowerUp`　*(分类)*
    - `ifil` file = `Objects\InventoryItems\CrystalShard\CrystalShard.mdl`　*(已使用的模型)*
    - `isca` scale = `0.1`　*(缩放值)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
