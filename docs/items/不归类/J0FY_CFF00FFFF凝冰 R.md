# J0FY · |CFF00FFFF凝冰|R

> **分类**：不归类　**品质**：融合　**类型**：Miscellaneous　**物品等级**：154　**价格**：1000 金

**物品 ID**：`J0FY`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 移动速度增加 (%) | 1 | `Z0QE` | `Oae1` | 1 |
| 攻击速度增加 (%) | 1 | `Z0QE` | `Oae2` | 1 |
| 初始伤害 | 2000 | `Z0QD` | `pxf1` | 1 |
| 每秒伤害 | 800 | `Z0QD` | `pxf2` | 1 |
| 敏捷奖励 | 350 | `Z0QC` | `Iagi` | 1 |
| 智力奖励 | 350 | `Z0QC` | `Iint` | 1 |
| 力量奖励 | 0 | `Z0QC` | `Istr` | 1 |
| 隐藏按钮 | 0 | `Z0QC` | `Ihid` | 1 |
| 攻击奖励 | 1200 | `Z0LL` | `Iatt` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `Z0QE` | 真白/攻速移速 | 魔法施放时间间隔=0, 魔法消耗=0, 移动速度增加 (%)=1, 攻击速度增加 (%)=1 | 增加周围单位10%的移动速度和5%的攻击速度。 |
| `Z0QD` | 追踪箭 | 魔法施放时间间隔=0.1, 魔法消耗=0, 初始伤害=2000, 每秒伤害=800 | 火焰流淌，灼烧附近的敌单位。 |
| `Z0QC` | 敏捷350体力350 | 魔法施放时间间隔=0, 魔法消耗=0, 敏捷奖励=350, 智力奖励=350, 力量奖励=0, 隐藏按钮=0 | — |
| `Z0LL` | 增加攻击1200 | 魔法施放时间间隔=0, 魔法消耗=0, 攻击奖励=1200 | — |

### 游戏内说明（原文）

> 不归类
>
> 攻击力:1200
> 敏捷:350
> 体力:350
> 能力:弓术
> 能力:冰魄箭(S级)
> 品质:融合

**提示工具（Tip）**：

```text
|CFF00FFFF凝冰|R
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNP2_28c33ebf693f57e9712b.blp`　*(界面图标)*
    - `ides` Description = `|cffdaa520不归类|r|n|n|cff6495ed攻击力:1200|n敏捷:350|n体力:350|n能力:弓术|n能力:冰魄箭(S级)|n品质:融合|r`　*(描述)*
    - `ihtp` HP = `75`　*(生命值)*
    - `uhot` Hotkey = `K`　*(热键)*
    - `ilev` Level = `154`　*(等级)*
    - `unam` Name = `|CFF00FFFF凝冰|R`　*(名字)*
    - `utip` Tip = `|CFF00FFFF凝冰|R`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffdaa520不归类|r|n|n|cff6495ed攻击力:1200|n敏捷:350|n体力:350|n能力:弓术|n能力:冰魄箭(S级)|n品质:融合|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `Z0QE,Z0QD,Z0QC,Z0LL`　*(技能)*
    - `iarm` armor = `Wood`　*(装甲类型)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `iclb` colorB = `100`　*(染色 3 (蓝色))*
    - `iclg` colorG = `65`　*(染色 2 (绿色))*
    - `iclr` colorR = `180`　*(染色 1 (红色))*
    - `icid` cooldownID = `Z1CR`　*(魔法施放间隔时间组)*
    - `idrp` drop = `0`　*(当携带者死亡时掉落)*
    - `idro` droppable = `1`　*(可以遗弃的)*
    - `ifil` file = `P2\war3mapImported\wuqi2.mdx`　*(已使用的模型)*
    - `igol` goldcost = `1000`　*(金子消耗)*
    - `iicd` ignoreCD = `0`　*(忽视延迟)*
    - `ilum` lumbercost = `0`　*(木材消耗)*
    - `imor` morph = `0`　*(转移有效目标)*
    - `ilvo` oldLevel = `154`　*(等级(无类别的))*
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
    - `iusa` usable = `0`　*(主动使用)*
    - `iuse` uses = `0`　*(负荷数量)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
