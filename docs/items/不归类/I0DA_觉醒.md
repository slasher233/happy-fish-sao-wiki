# I0DA · 觉醒

> **分类**：不归类　**品质**：—　**类型**：Miscellaneous　**物品等级**：—　**价格**：10000 金

**物品 ID**：`I0DA`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 让所有的沉睡中的能量都化为新的动力,让一切都浮出水面,觉醒需要毁灭钻石,你带了吗?r
>
> 白色礼服
> 暗夜星纱
> 寂静之戒
> 绯梦
> 星尘枪
> 伊诺帝皇剑

**提示工具（Tip）**：

```text
觉醒
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I0IR` | 觉醒 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNCC29.blp`　*(界面图标)*
    - `ides` Description = `让所有的沉睡中的能量都化为新的动力,让一切都浮出水面,觉醒需要毁灭钻石,你带了吗?r|n|n|cffffd700白色礼服|n暗夜星纱|n寂静之戒|n绯梦|n星尘枪|n伊诺帝皇剑|n|r`　*(描述)*
    - `unam` Name = `觉醒`　*(名字)*
    - `utip` Tip = `觉醒`　*(提示工具 - 基础)*
    - `utub` Ubertip = `让所有的沉睡中的能量都化为新的动力,让一切都浮出水面,觉醒需要毁灭钻石,你带了吗?r|n|n|cffffd700白色礼服|n暗夜星纱|n寂静之戒|n绯梦|n星尘枪|n伊诺帝皇剑|n|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `icid` cooldownID = ``　*(魔法施放间隔时间组)*
    - `igol` goldcost = `10000`　*(金子消耗)*
    - `iper` perishable = `1`　*(易腐烂的)*
    - `ipow` powerup = `1`　*(需要时自动使用)*
    - `istr` stockRegen = `1`　*(佣兵招募间隔)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
