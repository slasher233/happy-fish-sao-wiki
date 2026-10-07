# I0FK · 灵魂强化

> **分类**：不归类　**品质**：—　**类型**：Miscellaneous　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0FK`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 只能人造灵魂的武器才可以强化哦!
>
> 需求:毁灭钻石
>
> (提示:不一定成功有,失败消耗毁灭钻石，成功率60%每次+1都会降低10%的机会率,若+5灵魂可能会四分五裂)

**提示工具（Tip）**：

```text
灵魂强化
```

## 获取方式

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 玩家:冬妹子 | `nssn` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:29918 |


**拾取 / 使用触发**

| 方式 | 产出 | j 行号 |
| --- | --- | --- |
| recipe_scroll_used | `I0FM` 灵魂宝具(辉煌之刃)+1 | `29291` |
| recipe_scroll_used | `I0FN` 灵魂宝具(辉煌之刃)+2 | `29304` |
| recipe_scroll_used | `I0FO` 灵魂宝具(辉煌之刃)+3 | `29317` |
| recipe_scroll_used | `I0FP` 灵魂宝具(辉煌之刃)+4 | `29330` |
| recipe_scroll_used | `I0FQ` 灵魂宝具(辉煌之刃) | `29343` |
| recipe_scroll_used | `I0EP` 灵魂宝具(紫花姬)+1 | `29357` |
| recipe_scroll_used | `I0EN` 灵魂宝具(紫花姬)+2 | `29370` |
| recipe_scroll_used | `I0EO` 灵魂宝具(紫花姬)+3 | `29383` |
| recipe_scroll_used | `I0EL` 灵魂宝具(紫花姬)+4 | `29396` |
| recipe_scroll_used | `I0EM` 灵魂宝具(紫花姬)+5 | `29409` |
| recipe_scroll_used | `I0FF` 灵魂宝具(蓝纹飘带)+1 | `29423` |
| recipe_scroll_used | `I0FD` 灵魂宝具(蓝纹飘带)+2 | `29436` |
| recipe_scroll_used | `I0FH` 灵魂宝具(蓝纹飘带)+3 | `29449` |
| recipe_scroll_used | `I0FI` 灵魂宝具(蓝纹飘带)+4 | `29462` |
| recipe_scroll_used | `I0FG` 灵魂宝具(蓝纹飘带)+5 | `29475` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNOrbOfCorruption.blp`　*(界面图标)*
    - `ides` Description = `|cffff0000只能人造灵魂的武器才可以强化哦!|n|n需求:毁灭钻石|r|n|n(提示:不一定成功有,失败消耗毁灭钻石，成功率60%每次+1都会降低10%的机会率,若+5灵魂可能会四分五裂)`　*(描述)*
    - `unam` Name = `灵魂强化`　*(名字)*
    - `utip` Tip = `灵魂强化`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cffff0000只能人造灵魂的武器才可以强化哦!|n|n需求:毁灭钻石|r|n|n(提示:不一定成功有,失败消耗毁灭钻石，成功率60%每次+1都会降低10%的机会率,若+5灵魂可能会四分五裂)`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `iper` perishable = `1`　*(易腐烂的)*
    - `ipow` powerup = `1`　*(需要时自动使用)*
    - `istr` stockRegen = `3`　*(佣兵招募间隔)*
    - `iusa` usable = `1`　*(主动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
