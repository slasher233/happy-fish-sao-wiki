# tpow · 未设置名称（原型 知识之书）

> **分类**：不归类　**品质**：无数据（说明里没写品质）　**类型**：未设置　**物品等级**：未设置　**价格**：未设置

**物品 ID**：`tpow`　·　**原型**：`tpow`（知识之书）　·　**版本**：v1.0 正式版

## 功能描述（人话版）

_（暂时写不出人话版描述：该物品没有绑定物品技能（`iabi` 为空），对象数据里只有名称/说明等文字字段。）_

## 可改数值项（改这些值会写进地图对象）

_（这件物品没有可机械修改的数值项。）_

> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 增加英雄1点的体力，敏捷度和筋力。

## 获取方式

- **能不能拿到**：可获得
- **怎么拿**：第3层《蜘蛛巢穴》BOSS『流氓』掉落（概率33%）
- **掉落层**：10/13/15/18/24/3/39/40/45/49/6/9
- **掉落 BOSS**：ndrf/ndrv/nrvi/ntkf/nwlg/图斯卡尔枪兵/堕落树人/无名死灵/流氓/熊怪/熊怪萨满/蜘蛛螃蟹/蜘蛛螃蟹巨兽/达拉内尔先驱/风暴撕裂者学徒/黑暗骑士/龙卵盗贼

### 按来源聚合的掉落（同一 BOSS/宝箱的多件掉落并排列出）

| 来源（组号） | 所在层 | 物品 ID | 物品名 | 概率% | 权重 | 数量 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **G002** 楼层BOSS·黑暗骑士（`Hlgr`） | 49 圣殿神堂 | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:20379；war3map.j:20387；war3map.j:20395；war3map.j:20403；war3map.j:20411；war3map.j:20419；war3map.j:20427；war3map.j:20435；war3map.j:20443 |
| **G014** 楼层BOSS（`nbdm`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18023 |
| **G018** 楼层BOSS（`ndrh`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18512 |
| **G020** 楼层BOSS（`nenc`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18764；war3map.j:18772；war3map.j:18780；war3map.j:18788 |
| **G022** 楼层BOSS（`nfod`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18904 |
| **G026** 楼层BOSS（`nfrl`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:19354；war3map.j:19362；war3map.j:19370；war3map.j:19378；war3map.j:19386 |
| **G027** 楼层BOSS（`nfrs`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:21048 |
| **G038** 楼层BOSS（`nrog`） |  | `tpow` | 知识之书 | 33 | 33 | 1 | war3map.j:17979 |
| **G040** 楼层BOSS（`nsc3`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18188；war3map.j:18196；war3map.j:18204 |
| **G041** 楼层BOSS（`nscb`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:18312；war3map.j:18344；war3map.j:18352；war3map.j:18360；war3map.j:18368 |
| **G042** 楼层BOSS（`nsra`） |  | `tpow` | 知识之书 | 100 | 100 | 1 | war3map.j:20507；war3map.j:20515 |
| **G043** 楼层BOSS（`ntka`） |  | `tpow` | 知识之书 | 34 | 34 | 1 | war3map.j:19461；war3map.j:19462；war3map.j:19470；war3map.j:19478 |


> 组号 = `drops_by_boss.csv` 里的一格来源；同一组的继续行留空，表示它们来自同一个来源。

