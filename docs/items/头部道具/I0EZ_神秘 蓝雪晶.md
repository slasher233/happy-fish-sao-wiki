# I0EZ · 神秘:蓝雪晶

> **分类**：头部道具　**品质**：—　**类型**：Purchasable　**物品等级**：130　**价格**：— 金

**物品 ID**：`I0EZ`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 取得最大生命值 | 300 | `A06Q` | `Ilif` | 1 |
| 攻击速度增加 | 100 | `A0F2` | `Isx1` | 1 |
| 攻击奖励 | 300 | `A01F` | `Iatt` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A06Q` | 增加最大生命300 | 取得最大生命值=300 | — |
| `A0F2` | 增加攻击速度100 | 攻击速度增加=100 | — |
| `A01F` | 增加攻击300 | 攻击奖励=300 | — |

### 游戏内说明（原文）

> 头部道具
>
> 攻击力:300
> 生命值:300
> 攻击速度:100
> 品质;稀有
>
> 白中透蓝,非常漂亮,就算太阳照耀着也不会被融化

**提示工具（Tip）**：

```text
神秘:蓝雪晶
```

## 获取方式

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nrvs` 金色宝箱 | RandomDist (Blizzard.j 权重表) | 100% | `20632` |
| `nrvs` 金色宝箱 | RandomDist (Blizzard.j 权重表) | 10% | `21386` |
| `I0F1` | ChooseRandomItemExBJ(level, itemClass) | — | `29564` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNZZC4.blp`　*(界面图标)*
    - `ides` Description = `|cff6495ed头部道具|r|n|n|cff8a2be2攻击力:300|n生命值:300|n攻击速度:100|n品质;稀有|n|n白中透蓝,非常漂亮,就算太阳照耀着也不会被融化|r`　*(描述)*
    - `ilev` Level = `130`　*(等级)*
    - `unam` Name = `神秘:蓝雪晶`　*(名字)*
    - `utip` Tip = `神秘:蓝雪晶`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff6495ed头部道具|r|n|n|cff8a2be2攻击力:300|n生命值:300|n攻击速度:100|n品质;稀有|n|n白中透蓝,非常漂亮,就算太阳照耀着也不会被融化|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A06Q,A0F2,A01F`　*(技能)*
    - `icla` class = `Purchasable`　*(分类)*
    - `ilvo` oldLevel = `130`　*(等级(无类别的))*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
