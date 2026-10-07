# I0FS · 圣剑

> **分类**：武器　**品质**：传说　**类型**：Artifact　**物品等级**：8　**价格**：500000 金

**物品 ID**：`I0FS`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 生命值取得 | 9999999 | `Y200` | `Rej1` | 1 |
| 魔法点取得 | 9999999 | `Y200` | `Rej2` | 1 |
| 完整时可用 | 3 | `Y200` | `Rej3` | 1 |
| 没有目标要求 | 1 | `Y200` | `Rej4` | 1 |
| 敏捷奖励 | 333 | `Y203` | `Iagi` | 1 |
| 智力奖励 | 333 | `Y203` | `Iint` | 1 |
| 力量奖励 | 333 | `Y203` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Y203` | `Ihid` | 1 |
| 取得最大生命值 | 10000 | `Y202` | `Ilif` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Y200` | 王的祈祷 | 魔法施放时间间隔=35, 魔法消耗=0, 生命值取得=9999999, 魔法点取得=9999999, 完整时可用=3, 没有目标要求=1 | 在12秒内治疗目标友方单位400生命值。 |
| `Y203` | 全能力增加333 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=333, 智力奖励=333, 力量奖励=333, 隐藏按钮=0 | — |
| `Y202` | 增加最大生命值10000 | 魔法施放时间间隔=0, 魔法消耗=0, 取得最大生命值=10000 | — |

### 游戏内说明（原文）

> 武器
>
> 筋力:333
> 敏捷:333
> 体力:333
> 生命值:10000
> 能力:圣剑光辉
> 能力:王的祈祷
> 品质:传说
>
> 王者只是历史所记载的故事,没有人知道那英勇的事迹!

**提示工具（Tip）**：

```text
圣剑
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：

| 物品 ID | 物品名称 |
| --- | --- |
| `J0L4` | 圣剑 |
| `K001` | 圣剑 |

??? note "全部对象字段（原始值）"

    - `iico` Art = `P2E\war3mapImported\btnzz40.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520武器|r|n|n|cffffd700筋力:333|n敏捷:333|n体力:333|n生命值:10000|n能力:圣剑光辉|n能力:王的祈祷|n品质:传说|n|n王者只是历史所记载的故事,没有人知道那英勇的事迹!|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `8`　*(等级)*
    - `unam` Name = `|cffff7f50圣|r|cffffd700剑|r`　*(名字)*
    - `utip` Tip = `|cffff7f50圣|r|cffffd700剑|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520武器|r|n|n|cffffd700筋力:333|n敏捷:333|n体力:333|n生命值:10000|n能力:圣剑光辉|n能力:王的祈祷|n品质:传说|n|n王者只是历史所记载的故事,没有人知道那英勇的事迹!|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Y200,Y203,Y202`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Artifact`　*(分类)*
    - `iclb` colorB = `255`　*(染色 3 (蓝色))*
    - `iclg` colorG = `255`　*(染色 2 (绿色))*
    - `iclr` colorR = `255`　*(染色 1 (红色))*
    - `icid` cooldownID = `Y200`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `P2E\war3mapImported\wuqi2.mdx`　*(已使用的模型)*
    - `igol` goldcost = `500000`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `10`　*(等级(无类别的))*
    - `ipaw` pawnable = `1`　*(能被卖给商人)*
    - `iper` perishable = `0`　*(易腐烂的)*
    - `iprn` pickRandom = `1`　*(包括随机选择)*
    - `ipow` powerup = `0`　*(需要时自动使用)*
    - `ipri` prio = `126`　*(优先权)*
    - `isca` scale = `1`　*(缩放值)*
    - `issc` selSize = `0`　*(选择大小 – 编辑器)*
    - `isel` sellable = `1`　*(可以被商人出售)*
    - `isto` stockMax = `1`　*(最大储存)*
    - `istr` stockRegen = `120`　*(佣兵招募间隔)*
    - `isst` stockStart = `0`　*(佣兵招募时间)*
    - `iusa` usable = `1`　*(主动使用)*
    - `iuse` uses = `0`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
