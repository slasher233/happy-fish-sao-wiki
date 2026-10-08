# 英雄图鉴

共 **60** 条英雄数据 = **58** 个可选 + **2** 个地图上无此单位（`note_log/recon/heroes.tsv` 共 60 行）。开局在选人区把单位**双击**即可选中（触发器 `Lz` / `iy4`）。

| 说明 | 内容 |
| --- | --- |
| 可选英雄 | 58（另有 2 个地图上无此单位 → 合计 60 条数据） |
| 选人方式 | 双击 `Player(15)` 所属的选人单位 |
| 技能键位 | Q/W/E/R/F/D（对象数据 `abpx/abpy` 判定） |
| 地图上无此单位 | `H00U`、`H01O`（`PH_PortInit` 注册表不含这些 code，两页页内有 ⚠️ 警告） |
| 名单备注与选人注册表不一致（仍计为可选） | `Nsjs`（名单备注「不在 `PH_PortInit` 注册表」，计入上面 58 个可选里） |
| 技能类型口径 | 主动 / 被动 / 未判定（证据不足）三态，见各页「技能取得」表下说明 |
| 有专属装备证据的英雄 | 34 / 60（判定函数 `EXEQ_Allowed`，`war3map.j:87157-87312`） |

| ID | 名称 | 称号 | 主属性 | 可选 | 技能绑定 |
| --- | --- | --- | --- | --- | --- |
| [`H000`](<%E5%96%B5%E9%9C%B2%E6%9C%B5%E9%9C%B2%E8%96%87.md>) | 喵露朵露薇 | 喵露朵露薇 | 敏捷 | ✅ 可选 | Q:Z0TF　W:Z0U4　E:Z0TC　R:Z0TG　F:—　D:Z0TH |
| [`H001`](<%E5%96%B5%E5%96%B5%E6%8B%B3.md>) | 喵喵拳 | 喵喵拳（星川凌云） | 敏捷 | ✅ 可选 | Q:Z13Q　W:Z13R　E:Z13P　R:Z13S　F:Z13T　D:Z13O |
| [`H002`](<%E7%BA%A2%E7%BE%8E%E7%8E%B2.md>) | 红美玲 | 红美玲（暗黑红美玲） | 敏捷 | ✅ 可选 | Q:Z148　W:Z149　E:Z14A　R:Z14C　F:Z14B　D:Z14D |
| [`H003`](<%E8%B0%8F%E5%B1%B1%E9%BB%84%E6%B3%89.md>) | 谏山黄泉 | 谏山黄泉 | 敏捷 | ✅ 可选 | Q:Z17H　W:Z17I　E:Z17J　R:Z17K　F:—　D:Z17G |
| [`H004`](<%E4%B8%BA%E4%B8%96%E7%95%8C%E5%8D%96%E8%90%8C.md>) | 为世界卖萌 | 为世界卖萌（未来初音） | 敏捷 | ✅ 可选 | Q:Z0HM　W:Z0HR　E:Z0HN　R:Z0I1　F:—　D:— |
| [`H005`](<%E7%90%AA%E5%B0%94%E7%8E%9B%E5%88%A9%E4%BA%9A.md>) | 琪尔玛利亚 | 琪尔玛利亚（M·R） | 敏捷 | ✅ 可选 | Q:Z0CU　W:Z0CT　E:Z0CX　R:Z0HC　F:—　D:Z0CQ |
| [`H006`](<%E4%BA%94%E6%B2%B3%E7%90%B4%E9%87%8C.md>) | 五河琴里 | 五河琴里 | 体力 | ✅ 可选 | Q:Z12Z　W:Z0DG　E:Z130　R:Z0DH　F:—　D:Z12X |
| [`H007`](<%E9%BB%91%E7%8C%AB%E9%85%B1.md>) | 黑猫酱 | 黑猫酱（五更琉璃） | 体力 | ✅ 可选 | Q:Z0HO　W:Z0HS　E:Z0HT　R:Z0HU　F:—　D:— |
| [`H00C`](<%E6%B0%B8%E8%BF%9C%E7%9A%84%E9%B2%9C%E7%BA%A2%E5%B9%BC%E6%9C%88.md>) | 永远的鲜红幼月 | 永远的鲜红幼月（蕾米莉亚·斯卡雷特） | 敏捷 | ✅ 可选 | Q:Z0OX　W:Z10W　E:Z0A1　R:Z0A0　F:—　D:Z0A7 |
| [`H00D`](<%E7%A5%88%E6%9C%80%E7%88%B1%E7%9A%84%E5%A7%90%E5%A7%90%E5%A4%A7%E4%BA%BA.md>) | 祈最爱的姐姐大人 | 祈最爱的姐姐大人（御坂美琴） | 敏捷 | ✅ 可选 | Q:Z14I　W:Z14J　E:Z14L　R:Z14M　F:—　D:Z14O |
| [`H00E`](<%E7%A9%BF%E8%B6%8A%E6%97%B6%E7%A9%BA%E7%9A%84%E5%B0%91%E5%A5%B3.md>) | 穿越时空的少女 | 穿越时空的少女（椎名真白） | 体力 | ✅ 可选 | Q:Z138　W:Z139　E:Z08Y　R:Z092　F:—　D:— |
| [`H00J`](<%E9%AD%94%E5%A5%B3.md>) | 魔女 | 魔女 | 筋力 | ✅ 可选 | Q:Z0BY　W:Z0SC　E:Z0SD　R:Z0SB　F:—　D:Z0SA |
| [`H00K`](<%E7%BA%A2%E5%8F%B6.md>) | 红叶 | 红叶 | 敏捷 | ✅ 可选 | Q:Z0SF　W:Z0SG　E:Z0SH　R:Z0SI　F:—　D:Z0SE |
| [`H00P`](<%E7%BC%87%E5%A8%9C.md>) | 缇娜 | 缇娜 | 体力 | ✅ 可选 | Q:Z0TM　W:Z0TO　E:Z0TL　R:Z0TN　F:—　D:Z0TK |
| [`H00Q`](<%E5%96%B5%E5%8F%AF%E8%8E%89.md>) | 喵可莉 | 喵可莉 | 敏捷 | ✅ 可选 | Q:Z0TP　W:Z0TQ　E:Z0TR　R:Z0TS　F:—　D:Z0TT |
| [`H00S`](<%E8%8E%89%E4%BC%8A.md>) | 莉伊 | 莉伊 | 体力 | ✅ 可选 | Q:Z0U2　W:Z0TY　E:Z0U1　R:Z0U0　F:—　D:Z0TZ |
| [`H00T`](<%E8%8E%89%E8%8E%89%E4%B8%9D%E5%BF%92%E6%8B%89_H00T.md>) | 莉莉丝忒拉 | 莉莉丝忒拉（克萝伊·莉莉丝忒拉） | 敏捷 | ✅ 可选 | Q:Z10I　W:Z10J　E:Z10K　R:Z10L　F:—　D:— |
| [`H00U`](<%E8%8E%89%E8%8E%89%E4%B8%9D%E5%BF%92%E6%8B%89_H00U.md>) | 莉莉丝忒拉 | 莉莉丝忒拉（克萝伊·莉莉丝忒拉(真)） | 敏捷 | ❌ 地图上无此单位 | Q:Z10I　W:Z10J　E:Z10K　R:Z10L　F:—　D:— |
| [`H00V`](<%E7%89%B9%E8%8E%89%E6%B3%A2%E5%8D%A1.md>) | 特莉波卡 | 特莉波卡 | 敏捷 | ✅ 可选 | Q:Z12F　W:Z12G　E:Z12H　R:Z13I　F:—　D:Z12E |
| [`H00W`](<%E5%AD%A4%E7%8B%AC%E8%BD%AE%E5%9B%9E%E8%A7%82%E6%B5%8B%E8%80%85.md>) | 孤独轮回观测者 | 孤独轮回观测者（祸灵梦） | 体力 | ✅ 可选 | Q:Z13X　W:Z13Y　E:Z143　R:Z141　F:Z142　D:— |
| [`H00X`](<%E6%A2%A6%E6%A2%A6.md>) | 梦梦 | 梦梦（贝莉雅·戴比路克） | 体力 | ✅ 可选 | Q:Z16M　W:Z16N　E:Z16O　R:—　F:—　D:Z16H |
| [`H00Y`](<%E9%AD%85%E5%BD%B1.md>) | 魅影 | 魅影（魅影十字军） | 筋力 | ✅ 可选 | Q:Z18K　W:Z18L　E:Z18M　R:Z18N　F:Z18P　D:Z18R |
| [`H00Z`](<%E5%B0%81%E5%BC%8A%E8%80%85.md>) | 封弊者 | 封弊者（桐谷和人） | 敏捷 | ✅ 可选 | Q:Z06L　W:Z0Y3　E:Z06G　R:Z17F　F:Z0IN　D:Z0Y4 |
| [`H010`](<%E7%BB%9D%E5%89%91.md>) | 绝剑 | 绝剑（优纪） | 体力 | ✅ 可选 | Q:Z0L6　W:Z0L7　E:Z0M6　R:Z0L9　F:Z0MN　D:Z0L5 |
| [`H013`](<%E6%96%AF%E6%89%98%E8%95%BE%E4%BA%9A.md>) | 斯托蕾亚 | 斯托蕾亚 | 筋力 | ✅ 可选 | Q:Z17X　W:Z0CF　E:Z0CB　R:Z17W　F:Z0IN　D:Z0CE |
| [`H014`](<%E5%86%AC.md>) | 冬 | 冬（夜刀神十香） | 筋力 | ✅ 可选 | Q:Z0D0　W:Z0D4　E:Z0AW　R:Z0D3　F:Z0D2　D:Z0CY |
| [`H015`](<%E9%A3%8E%E6%9E%97%E7%81%AB%E5%B1%B1%E4%BC%9A%E9%95%BF.md>) | 风林火山会长 | 风林火山会长（克莱因） | 筋力 | ✅ 可选 | Q:Z0FU　W:Z0FV　E:Z0FY　R:Z1FX　F:Z0IN　D:Z0B8 |
| [`H016`](<%E4%B8%83%E7%9A%87.md>) | 七皇 | 七皇（动念女神） | 体力 | ✅ 可选 | Q:Z07F　W:Z07K　E:Z07X　R:Z0BF　F:—　D:Z08U |
| [`H017`](<%E7%BB%88%E4%BB%8E%E9%BB%91%E6%9A%97%E4%B8%AD%E8%B5%B0%E5%87%BA%E7%9A%84%E6%88%98%E5%A3%AB.md>) | 终从黑暗中走出的战士 | 终从黑暗中走出的战士（MC） | 敏捷 | ✅ 可选 | Q:Z0GX　W:—　E:Z0GW　R:—　F:—　D:— |
| [`H019`](<%E9%A9%AF%E5%85%BD%E5%B8%88.md>) | 驯兽师 | 驯兽师（西莉卡） | 体力 | ✅ 可选 | Q:Z0Y2　W:Z0Y6　E:—　R:Z0Y7　F:Z09V　D:Z09W |
| [`H01A`](<%E9%97%AA%E5%85%89.md>) | 闪光 | 闪光（亚丝娜(结城明日奈)） | 敏捷 | ✅ 可选 | Q:Z0YC　W:Z17B　E:Z17E　R:Z0XV　F:Z0IN　D:Z08T |
| [`H01B`](<%E5%8A%A0%E9%80%9F%E4%B8%96%E7%95%8C.md>) | 加速世界 | 加速世界（黑雪姬） | 体力 | ✅ 可选 | Q:Z0DK　W:Z0E7　E:Z0EA　R:Z0E9　F:—　D:Z0DJ |
| [`H01C`](<%E5%8F%8C%E5%8F%B6%E6%9D%8F.md>) | 双叶杏 | 双叶杏（天堂） | 筋力 | ✅ 可选 | Q:Z0BK　W:Z0BH　E:Z0BG　R:Z0GF　F:—　D:Z0BI |
| [`H01D`](<%E4%BA%8C%E7%9A%87.md>) | 二皇 | 二皇（爱丽丝） | 敏捷 | ✅ 可选 | Q:Z0BM　W:Z0BO　E:Z0BL　R:Z0BN　F:—　D:Z0BP |
| [`H01E`](<%E6%B8%85%E6%99%A8.md>) | 清晨 | 清晨（艾基尔） | 筋力 | ✅ 可选 | Q:Z0B7　W:Z0B6　E:—　R:Z0FT　F:Z0IN　D:Z1D9 |
| [`H01F`](<%E5%B0%B1%E7%AE%97%E4%B8%8D%E7%AC%91%E4%B9%9F%E5%BE%88%E5%8F%AF%E7%88%B1.md>) | 就算不笑也很可爱 | 就算不笑也很可爱（筒隐月子） | 敏捷 | ✅ 可选 | Q:Z0BV　W:Z0BW　E:Z0BU　R:Z0BX　F:—　D:Z0BT |
| [`H01G`](<Six.md>) | Six | Six（黄泉） | 筋力 | ✅ 可选 | Q:Z0IX　W:Z0IT　E:Z0IU　R:Z10Z　F:—　D:Z0IS |
| [`H01J`](<%E5%85%AC%E4%BC%9A%20%E5%91%BD%E8%BF%90%E4%B9%8B%E5%A4%9C%28four%20king%29_H01J.md>) | 公会:命运之夜(four\*king) | 公会:命运之夜(four\*king)（玩家:CD） | 敏捷 | ✅ 可选 | Q:Z095　W:Z09S　E:—　R:—　F:—　D:— |
| [`H01K`](<%E5%85%AC%E4%BC%9A%20%E5%91%BD%E8%BF%90%E4%B9%8B%E5%A4%9C%28four%20king%29_H01K.md>) | 公会:命运之夜(four\*king) | 公会:命运之夜(four\*king)（CD） | 体力 | ✅ 可选 | Q:Z095　W:Z096　E:Z097　R:—　F:—　D:Z094 |
| [`H01N`](<%E9%9B%B7%E7%94%B5%C2%B7%E5%BF%98%E5%B7%9D%E5%AE%88%C2%B7%E8%8A%BD%E8%A1%A3_H01N.md>) | 雷电·忘川守·芽衣 | 雷电·忘川守·芽衣（黄泉） | 敏捷 | ✅ 可选 | Q:Z17M　W:Z17N　E:Z17O　R:Z17P　F:—　D:— |
| [`H01O`](<%E9%9B%B7%E7%94%B5%C2%B7%E5%BF%98%E5%B7%9D%E5%AE%88%C2%B7%E8%8A%BD%E8%A1%A3_H01O.md>) | 雷电·忘川守·芽衣 | 雷电·忘川守·芽衣（黄泉）（地图上无此单位） | 敏捷 | ❌ 地图上无此单位 | Q:Z17M　W:Z17N　E:Z17O　R:Z17P　F:—　D:— |
| [`H01P`](<%E7%A9%B9.md>) | 穹 | 穹（冬弥） | 筋力 | ✅ 可选 | Q:Z0P6　W:Z0P7　E:Z0P5　R:Z0D8　F:Z0PA　D:Z0D5 |
| [`H01Q`](<%E8%AF%97%E4%B9%83.md>) | 诗乃 | 诗乃（朝田诗乃） | 筋力 | ✅ 可选 | Q:Z0PL　W:—　E:Z0PM　R:—　F:—　D:— |
| [`H01R`](<AI.md>) | AI | AI（结衣） | 体力 | ✅ 可选 | Q:Z0YA　W:Z0JA　E:Z0JB　R:Z0Y1　F:—　D:Z08V |
| [`H01S`](<%E9%AD%94%E6%B3%95%E6%88%98%E4%BA%89.md>) | 魔法战争 | 魔法战争（相羽六） | 敏捷 | ✅ 可选 | Q:Z0GO　W:Z0GM　E:Z1G6　R:Z0GQ　F:Z0GN　D:— |
| [`H01T`](<%E5%A8%83%E5%A8%83.md>) | 娃娃 | 娃娃（Saber） | 筋力 | ✅ 可选 | Q:Z0OA　W:Z0O9　E:Z0OD　R:Z0OE　F:—　D:Z0O8 |
| [`H01U`](<%E5%85%84%E6%8E%A7%E4%B8%87%E5%B2%81.md>) | 兄控万岁 | 兄控万岁（莉法） | 敏捷 | ✅ 可选 | Q:Z0C5　W:Z0BZ　E:Z0C6　R:Z0C7　F:Z0IN　D:Z0C1 |
| [`H01W`](<%E5%86%AC%E5%BC%A5.md>) | 冬弥 | 冬弥（优库里伍德） | 体力 | ✅ 可选 | Q:Z0EE　W:Z0ED　E:Z0EF　R:Z0EG　F:Z0EC　D:— |
| [`H01X`](<11eyes%E7%BD%AA%E4%B8%8E%E7%BD%9A%E4%B8%8E%E8%B5%8E%E7%9A%84%E5%B0%91%E5%A5%B3.md>) | 11eyes罪与罚与赎的少女 | 11eyes罪与罚与赎的少女（草壁操） | 敏捷 | ✅ 可选 | Q:Z0JK　W:Z0JL　E:Z0JN　R:Z0JP　F:—　D:— |
| [`H01Y`](<%E5%B0%BE%E9%9A%8F%E5%A7%90%E5%A7%90%E7%9A%84%E6%80%AA%E5%A6%B9%E5%AD%90.md>) | 尾随姐姐的怪妹子 | 尾随姐姐的怪妹子（芙兰朵露·斯卡雷特） | 敏捷 | ✅ 可选 | Q:Z0NB　W:Z0FV　E:—　R:—　F:Z0NC　D:Z0N8 |
| [`H01Z`](<%E4%BC%98%E5%BA%93%E9%87%8C%E4%BC%8D%E5%BE%B7.md>) | 优库里伍德 | 优库里伍德（冬弥(泳装形态)） | 敏捷 | ✅ 可选 | Q:Z0EM　W:Z0EQ　E:Z0EO　R:Z0ER　F:—　D:Z0EK |
| [`H020`](<%E7%81%BC%E7%9C%BC%E7%9A%84%E5%A4%8F%E5%A8%9C.md>) | 灼眼的夏娜 | 灼眼的夏娜（夏娜） | 筋力 | ✅ 可选 | Q:Z0ES　W:Z0EW　E:Z0EX　R:Z0EY　F:—　D:Z0EU |
| [`H021`](<%E4%B8%96%E7%95%8C%E6%9C%80%E5%BC%BA%E7%AC%A8%E8%9B%8B.md>) | 世界最强笨蛋 | 世界最强笨蛋（⑨） | 筋力 | ✅ 可选 | Q:Z0JF　W:Z0JH　E:Z0JJ　R:Z0JE　F:—　D:Z0JG |
| [`H025`](<%E7%99%BD%E9%9B%AA%E5%85%AC%E4%B8%BB.md>) | 白雪公主 | 白雪公主（White Trailer） | 体力 | ✅ 可选 | Q:Z0G7　W:Z0G9　E:Z0FZ　R:Z0GD　F:—　D:— |
| [`H027`](<%E9%BB%84%E9%87%91%E8%8B%B9%E6%9E%9C%E4%BC%9A%E9%95%BF.md>) | 黄金苹果会长 | 黄金苹果会长（葛林瑟鲁妲） | 筋力 | ✅ 可选 | Q:Z0B0　W:Z0B1　E:Z0B2　R:Z0B3　F:Z0IN　D:Z0B5 |
| [`H028`](<%E5%A5%A5%E5%88%A9%E7%BB%B4%E4%BA%9A.md>) | 奥利维亚 | 奥利维亚（一皇(one)） | 筋力 | ✅ 可选 | Q:Z0NW　W:Z0NX　E:Z0NV　R:Z0NZ　F:—　D:Z0NY |
| [`H02A`](<%E5%88%80%E4%BB%95%E8%A5%A7%E5%AE%9C.md>) | 刀仕襧宜 | 刀仕襧宜（朱雀院椿） | 筋力 | ✅ 可选 | Q:Z0H8　W:Z0IJ　E:Z097　R:Z0NR　F:—　D:— |
| [`H040`](<%E6%95%B0%E5%AD%97%E5%90%9B.md>) | 数字君 | 数字君（458356800） | 敏捷 | ✅ 可选 | Q:Z0YR　W:Z0YS　E:Z0YT　R:Z0YW　F:Z0YQ　D:Z0YP |
| [`N023`](<%E7%BB%AF%E9%9B%AA.md>) | 绯雪 | 绯雪（「永世灼樱巫女」） | 敏捷 | ✅ 可选 | Q:Z1US　W:Z1UT　E:Z1UU　R:Z1UV　F:Z1V0　D:Z1UR |
| [`Nsjs`](<%E6%97%B6%E5%B4%8E%E7%8B%82%E4%B8%89.md>) | 时崎狂三 | 时崎狂三 | 未设置 | ⚠️ 名单备注与注册表不一致 | Q:A0OJ　W:A0OK　E:A0QV　R:A0ON　F:—　D:A0OI |



---

<div class="wiki-source-note" markdown="1">

**数据来源**：`刀剑物语 happy丶FISH v1.0 正式版`（母图 SHA256 `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D`）

本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。哪些内容已被交叉验证、有哪些已知限制，见 [地图身份](../info/地图身份.md)；本页符号（`—` / `未判定（证据不足）` / `⚠️ 不可选`）的含义见 [术语与用语](../info/术语与用语.md)。

</div>
