# I0PR · 传送湖底水晶

> **分类**：不归类　**品质**：无数据（说明里没写品质）　**类型**：未分类　**物品等级**：8　**价格**：200 金

**物品 ID**：`I0PR`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.1 正式版

## 功能描述（人话版）

无可直接展示的数值效果（技能:传送水晶次数充值）

> 自动转写置信度 **low**。
> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。

## 可改数值项（改这些值会写进地图对象）

**类别**列里「每级数值」是技能对象 `Data` 里的分级数值，「表头字段」是技能级的冷却/耗魔/距离/范围/持续（与等级无关）。

| 数值项 | 当前值 | 字段 id | 等级 | 类别 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 跟随时间 | 0 | `Ncl1` | 1 | 每级数值 | — |
| 目标类型 | 0 | `Ncl2` | 1 | 每级数值 | 单位：点 |
| 选项 | 2 | `Ncl3` | 1 | 每级数值 | 单位：点 |
| 技术持续时间 | 0 | `Ncl4` | 1 | 每级数值 | — |
| 使其他技能无效 | 0 | `Ncl5` | 1 | 每级数值 | 单位：点 |
| 基本顺序 ID |  | `Ncl6` | 1 | 每级数值 | 单位：点 |
| 冷却 | 0.0 | `acdn` | 1 | 表头字段 | — |
| 魔法消耗 | 0 | `amcs` | 1 | 表头字段 | — |
| 持续时间 | 0.0 | `adur` | 1 | 表头字段 | — |
| 英雄持续时间 | 0.0 | `ahdu` | 1 | 表头字段 | — |
| 等级数 | 1 | `alev` | 0 | 表头字段 | — |


**怎么改**：到需求单仓库 `happy-fish-patch-plan` 打开 `data/item_ability_data.csv`，按 `item_code` + `ability_code` + `field` + `level` 找到对应行，把目标值写进 `new_value`，同行补 `req_id` 与 `note`；或者直接在「口语需求（自然语言）」Issue 里说人话，由我落表。

> ✔ = 该数值在游戏内说明里出现过（说明与对象数值对得上）。标 `x100` 的百分比项：CSV 里的 `cur_value` 存的是**原始小数**（0.1 = 10%），`new_value` 也要填小数。

**热键**：`Q`

## v1.1 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 跟随时间 | 0 | `ZRc0` | `Ncl1` | 1 |
| 目标类型 | 0 | `ZRc0` | `Ncl2` | 1 |
| 选项 | 2 | `ZRc0` | `Ncl3` | 1 |
| 技术持续时间 | 0 | `ZRc0` | `Ncl4` | 1 |
| 使其他技能无效 | 0 | `ZRc0` | `Ncl5` | 1 |
| 基本顺序 ID | channel | `ZRc0` | `Ncl6` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 |
| --- | --- | --- |
| `ZRc0` | 传送水晶次数充值 | 魔法施放时间间隔=0, 魔法消耗=0, 跟随时间=0, 目标类型=0, 选项=2, 技术持续时间=0, 使其他技能无效=0, 基本顺序 ID=channel |


> 对象数据没有给出这些能力的说明文字（`Ubertip` 为空），所以不列「能力说明」列。

### 游戏内说明（原文）

> 不归类
>
> 使用后消耗水晶，增加湖底之城传送次数3000次。
> 回车输入 hc5 传送，每次消耗1次。
> 次数属于使用者，并随队伍存档保存。

**提示工具（Tip）**：

```text
购买传送湖底之城水晶(Q)
```

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：商店『nhef』出售

_（本节无内容：`item_sources.json` 里这件物品的来源没有记到具体 BOSS/宝箱/店，只有「可获得」这一条笼统记录；逐条证据见下方「全部证据明细」。）_

### 全部证据明细

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| NPC:安莉 | `nhef` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:4353 |
| NPC:杂货商人(啪啪啪) | `ogru` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:5669 |
| NPC:俺妹不可能这么可爱 | `nckb` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:13811 |
| NPC:道具店（之黥） | `uktg` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:20681 |


