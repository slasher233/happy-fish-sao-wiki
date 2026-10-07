# I0FV · 死亡骷髅钥匙

> **分类**：任务物品　**品质**：—　**类型**：Permanent　**物品等级**：—　**价格**：— 金

**物品 ID**：`I0FV`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 用骷髅所做的钥匙,看上去很恶心

**提示工具（Tip）**：

```text
死亡骷髅钥匙
```

## 获取方式

**打造 / 合成**

| 触发物 | 消耗材料 | j 行号 | 备注 |
| --- | --- | --- | --- |
| 魔神的事迹 `I0FU` | `I03I` 毁灭钻石 | `37742` | — |


**掉落（掉落表 / 权重表）**

| 来源单位 | 方式 | 概率 | j 行号 |
| --- | --- | --- | --- |
| `n023` Lv85:小馋猫 | RandomDist (Blizzard.j 权重表) | 100% | `22639` |
| `n022` Lv85:Sword | RandomDist (Blizzard.j 权重表) | 100% | `22667` |


**触发时赠予**

| 方式 | 给谁 | j 行号 |
| --- | --- | --- |
| unclassified_give | GetTriggerUnit( | `37744` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNWandSkull.blp`　*(界面图标)*
    - `ides` Description = `用骷髅所做的钥匙,看上去很恶心`　*(描述)*
    - `unam` Name = `死亡骷髅钥匙`　*(名字)*
    - `utip` Tip = `死亡骷髅钥匙`　*(提示工具 - 基础)*
    - `utub` Ubertip = `用骷髅所做的钥匙,看上去很恶心`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Permanent`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
