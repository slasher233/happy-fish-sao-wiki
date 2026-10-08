# I0GT · 传送湖底之城

> **分类**：传送与关卡　**品质**：无数据（说明里没写品质）　**类型**：杂项（原始枚举 `Miscellaneous`）　**物品等级**：未设置　**价格**：未设置

**物品 ID**：`I0GT`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## 功能描述（人话版）

魔法施放时间间隔 5；持续时间 - 普通 0.1；持续时间 - 英雄 0.1

> 自动转写置信度 **low**；与说明原文的差异：无技能引用 1 处。
> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。

## 可改数值项（改这些值会写进地图对象）

_（这件物品没有可机械修改的数值项。）_

> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。

**热键**：`D`

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

| 能力 ID | 能力名称 | 关键数值 |
| --- | --- | --- |
| `A0OQ` | 传送湖底之城 | 魔法施放时间间隔=5, 魔法消耗=0 |


> 对象数据没有给出这些能力的说明文字（`Ubertip` 为空），所以只列绑定关系与关键数值。

### 游戏内说明（原文）

> 能力:能让自己前往湖底之城

_（提示工具（Tip）与物品名相同，没有额外说明。）_

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：BOSS『ndqp』掉落（权重100）
- **掉落 BOSS**：ndqp

_（这件物品的获取方式没有按来源聚合成组，见下方证据明细。）_

### 全部证据明细

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `ndqp` Lv50:(.The killer of Massacre 2) | RandomDist (Blizzard.j 权重表) | 100% | `20676` |
| `ndqp` Lv50:(.The killer of Massacre 2) | RandomDist (Blizzard.j 权重表) | 100% | `20684` |
| `ndqp` Lv50:(.The killer of Massacre 2) | RandomDist (Blizzard.j 权重表) | 100% | `20692` |
| `ndqp` Lv50:(.The killer of Massacre 2) | RandomDist (Blizzard.j 权重表) | 100% | `20700` |


## 合成与材料用途

**说明文本中提到本物品的物品**（文本匹配，不等于真实配方）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I0HI` | 传送湖底之城 |
| `I0IT` | 传送湖底之城 |


??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `iico` **界面图标**（Art） = `ReplaceableTextures\CommandButtons\BTNCC25.blp`
    - `ides` **描述**（Description） = `能力:能让自己前往湖底之城`
    - `uhot` **热键**（Hotkey） = `D`
    - `unam` **名字**（Name） = `传送湖底之城`
    - `utip` **提示工具 - 基础**（Tip） = `传送湖底之城`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `能力:能让自己前往湖底之城`
    - `iabi` **技能**（abilList） = `A0OQ`
    - `icla` **分类**（class） = `Miscellaneous`
    - `icid` **魔法施放间隔时间组**（cooldownID） = `A0OQ`
    - `istr` **佣兵招募间隔**（stockRegen） = `3`
    - `iusa` **主动使用**（usable） = `1`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
