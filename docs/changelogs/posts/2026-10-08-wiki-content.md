---
map_version: "v1.0 正式版"
date:
  created: 2026-10-08
authors: [wiki]
categories: [Wiki 更新]
---

# Wiki 内容补全：获取途径、专属装备、楼层与存档

本次没有修改地图。所有新增内容都是从母图成员里**静态解析**出来的，逐条带 `war3map.j` 行号。

<!-- more -->

## 物品页：获取方式

**499 / 551（90.6%）** 个物品拿到了至少一条获取途径证据，按渠道分块：

| 渠道 | 说明 |
| --- | --- |
| `drop` / `boss_pool` | 单位死亡掉落表（`RandomDist` 权重表、`ChooseRandomItemExBJ` 等级表）、BOSS 专属掉落池 |
| `vendor` / `vendor_object_data` | 商店出售（JASS 进货接口与对象数据里的货架 `usei`/`umki`） |
| `craft` / `craft_station` | 配方卷轴打造、通用合成台 |
| `gacha` / `tower_reward` / `gift` | 抽奖机、通天塔层奖励、NPC 赠送 |
| `grow` / `grow_into` | 击杀累积成长链 |
| `trigger_use` / `used_as_material` | 被触发器消耗或作为材料 |

仍有 39 个物品**没有任何获取证据**（在页面上标为「待考证」），另有 52 个物品只有上下文证据。

## 英雄页：专属装备

本图**不用哈希表存「英雄→物品」配对**。专属关系由唯一白名单函数
`EXEQ_Allowed(unit, integer)`（`war3map.j:87157-87312`）决定，拾取时由
`EXEQ_InventoryEvent`（`war3map.j:88094-88112`）强制移除不合规物品。

- 60 个英雄条目里 **34 个英雄类型有专属物品证据**（41 件专属物品）。
- 其中 5 件按**玩家昵称**判定（`J0H6`/`J0L4`/`K001`/`K002`/`K004`），无法归属到英雄类型，页面上单独标注为「限定使用（按玩家昵称）」。
- 4 件来自旧版硬编码触发器（`war3map.j:30892-30931`）。

## 楼层与 Boss、存档与读档

- 楼层/传送/掉落与 BOSS 数据：见「资料 → 楼层信息」。
- 存档格式说明：见「资料 → 存档与读档」。

## 仍然没有证据的部分

- **技能解锁与升级等级**：本图技能对象全部只有 1 级（`alev=1`），升级由触发器控制，对象数据里没有可读值 → 一律标「待考证」。
- **实机验证**：Wiki 全部内容都是静态解析，**没有进过游戏**。

---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` / `war3map.j` 与 4 个 Lua 模块解析生成；**未经过实机验证**。

</div>