### 全部证据明细

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nrog` LV5:(the spider lord) | RandomDist (Blizzard.j 权重表) | 33% | `17979` |
| `nbdm` Lv:8(Sly piranha) | RandomDist (Blizzard.j 权重表) | 100% | `18023` |
| `nsc3` ★Lv12(the forest owner)★ | RandomDist (Blizzard.j 权重表) | 100% | `18188` |
| `nsc3` ★Lv12(the forest owner)★ | RandomDist (Blizzard.j 权重表) | 100% | `18196` |
| `nsc3` ★Lv12(the forest owner)★ | RandomDist (Blizzard.j 权重表) | 100% | `18204` |
| `nscb` Lv:11(The Cemetery Guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18312` |
| `nscb` Lv:11(The Cemetery Guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18344` |
| `nscb` Lv:11(The Cemetery Guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18352` |
| `nscb` Lv:11(The Cemetery Guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18360` |
| `nscb` Lv:11(The Cemetery Guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18368` |
| `ndrh` Lv13:(forest guardian) | RandomDist (Blizzard.j 权重表) | 100% | `18512` |
| `ndrf` Lv:11(cruel animals) | RandomDist (Blizzard.j 权重表) | 100% | `18568` |
| `ndrf` Lv:11(cruel animals) | RandomDist (Blizzard.j 权重表) | 100% | `18576` |
| `ndrf` Lv:11(cruel animals) | RandomDist (Blizzard.j 权重表) | 100% | `18584` |
| `ndrf` Lv:11(cruel animals) | RandomDist (Blizzard.j 权重表) | 100% | `18592` |
| `ndrf` Lv:11(cruel animals) | RandomDist (Blizzard.j 权重表) | 100% | `18600` |
| `ntkf` Lv50:(The evil eye) | RandomDist (Blizzard.j 权重表) | 100% | `18688` |
| `ntkf` Lv50:(The evil eye) | RandomDist (Blizzard.j 权重表) | 100% | `18696` |
| `ntkf` Lv50:(The evil eye) | RandomDist (Blizzard.j 权重表) | 100% | `18704` |
| `ntkf` Lv50:(The evil eye) | RandomDist (Blizzard.j 权重表) | 100% | `18712` |
| `ntkf` Lv50:(The evil eye) | RandomDist (Blizzard.j 权重表) | 100% | `18720` |
| `nenc` Lv15:★(The people who visit soul)★ | RandomDist (Blizzard.j 权重表) | 100% | `18764` |
| `nenc` Lv15:★(The people who visit soul)★ | RandomDist (Blizzard.j 权重表) | 100% | `18772` |
| `nenc` Lv15:★(The people who visit soul)★ | RandomDist (Blizzard.j 权重表) | 100% | `18780` |
| `nenc` Lv15:★(The people who visit soul)★ | RandomDist (Blizzard.j 权重表) | 100% | `18788` |
| `nfod` Lv22:(Bone emperor) | RandomDist (Blizzard.j 权重表) | 100% | `18904` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19004` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19012` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19020` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19028` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19036` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19044` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19052` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19060` |
| `nwlg` Lv:40伊偌-亚兰·德兹 | RandomDist (Blizzard.j 权重表) | 100% | `19068` |
| `nfrl` Lv:32(树人中的王者) | RandomDist (Blizzard.j 权重表) | 100% | `19354` |
| `nfrl` Lv:32(树人中的王者) | RandomDist (Blizzard.j 权重表) | 100% | `19362` |
| `nfrl` Lv:32(树人中的王者) | RandomDist (Blizzard.j 权重表) | 100% | `19370` |
| `nfrl` Lv:32(树人中的王者) | RandomDist (Blizzard.j 权重表) | 100% | `19378` |
| `nfrl` Lv:32(树人中的王者) | RandomDist (Blizzard.j 权重表) | 100% | `19386` |
| `ntka` Lv65:(Pearl 's Monster) | RandomDist (Blizzard.j 权重表) | 34% | `19461` |
| `ntka` Lv65:(Pearl 's Monster) | RandomDist (Blizzard.j 权重表) | 33% | `19462` |
| `ntka` Lv65:(Pearl 's Monster) | RandomDist (Blizzard.j 权重表) | 100% | `19470` |
| `ntka` Lv65:(Pearl 's Monster) | RandomDist (Blizzard.j 权重表) | 100% | `19478` |
| `ndrv` 宝物箱子 | RandomDist (Blizzard.j 权重表) | 33% | `19810` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20379` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20387` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20395` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20403` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20411` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20419` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20427` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20435` |
| `Hlgr` 魂魄妖梦 | RandomDist (Blizzard.j 权重表) | 100% | `20443` |
| `nsra` Lv69:The monster caused in disaster | RandomDist (Blizzard.j 权重表) | 100% | `20507` |
| `nsra` Lv69:The monster caused in disaster | RandomDist (Blizzard.j 权重表) | 34% | `20515` |
| `nfrs` Lv65:(asura) | RandomDist (Blizzard.j 权重表) | 100% | `21048` |
| `nrvi` 公会:微笑棺材 会长:幽冥 | RandomDist (Blizzard.j 权重表) | 100% | `24460` |
| `nrvi` 公会:微笑棺材 会长:幽冥 | RandomDist (Blizzard.j 权重表) | 100% | `24488` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。
    正常阅读不用看这里；要改数值请看上面的「可改数值项」。

    - `ides` **描述**（Description） = `增加英雄1点的体力，敏捷度和筋力。`
    - `utub` **提示工具 - 扩展的**（Ubertip） = `增加英雄1点的体力，敏捷度和筋力。`


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
