# tin2 · 体力之书 +2

> **分类**：消耗品　**品质**：无数据（说明里没写品质）　**类型**：未设置　**物品等级**：未设置　**价格**：未设置

**物品 ID**：`tin2`　·　**原型**：`tin2`（智力之书 +2）　·　**版本**：v1.0 正式版

## 功能描述（人话版）

_（暂时写不出人话版描述：该物品没有绑定物品技能（`iabi` 为空），对象数据里只有名称/说明等文字字段。）_

> 自动转写置信度 **low**；与说明原文的差异：无技能引用 1 处。
> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。

## 可改数值项（改这些值会写进地图对象）

_（这件物品没有可机械修改的数值项。）_

> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 能永久地增加英雄2点的体力。

**提示工具（Tip）**：

```text
购买体力之书 +2
```

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：第3层《蜘蛛巢穴》BOSS『流氓』掉落（概率33%）
- **掉落层**：13/3/34/5
- **掉落 BOSS**：ndqs/强制者/恐怖猛犸/流氓/达拉内尔先驱

### 按来源聚合的掉落（同一 BOSS/宝箱的多件掉落并排列出）

| 来源（组号） | 所在层 | 物品 ID | 物品名 | 概率% | 权重 | 数量 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **G018** 楼层BOSS·达拉内尔先驱（`ndrh`） | 13 道路森林 | `tin2` | 体力之书 +2 | 100 | 100 | 1 | war3map.j:18488 |
| **G021** 楼层BOSS（`nenf`） |  | `tin2` | 体力之书 +2 | 25 | 25 | 1 | war3map.j:18107 |
| **G031** 楼层BOSS·恐怖猛犸（`nmdr`） | 34 吻雪森林 | `tin2` | 体力之书 +2 | 100 | 100 | 1 | war3map.j:20234；war3map.j:20242；war3map.j:20250；war3map.j:20258；war3map.j:20266 |
| **G038** 楼层BOSS（`nrog`） |  | `tin2` | 体力之书 +2 | 33 | 33 | 1 | war3map.j:17978 |


> 组号 = `drops_by_boss.csv` 里的一格来源；同一组的继续行留空，表示它们来自同一个来源。

### 全部证据明细

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nrog` LV5:(the spider lord) | RandomDist (Blizzard.j 权重表) | 33% | `17978` |
| `nenf` ★Lv:7（Early three head snake)★ | RandomDist (Blizzard.j 权重表) | 25% | `18107` |
| `ndrh` Lv13:(forest guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18488` |
| `nmdr` Lv55:(The indifferent giant) | RandomDist (Blizzard.j 权重表) | 100% | `20234` |
| `nmdr` Lv55:(The indifferent giant) | RandomDist (Blizzard.j 权重表) | 100% | `20242` |
| `nmdr` Lv55:(The indifferent giant) | RandomDist (Blizzard.j 权重表) | 100% | `20250` |
| `nmdr` Lv55:(The indifferent giant) | RandomDist (Blizzard.j 权重表) | 100% | `20258` |
| `nmdr` Lv55:(The indifferent giant) | RandomDist (Blizzard.j 权重表) | 100% | `20266` |
| `ndqs` Lv50:(The killer of Massacre) | RandomDist (Blizzard.j 权重表) | 100% | `20760` |
| `ndqs` Lv50:(The killer of Massacre) | RandomDist (Blizzard.j 权重表) | 100% | `20768` |
| `ndqs` Lv50:(The killer of Massacre) | RandomDist (Blizzard.j 权重表) | 100% | `20776` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `ides` **描述**（Description） = `能永久地增加英雄的体力。`
    - `unam` **名字**（Name） = `体力之书 +2`
    - `utip` **提示工具 - 基础**（Tip） = `购买体力之书 +2`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `能永久地增加英雄2点的体力。`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
