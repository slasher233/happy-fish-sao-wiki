# I0HV · 能量

> **分类**：不归类　**品质**：—　**类型**：Permanent　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0HV`　·　**原型**：`tpow`（知识之书）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 力量奖励 | 66 | `A0QO` | `Istr` | 1 |
| 敏捷奖励 | 66 | `A0QO` | `Iagi` | 1 |
| 智力奖励 | 66 | `A0QO` | `Iint` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0QO` | .能源 | 力量奖励=66, 敏捷奖励=66, 智力奖励=66 | — |

### 游戏内说明（原文）

> 增加英雄1点的体力，敏捷度和筋力。

**提示工具（Tip）**：

```text
能量
```

## 获取方式

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `Hart` 神秘的人 | RandomDist (Blizzard.j 权重表) | 100% | `19220` |


## 合成与材料用途

**说明文本中提到本物品的物品**（文本匹配，不等于真实配方）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I00K` | 能量 |
| `I0DA` | 能量 |
| `I0DE` | 能量 |
| `I0E3` | 能量 |
| `J041` | 能量 |


??? note "全部对象字段（原始值）"

    - `ides` Description = `增加英雄1点的体力，敏捷度和筋力。`　*(描述)*
    - `unam` Name = `能量`　*(名字)*
    - `utip` Tip = `能量`　*(提示工具 - 基础)*
    - `utub` Ubertip = `增加英雄1点的体力，敏捷度和筋力。`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0QO`　*(技能)*
    - `icla` class = `Permanent`　*(分类)*
    - `icid` cooldownID = `A0QO`　*(魔法施放间隔时间组)*
    - `ifil` file = `Objects\InventoryItems\CrystalShard\CrystalShard.mdl`　*(已使用的模型)*
    - `isca` scale = `1.5`　*(缩放值)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
