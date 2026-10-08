# J0QR · 医疗剂

> **分类**：不归类　**品质**：无数据（说明里没写品质）　**类型**：可购买（原始枚举 `Purchasable`）　**物品等级**：1　**价格**：100 金

**物品 ID**：`J0QR`　·　**原型**：`hslv`（医疗剂）　·　**版本**：v1.0 正式版

## 功能描述（人话版）

持续时间 - 普通 45（说明里出现过）；持续时间 - 英雄 45（说明里出现过）；魔法施放范围 500

> 自动转写置信度 **low**；与说明原文的差异：原文有·数值无 3 处、无技能引用 1 处。
> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。

## 可改数值项（改这些值会写进地图对象）

**类别**列里「每级数值」是技能对象 `Data` 里的分级数值，「表头字段」是技能级的冷却/耗魔/距离/范围/持续（与等级无关）。

| 数值项 | 当前值 | 字段 id | 等级 | 类别 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 冷却 | 0.0 | `acdn` | 1 | 表头字段 | — |
| 魔法消耗 | 0 | `amcs` | 1 | 表头字段 | — |
| 施法距离 | 500.0 | `aran` | 1 | 表头字段 | — |
| 作用范围 | 0.0 | `aare` | 1 | 表头字段 | — |
| 持续时间 | 45.0 | `adur` | 1 | 表头字段 | — |
| 英雄持续时间 | 45.0 | `ahdu` | 1 | 表头字段 | — |
| 等级数 | 1 | `alev` | 0 | 表头字段 | — |


**怎么改**：到需求单仓库 `happy-fish-patch-plan` 打开 `data/item_ability_data.csv`，按 `item_code` + `ability_code` + `field` + `level` 找到对应行，把目标值写进 `new_value`，同行补 `req_id` 与 `note`；或者直接在「口语需求（自然语言）」Issue 里说人话，由我落表。

> ✔ = 该数值在游戏内说明里出现过（说明与对象数值对得上）。标 `x100` 的百分比项：CSV 里的 `cur_value` 存的是**原始小数**（0.1 = 10%），`new_value` 也要填小数。

**热键**：`H`

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

| 能力 ID | 能力名称 | 关键数值 |
| --- | --- | --- |
| `Z1BW` | 医疗剂 | 魔法施放时间间隔=0, 魔法消耗=0 |


> 对象数据没有给出这些能力的说明文字（`Ubertip` 为空），所以只列绑定关系与关键数值。

### 游戏内说明（原文）

> 非战斗类消耗型物品
> 使用后在45秒内恢复目标单位的生命值400点。
> 可使用3次。

**提示工具（Tip）**：

```text
购买医疗剂(H)
```

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：商店『巫毒商店』出售

_（这件物品的获取方式没有按来源聚合成组，见下方证据明细。）_

### 全部证据明细

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 巫毒商店 | `u0OK` | `umki` | Makeitems 人造的物品 | note_log/index/w3u_verify.txt:574460 |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `iico` **界面图标**（Art） = `ReplaceableTextures\CommandButtons\BTNHealingSalve.blp`
    - `ides` **描述**（Description） = `在一定的时间内恢复目标单位的生命值。`
    - `ihtp` **生命值**（HP） = `75`
    - `uhot` **热键**（Hotkey） = `H`
    - `ilev` **等级**（Level） = `1`
    - `unam` **名字**（Name） = `医疗剂`
    - `utip` **提示工具 - 基础**（Tip） = `购买医疗剂(H)`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `非战斗类消耗型物品 / 使用后在45秒内恢复目标单位的生命值400点。 / 可使用3次。`
    - `iabi` **技能**（abilList） = `Z1BW`
    - `iarm` **装甲类型**（armor） = `Wood`
    - `icla` **分类**（class） = `Purchasable`
    - `iclb` **染色 3 (蓝色)**（colorB） = `255`
    - `iclg` **染色 2 (绿色)**（colorG） = `255`
    - `iclr` **染色 1 (红色)**（colorR） = `255`
    - `icid` **魔法施放间隔时间组**（cooldownID） = `AIrg`
    - `idrp` **当携带者死亡时掉落**（drop） = `0`
    - `idro` **可以遗弃的**（droppable） = `1`
    - `ifil` **已使用的模型**（file） = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`
    - `igol` **金子消耗**（goldcost） = `100`
    - `iicd` **忽视延迟**（ignoreCD） = `0`
    - `ilum` **木材消耗**（lumbercost） = `0`
    - `imor` **转移有效目标**（morph） = `0`
    - `ilvo` **等级(无类别的)**（oldLevel） = `0`
    - `ipaw` **能被卖给商人**（pawnable） = `1`
    - `iper` **易腐烂的**（perishable） = `1`
    - `iprn` **包括随机选择**（pickRandom） = `0`
    - `ipow` **需要时自动使用**（powerup） = `0`
    - `ipri` **优先权**（prio） = `82`
    - `isca` **缩放值**（scale） = `1`
    - `issc` **选择大小 – 编辑器**（selSize） = `0`
    - `isel` **可以被商人出售**（sellable） = `1`
    - `isto` **最大储存**（stockMax） = `2`
    - `istr` **佣兵招募间隔**（stockRegen） = `60`
    - `isst` **佣兵招募时间**（stockStart） = `0`
    - `iusa` **主动使用**（usable） = `1`
    - `iuse` **负荷数量**（uses） = `3`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
