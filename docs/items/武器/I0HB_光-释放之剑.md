# I0HB · 光-释放之剑

> **分类**：武器　**品质**：传说　**类型**：Artifact　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0HB`　·　**原型**：`rst1`（食人鬼手套 +3）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击奖励 | 225 | `A01H` | `Iatt` | 1 |
| 取得最大生命值 | 2000 | `A0H4` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A01H` | 增加攻击225 | 攻击奖励=225 | — |
| `A0H4` | 增加最大生命2000 | 取得最大生命值=2000 | — |

### 游戏内说明（原文）

> 武器
>
> 攻击力:121
> 生命值:2000
> 品质:传说
>
> 就好像沉睡的公主,在那里静静的期待着什么来临

**提示工具（Tip）**：

```text
光-释放之剑
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTN141C.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|n|cffffd700攻击力:121|n生命值:2000|n品质:传说|n|n就好像沉睡的公主,在那里静静的期待着什么来临|r`　*(描述)*
    - `unam` Name = `光-释放之剑`　*(名字)*
    - `utip` Tip = `光-释放之剑`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|n|cffffd700攻击力:121|n生命值:2000|n品质:传说|n|n就好像沉睡的公主,在那里静静的期待着什么来临|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A01H,A0H4`　*(技能)*
    - `icla` class = `Artifact`　*(分类)*
    - `ifil` file = `Objects\InventoryItems\CrystalShard\CrystalShard.mdl`　*(已使用的模型)*
    - `isca` scale = `0.1`　*(缩放值)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
