# I0GI · 灵魂宝具(赤色羽翼)

> **分类**：装甲　**品质**：灵魂(Earl's level)　**类型**：PowerUp　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0GI`　·　**原型**：`ratc`（攻击之爪 +12）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 防御奖励 | 72 | `A065` | `Idef` | 1 |
| 取得最大生命值 | 10000 | `A0TE` | `Ilif` | 1 |
| 移动速度奖励 | 120 | `A08K` | `Imvb` | 1 |
| 力量奖励 | 233 | `A0DE` | `Istr` | 1 |
| 敏捷奖励 | 233 | `A0DE` | `Iagi` | 1 |
| 智力奖励 | 233 | `A0DE` | `Iint` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A065` | 增加防御72 | 防御奖励=72 | — |
| `A0TE` | 增加最大生命值10000 | 取得最大生命值=10000 | — |
| `A08K` | 移动速度120 | 移动速度奖励=120 | — |
| `A0DE` | 全能力增加233 | 力量奖励=233, 敏捷奖励=233, 智力奖励=233 | — |

### 游戏内说明（原文）

> 装甲
>
> 筋力:233
> 敏捷:233
> 体力:233
> 防御值:50
> 生命值:10000
> 移动速度:120
> 品质:灵魂(Earl's level) 
>
> 由天使的羽毛和天使的血液制造出的翅膀

**提示工具（Tip）**：

```text
灵魂宝具(赤色羽翼)
```

## 获取方式

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nrvs` 金色宝箱 | RandomDist (Blizzard.j 权重表) | 100% | `17856` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN201408.blp`　*(界面图标)*
    - `ides` Description = `|cfff0e68c装甲|r|n|n|cffff0000筋力:233|n敏捷:233|n体力:233|n防御值:50|n生命值:10000|n移动速度:120|n品质:灵魂|r(|cffdc143cEarl's level|r)|cffdc143c |n|n由天使的羽毛和天使的血液制造出的翅膀|r`　*(描述)*
    - `unam` Name = `|cffdc143c灵魂宝具|r(|cffff0000赤色羽翼|r)`　*(名字)*
    - `utip` Tip = `|cffdc143c灵魂宝具|r(|cffff0000赤色羽翼|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cfff0e68c装甲|r|n|n|cffff0000筋力:233|n敏捷:233|n体力:233|n防御值:50|n生命值:10000|n移动速度:120|n品质:灵魂|r(|cffdc143cEarl's level|r)|cffdc143c |n|n由天使的羽毛和天使的血液制造出的翅膀|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A065,A0TE,A08K,A0DE`　*(技能)*
    - `icla` class = `PowerUp`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
