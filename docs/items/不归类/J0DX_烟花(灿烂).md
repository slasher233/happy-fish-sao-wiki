# J0DX · 烟花(灿烂)

> **分类**：不归类　**品质**：无数据（说明里没写品质）　**类型**：充能（原始枚举 `Charged`）　**物品等级**：8　**价格**：0 金

**物品 ID**：`J0DX`　·　**原型**：`ches`（奶酪）　·　**版本**：v1.0 正式版

## 功能描述（人话版）

_（暂时写不出人话版描述：该物品没有绑定物品技能（`iabi` 为空），对象数据里只有名称/说明等文字字段。）_

> 自动转写置信度 **low**；与说明原文的差异：无技能引用 1 处。
> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。

## 可改数值项（改这些值会写进地图对象）

_（这件物品没有可机械修改的数值项。）_

> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。

**热键**：`K`

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 由某人所制造的烟花,能释放出灿烂的烟火
>
> 能力:能让自己获得扭蛋卷*2

_（提示工具（Tip）与物品名相同，没有额外说明。）_

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：打造/合成获得

_（这件物品的获取方式没有按来源聚合成组，见下方证据明细。）_

### 全部证据明细

**打造 / 合成**

| 触发物 | 消耗材料 | j 行号 | 备注 |
| --- | --- | --- | --- |
| （自动合成） |  | `65415` | — |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `iico` **界面图标**（Art） = `ReplaceableTextures\CommandButtons\BTNHumanArtilleryUpOne.blp`
    - `ides` **描述**（Description） = `由某人所制造的烟花,能释放出灿烂的烟火 / 能力:能让自己获得扭蛋卷*2`
    - `ihtp` **生命值**（HP） = `75`
    - `uhot` **热键**（Hotkey） = `K`
    - `ilev` **等级**（Level） = `8`
    - `unam` **名字**（Name） = `烟花(灿烂)`
    - `utip` **提示工具 - 基础**（Tip） = `烟花(灿烂)`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `由某人所制造的烟花,能释放出灿烂的烟火 / 能力:能让自己获得扭蛋卷*2`
    - `iabi` **技能**（abilList） = `（对象数据中此字段为空字符串）`
    - `iarm` **装甲类型**（armor） = `Wood`
    - `icla` **分类**（class） = `Charged`
    - `iclb` **染色 3 (蓝色)**（colorB） = `255`
    - `iclg` **染色 2 (绿色)**（colorG） = `255`
    - `iclr` **染色 1 (红色)**（colorR） = `255`
    - `icid` **魔法施放间隔时间组**（cooldownID） = `A0KT`
    - `idrp` **当携带者死亡时掉落**（drop） = `0`
    - `idro` **可以遗弃的**（droppable） = `1`
    - `ifil` **已使用的模型**（file） = `Objects\InventoryItems\TreasureChest\treasurechest.mdl`
    - `igol` **金子消耗**（goldcost） = `0`
    - `iicd` **忽视延迟**（ignoreCD） = `1`
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
    - `isto` **最大储存**（stockMax） = `10`
    - `istr` **佣兵招募间隔**（stockRegen） = `120`
    - `isst` **佣兵招募时间**（stockStart） = `0`
    - `iusa` **主动使用**（usable） = `1`
    - `iuse` **负荷数量**（uses） = `1`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
