# modeflip

REST API:

# 设计师操作
- (GET)返回所有设计师：/designers
- (GET)返回一个设计师，根据设计师ID（did）：/designers/1
- (POST)创建设计师：/designers
  JSON:
    did = Integer （必须为新did，不能已存在）
    name = String
    origin = String
    icon_link = String （要求完整链接，包括http://****.com）（阿里云OSS对象链接，测试可随意）
    is_active = Bool
    bio = String
    music_collection = List（阿里云OSS对象链接）

- (PUT)更新设计师信息，根据设计师ID（did）：/designers/1
  JSON：同上
- (DELETE)删除设计师信息，根据设计师ID（did）：/designers/1



# 作品集操作
- (GET)返回设计师所有作品集，根据设计师ID（did）：/designers/1/collections
- (GET)返回设计师的一个作品集，根据作品集ID（cid）: /designers/1/collections/1
- (POST)创建新作品集：/designers/1/collections
  JSON:
    cid = Integer  （必须为新cid，不能已存在）
    did = Integer （必须提供，不限制，但是应该是已经存在的did）
    name = String
    released = DateTime  (utc timestamp的int或者float，比如：2016年5月1日0点0分，utc timestamp int为1462060800)
    signatrue_pics = List （阿里云OSS对象链接）
    signatrue_musics = List（阿里云OSS对象链接）
    signatrue_videos = List（阿里云OSS对象链接）

- (PUT)更新作品集信息，根据设计师ID（did）以及作品集ID（cid）：/designers/1/collections/1
  JSON：同上
- (DELETE)删除设计师信息，根据设计师ID（did）以及作品集ID（cid）：/designers/1/collections/1



# 服装操作
- (GET)返回一个作品集里的所有服装：/designers/1/collections/1/garments
- (GET)返回一个作品集里的一套服装，根据服装ID（gid）：/designers/1/collections/1/garments/1
- (POST)创建新服装：/designers/1/collections/1/garments
  JSON:
    gid = Integer （必须为新gid，不能已存在）
    cid = Integer （必须提供，不限制，但是应该是已经存在的cid）
    did = Integer （必须提供，不限制，但是应该是已经存在的did）
    price = Float
    description = String
    shop_link = String （必须为完整链接，包括http://****.com）（有赞商城商品链接）
    pictures = List（阿里云OSS对象链接）

- (PUT)更新服装信息，根据设计师ID（did），作品集ID（cid）以及服装ID（gid）：/designers/1/collections/1/garments/1
  JSON：同上
- (DELETE)删除服装信息，根据设计师ID（did），作品集ID（cid）以及服装ID（gid）：/designers/1/collections/1/garments/1



其他API:
- (GET)返回设计师目前点赞数量：/designers/1/likes
- (PUT)给设计师点赞（+1）：/designers/1/do_like
- (GET)返回设计师目前的关注数量：/designers/1/subscribes
- (PUT)给设计师关注（+1）：/designers/1/do_subscribe
