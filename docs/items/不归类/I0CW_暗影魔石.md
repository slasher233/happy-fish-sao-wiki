# I0CW · 暗影魔石

> **分类**：不归类　**品质**：—　**类型**：Permanent　**物品等级**：60　**价格**：5000 金

**物品 ID**：`I0CW`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 带着黑色的光芒的石头,有着诡异的一面,但是却是一种很稀有的材料

**提示工具（Tip）**：

```text
暗影魔石
```

## 获取方式

**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `nowk` Lv43:（意念巨兽） | ChooseRandomItemExBJ(level, itemClass) | — | `32668` |


**作为材料被消耗**

| 触发卷轴/菜单 | 合成结果 | j 行号 |
| --- | --- | --- |
| VIP中级金属甲类防具打造 `I08F` | `I0D1` b海豹面具 | `29222` |


## 合成与材料用途

**作为材料参与合成（触发器证据）**：

| 触发卷轴/菜单 | 合成结果 | j 行号 |
| --- | --- | --- |
| VIP中级金属甲类防具打造 `I08F` | `I0D1` b海豹面具 | `29222` |


**说明文本中提到本物品的物品**（文本匹配，不等于真实配方）：

| 物品 ID | 物品名称 |
| --- | --- |
| `I08F` | 暗影魔石 |
| `I0BU` | 暗影魔石 |


??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNOrb.blp`　*(界面图标)*
    - `ides` Description = `|cff8a2be2带着黑色的光芒的石头,有着诡异的一面,但是却是一种很稀有的材料|r`　*(描述)*
    - `ilev` Level = `60`　*(等级)*
    - `unam` Name = `|cff8a2be2暗影魔石|r`　*(名字)*
    - `utip` Tip = `|cff8a2be2暗影魔石|r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff8a2be2带着黑色的光芒的石头,有着诡异的一面,但是却是一种很稀有的材料|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Permanent`　*(分类)*
    - `igol` goldcost = `5000`　*(金子消耗)*
    - `ilvo` oldLevel = `60`　*(等级(无类别的))*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
