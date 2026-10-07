# I06J · 真红剑★★☆r

> **分类**：副武器　**品质**：究极　**类型**：Charged　**物品等级**：—　**价格**：— 金

**物品 ID**：`I06J`　·　**原型**：`ckng`（国王之冠 +5）　·　**版本**：v1.0 正式版

## v1.0 正式版 当前数据

### 基础属性

| 属性 | 数值 | 来源能力 | 字段 | 等级 |
| --- | --- | --- | --- | --- |
| 攻击奖励 | 110 | `A019` | `Iatt` | 1 |
| 攻击速度增加 | 0.56 | `A080` | `Isx1` | 1 |
| 分布式伤害因素 | 0.2 | `A0CJ` | `nca1` | 1 |

### 物品能力

| 能力 ID | 能力名称 | 关键数值 | 能力说明 |
| --- | --- | --- | --- |
| `A019` | 增加攻击110 | 攻击奖励=110 | — |
| `A080` | 增加攻击速度56 | 攻击速度增加=0.56 | — |
| `A0CJ` | 隔绝斩击Lv3 | 分布式伤害因素=0.2 | — |

### 游戏内说明（原文）

> -副武器
>
> 攻击力:110
> 攻击速度:56
> 能力:隔绝斩击Lv3(E级)
> (此能力远程攻击类型无法使用)
> 品质:究极
>
> 像鲜红的血一样,却不让人讨厌,仿佛在吸引着各种生活去使用它!

**提示工具（Tip）**：

```text
真红剑★★☆r
```

## 获取方式

**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。

> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。

## 合成与材料用途

_（没有其它物品的说明提到本物品）_

??? note "全部对象字段（原始值）"

    - `iico` Art = `ReplaceableTextures\CommandButtons\BTNCC30.blp`　*(界面图标)*
    - `ides` Description = `|cff9db9eb-副武器|r|n|n|cffff7f50攻击力:110|n攻击速度:56|n能力:隔绝斩击Lv3(E级)|n(此能力远程攻击类型无法使用)|n品质:究极|n|n像鲜红的血一样,却不让人讨厌,仿佛在吸引着各种生活去使用它!|r`　*(描述)*
    - `unam` Name = `|cffff7f50真红剑★★☆r`　*(名字)*
    - `utip` Tip = `|cffff7f50真红剑★★☆r`　*(提示工具 - 基础)*
    - `utub` Ubertip = `|cff9db9eb-副武器|r|n|n|cffff7f50攻击力:110|n攻击速度:56|n能力:隔绝斩击Lv3(E级)|n(此能力远程攻击类型无法使用)|n品质:究极|n|n像鲜红的血一样,却不让人讨厌,仿佛在吸引着各种生活去使用它!|r`　*(提示工具 - 扩展的)*
    - `iabi` abilList = `A019,A080,A0CJ`　*(技能)*
    - `icla` class = `Charged`　*(分类)*


---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。

物品字段：`war3map.w3t`（SHA256 `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d`）；物品技能：`war3map.w3a`（SHA256 `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3`）；物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。

</div>
