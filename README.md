# happy丶FISH Wiki

《刀剑物语 happy丶FISH v1.0 正式版》的数据图鉴站点。站点格式参考并复刻自开源项目 [crt106/sao-wiki](https://github.com/crt106/sao-wiki)，**内容数据全部来自本图自己的成员**，不是参考仓库的数据。

## 数据来源（身份优先于文件名）

| 项 | 值 |
|---|---|
| 母图 | `Maps\Custom Maps\刀剑物语 happy丶FISH v1.0 正式版.w3x` |
| 字节数 | 223,227,915 |
| SHA256 | `62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D` |
| `war3map.j` | 4,465,891 B · `13bafcf0c1e91848fbf8ee72cbc48017e711cae7b6198e69cb01136c7064a4a2` |
| `war3map.w3u` | 1,801,123 B · `e8612c55afc5219e30c45c19dcff26b63cd8966a94d740853c5ef39085804294` |
| `war3map.w3a` | 1,427,367 B · `80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3` |
| `war3map.w3t` | 399,046 B · `98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d` |

数值来源分层（**不要把不同层混为一谈**）：

1. **对象数据真值**：`war3map.w3u`（单位）/ `war3map.w3a`（技能）/ `war3map.w3t`（物品）的字段值。本站的表格数值来自这里。
2. **触发器真值**：`war3map.j`（JASS，112,226 行）。伤害公式、合成、掉落、专属、技能实际效果以这里为准；页面里凡引用触发器的地方都带行号。
3. **游戏内文字**：对象数据的 `Ubertip` / `Tip` / `Description`。**这是策划手写文本，可能与实际效果不一致**，站点原样保留并单列，不做"以它为准"的推断。
4. **客户端字段字典**：字段中文名来自用户本机 1.27a 客户端 `War3Patch.mpq` 的 `UnitMetaData.slk` / `AbilityMetaData.slk` + `UI\WorldEditStrings.txt`。

## 目录结构

```
mkdocs.yml            MkDocs 配置（导航靠各目录 .pages，不写 nav:）
docs/                 站点内容（生成产物也在这里，交付即页面）
  index.md            首页
  heroes/             英雄图鉴（一英雄一页）
  items/<类别>/        物品图鉴（一物品一页，文件名 <ID>_<名称>.md）
  skills/             技能索引
  info/               资料（数据来源与方法、存档、崩溃、楼层）
  changelogs/         版本更新日志（MkDocs Blog）
  stylesheets/        样式
hooks/                MkDocs hook（jieba 中文分词搜索）
overrides/            主题模板覆盖（页脚注入地图版本）
scripts/              生成器：从地图数据生成 docs/ 下的页面
.github/workflows/    GitHub Pages 部署
```

## 本地构建

```powershell
# 本仓库自带虚拟环境（.venv 不入库）
.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8000
# 快模式（跳过两个 Git 元数据插件，1000+ 页明显更快）
$env:MKDOCS_ENABLE_GIT_META="false"; $env:WATCHFILES_FORCE_POLLING="true"
.\.venv\Scripts\python.exe -m mkdocs serve --dirtyreload -a 127.0.0.1:8000
```

## 生成器

页面不是手写的，是从地图成员重新生成的：

```powershell
python scripts\build_items.py     # 物品页 551 个
python scripts\build_heroes.py    # 英雄页 58 个
python scripts\build_skills.py    # 技能索引
python scripts\build_info.py      # 首页与资料页
```

生成器读的是 `note_log\` 下的解析产物（`wiki_data\*.json`、`index\*.tsv`、`recon\*.tsv`）。

## 站点声明

- 本站**只读展示**，不含任何游戏内修改功能，也不含地图/模型/贴图资源。
- 站点所有数值**未经过实机验证**。区分清楚：数据来自哪个成员（已核对 SHA256） ≠ 游戏里跑出来就是这样。
- 发现与游戏实际不符，请以游戏为准，并记录来源成员与行号后再改本站。
