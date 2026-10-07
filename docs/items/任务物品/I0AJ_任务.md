# I0AJ · 任务

> **分类**：任务物品　**品质**：—　**类型**：Miscellaneous　**物品等级**：—　**价格**：0 金

**物品 ID**：`I0AJ`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 城外有之疯狂的母牛,看上去却不是母牛,一般人发现不了有这只母牛的存在,想挑战它的话,拿个奶酪来孝敬我就好了,记住这奶牛只能刷一次,作为测试玩家的我,就告诉你们把!
>
> 需求物品:奶酪

**提示工具（Tip）**：

```text
任务
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I09R` | 任务 |
| `I0C5` | 任务 |
| `I0C8` | 任务 |
| `I0C9` | 任务 |
| `J0P8` | 任务 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNScroll.blp`　*(界面图标)*
    - `ides` Description = `|cfffff8dc城外有之疯狂的母牛,看上去却不是母牛,一般人发现不了有这只母牛的存在,想挑战它的话,拿个奶酪来孝敬我就好了,记住这奶牛只能刷一次,作为测试玩家的我,就告诉你们把!|n|n需求物品:奶酪|r`　*(描述)*
    - `unam` Name = `任务`　*(名字)*
    - `utip` Tip = `任务`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cfffff8dc城外有之疯狂的母牛,看上去却不是母牛,一般人发现不了有这只母牛的存在,想挑战它的话,拿个奶酪来孝敬我就好了,记住这奶牛只能刷一次,作为测试玩家的我,就告诉你们把!|n|n需求物品:奶酪|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `igol` goldcost = `0`　*(金子消耗)*
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
