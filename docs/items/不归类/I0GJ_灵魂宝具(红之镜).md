# I0GJ · 灵魂宝具(红之镜)

> **分类**：不归类　**品质**：灵魂(God's Level)　**类型**：Campaign　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0GJ`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击速度增加 (%) | 0.4 | `A0FE` | `Oae2` | 1 |
| 移动速度增加 (%) | 0.15 | `A0FE` | `Oae1` | 1 |
| 装甲奖励 | -8 | `A0O5` | `Had1` | 1 |
| 攻击伤害增加 | 0.3 | `A0O6` | `Cac1` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A0VM` | .小血羽 | 魔法施放时间间隔=15 | — |
| `A0FE` | 疯狂舞会Lv3 | 攻击速度增加 (%)=0.4, 移动速度增加 (%)=0.15 | — |
| `A0O5` | 暴雨宴会Lv3 | 装甲奖励=-8 | — |
| `A0O6` | 士气上升Lv3 | 攻击伤害增加=0.3 | — |

### 游戏内说明（原文）

> 道具(项链,手套,戒指,鞋子,灵魂)
>
> 能力;疯狂舞会Lv3(D级)
> 能力:暴雨宴会Lv3(D级)
> 能力:士气上升Lv3(D级)
> 小血羽(魔免3秒,间隔15秒)
> 能力:黑天使Lv4(B级)
> 品质:灵魂(God's Level)
>
> 拥有红之镜的人,它能为自己驱散不安和恐惧感,它的带来是温暖和安全感

**提示工具（Tip）**：

```text
灵魂宝具(红之镜)
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN201409.blp`　*(界面图标)*
    - `ides` Description = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cffdc143c能力;疯狂舞会Lv3(D级)|n能力:暴雨宴会Lv3(D级)|n能力:士气上升Lv3(D级)|n小血羽(魔免3秒,间隔15秒)|n能力:黑天使Lv4(B级)|n品质:灵魂(|r|cffff1493God's Level)|r|n|n|cfffa8072拥有红之镜的人,它能为自己驱散不安和恐惧感,它的带来是温暖和安全感|r`　*(描述)*
    - `unam` Name = `|cffdc143c灵魂宝具|r(|cffff0000红之镜|r)`　*(名字)*
    - `utip` Tip = `|cffdc143c灵魂宝具|r(|cffff0000红之镜|r)`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffe9967a道具(项链,手套,戒指,鞋子,灵魂)|r|n|n|cffdc143c能力;疯狂舞会Lv3(D级)|n能力:暴雨宴会Lv3(D级)|n能力:士气上升Lv3(D级)|n小血羽(魔免3秒,间隔15秒)|n能力:黑天使Lv4(B级)|n品质:灵魂(|r|cffff1493God's Level)|r|n|n|cfffa8072拥有红之镜的人,它能为自己驱散不安和恐惧感,它的带来是温暖和安全感|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A0VM,A0FE,A0O5,A0O6`　*(技能)*
    - `icla` class = `Campaign`　*(分类)*
    - `icid` cooldownID = `A0O8`　*(魔法施放间隔时间组)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