## 合成与材料用途

_（本节无内容：`item_sources.json` 里这件物品既没有 `used_as_material`、也没有 `consumed_only` 记录，全物品的说明文本（Tip/Ubertip）里也没有任何物品提到它（文本匹配，不等于真实配方）；逐条证据见下方「全部证据明细」。）_

??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）——字段 id 与中文名的完整对照见 [对象字段对照表](../../info/对象字段对照表.md)。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `iico` **界面图标**（Art） = `ReplaceableTextures\CommandButtons\BTNGlyph.blp`
    - `ides` **描述**（Description） = `使用后消耗水晶，增加湖底之城传送次数3000次。 / 回车输入 hc5 传送，每次消耗1次。 / 次数属于使用者，并随队伍存档保存。`
    - `ihtp` **生命值**（HP） = `75`
    - `uhot` **热键**（Hotkey） = `Q`
    - `ilev` **等级**（Level） = `8`
    - `unam` **名字**（Name） = `传送湖底水晶`
    - `utip` **提示工具 - 基础**（Tip） = `购买传送湖底之城水晶(Q)`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `不归类 / 使用后消耗水晶，增加湖底之城传送次数3000次。 / 回车输入 hc5 传送，每次消耗1次。 / 次数属于使用者，并随队伍存档保存。`
    - `iabi` **技能**（abilList） = `ZRc0`
    - `iarm` **装甲类型**（armor） = `Wood`
    - `icla` **分类**（class） = `Unknown`
    - `iclb` **染色 3 (蓝色)**（colorB） = `255`
    - `iclg` **染色 2 (绿色)**（colorG） = `255`
    - `iclr` **染色 1 (红色)**（colorR） = `255`
    - `icid` **魔法施放间隔时间组**（cooldownID） = `ZRc0`
    - `idrp` **当携带者死亡时掉落**（drop） = `0`
    - `idro` **可以遗弃的**（droppable） = `1`
    - `ifil` **已使用的模型**（file） = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`
    - `igol` **金子消耗**（goldcost） = `200`
    - `iicd` **忽视延迟**（ignoreCD） = `0`
    - `ilum` **木材消耗**（lumbercost） = `0`
    - `imor` **转移有效目标**（morph） = `0`
    - `ilvo` **等级(无类别的)**（oldLevel） = `10`
    - `ipaw` **能被卖给商人**（pawnable） = `1`
    - `iper` **易腐烂的**（perishable） = `1`
    - `iprn` **包括随机选择**（pickRandom） = `1`
    - `ipow` **需要时自动使用**（powerup） = `0`
    - `ipri` **优先权**（prio） = `126`
    - `isca` **缩放值**（scale） = `1`
    - `issc` **选择大小 – 编辑器**（selSize） = `0`
    - `isel` **可以被商人出售**（sellable） = `1`
    - `isto` **最大储存**（stockMax） = `1`
    - `istr` **佣兵招募间隔**（stockRegen） = `1`
    - `isst` **佣兵招募时间**（stockStart） = `0`
    - `iusa` **主动使用**（usable） = `1`
    - `iuse` **负荷数量**（uses） = `1`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.1 正式版`（母图 SHA256 `8CD69840B265DA0ABE207575DB4DE9D07D961B59BA3491A390D07A923A17775C`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。哪些内容已被交叉验证、有哪些已知限制，见 [地图身份](../../info/地图身份.md)；本页符号（`—` / `未判定（证据不足）` / `⚠️ 不可选`）的含义见 [术语与用语](../../info/术语与用语.md)。

物品字段：`war3map.w3t`（SHA256 `5fe1ba0251226e4e0172e364aef1fbc35c6ea0726c7b8452c02018ba9ab01c0c`）；物品技能：`war3map.w3a`（SHA256 `b530c6578cb81d256e8b921993d5440242aef63a123a6d0a4bb128d0dfa71b8c`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
