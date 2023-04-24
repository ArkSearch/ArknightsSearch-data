
> 开发时的笔记

**story table 中部分id首字母大写，与实际文件路径不同**

## Trigger Type

| key                         | 解释                                  |
|-----------------------------|-------------------------------------|
| BEFORE_BATTLE               | 战斗前                                 |
| AFTER_BATTLE                | 战斗后                                 |
| ACTIVITY_LOADED             | 进入活动播放                              |
| PAGE_LOADED                 | 进入某一页面                              |
| STORY_FINISH_OR_PAGE_LOADED | 活动结束/进入某一页面(解锁关卡?)                  |
| CRISIS_SEASON_LOADED        | 危机合约上限(唯一) ~~再见了最后的危机合约~~           |
| CUSTOM_OPERATION            | 客户端主动点击                             |
| GAME_START                  | 进入游戏(唯二)(后台重进也算)                    |
| ACTIVITY_ANNOUNCE           | 活动公告，运作模式类似`GAME_START`，目前仅发现于愚人节活动 |

## obt 文件夹注解

| dir           | 解释           | 不解析原因      |
|---------------|--------------|------------|
| main          | 主线剧情         |            |
| memory        | 干员密录         |            |
| rogue         | 肉鸽月度剧情       |            |
| ~~record~~    | 10/11章note   | 无名称        |
| ~~roguelike~~ | 肉鸽剧情         | 无名称/不可再次触发 |
| ~~guide~~     | 游戏内引导(基建/专精) | 无名称/不可再次触发 |
| ~~legion~~    | 保全派驻         | 无名称/不可再次触发 |
| ~~rune~~      | 危机合约         | 无名称/不可再次触发 |
| ~~tutorial~~  | 教学关          | 懒          |

~~不解析的内容有人用了再解析~~

## obt/main 类型注解

| type                       | 解释              |
|----------------------------|-----------------|
| level_main                 | 一般主线剧情          |
| level_st                   | 纯剧情关卡           |
| level_spst                 | 第八章隐藏剧情         |
| level_main_9_chapter_recap | 剧情回顾            |
| zone_enter                 | "观看序曲" (章节进入剧情) |

**生稀盐酸部分剧情暂不解析**

## activities 类型注释

| type            | 解释                    |
|-----------------|-----------------------|
| *beg/end        | 行动前/行动后               | 
| st*             | 剧情关                   |
| guide/training* | 教程                    |
| tutorial*       | 关卡内剧情                 |
| ui*cc           | 目前仅在act5d1(危机合约)发现此类型 |