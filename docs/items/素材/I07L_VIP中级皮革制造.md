# I07L · VIP中级皮革制造

> **分类**：素材　**品质**：—　**类型**：Miscellaneous　**物品等级**：—　**价格**：6000 金

**物品 ID**：`I07L`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

_（该物品没有属性类物品技能）_

### 物品能力

_（无 `iabi` 绑定）_

### 游戏内说明（原文）

> 在这里你可以享受更美好的待遇,呵呵
>
> 奇异的皮质.比较好的狼皮   制造:风衣
> 鳄鱼皮.蝙蝠翅膀           制造:蝙蝠之战鞋
> 穷人的布料.坚硬的壳子      制造:恒宇衣
> 土兽皮.魔法木头            制造:野兽烈衣
> 白狼皮.富人的布料          制造:白狼袍

**提示工具（Tip）**：

```text
VIP中级皮革制造
```

## 获取方式

**商店货架（对象数据 `usei`/`umki`）**

| 商店 | 商店单位 | 字段 | 字段名 | 证据位置 |
| --- | --- | --- | --- | --- |
| 工会:命运之夜 玩家:雪雪 | `orai` | `usei` | Sellitems 售出的物品 | note_log/index/w3u_verify.txt:6222 |


**拾取 / 使用触发**

| 方式 | 产出 | j 行号 |
| --- | --- | --- |
| recipe_scroll_used | `I07E` | `29236` |
| recipe_scroll_used | `I08H` | `29241` |
| recipe_scroll_used | `I08L` | `29246` |
| recipe_scroll_used | `I08P` | `29251` |


## 合成与材料用途

_（没有找到本物品参与合成或作为材料的证据）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNCC19.blp`　*(界面图标)*
    - `ides` Description = `|cff00ffff在这里你可以享受更美好的待遇,呵呵|n|n奇异的皮质.|r|cff7fff00比较好的狼皮   |r|cff00ffff制造:风衣|n鳄鱼皮.蝙蝠翅膀           制造:蝙蝠之战鞋|n穷人的布料.坚硬的壳子      制造:恒宇衣|n土兽皮.魔法木头            制造:野兽烈衣|n白狼皮.富人的布料          制造:白狼袍|r`　*(描述)*
    - `unam` Name = `VIP中级皮革制造`　*(名字)*
    - `utip` Tip = `VIP中级皮革制造`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff00ffff在这里你可以享受更美好的待遇,呵呵|n|n奇异的皮质.|r|cff7fff00比较好的狼皮   |r|cff00ffff制造:风衣|n鳄鱼皮.蝙蝠翅膀           制造:蝙蝠之战鞋|n穷人的布料.坚硬的壳子      制造:恒宇衣|n土兽皮.魔法木头            制造:野兽烈衣|n白狼皮.富人的布料          制造:白狼袍|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = ``　*(技能)*
    - `icla` class = `Miscellaneous`　*(分类)*
    - `igol` goldcost = `6000`　*(金子消耗)*
    - `ipow` powerup = `1`　*(需要时自动使用)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
