# modeflip

REST API

- (GET)返回所有设计师：/designers
- (GET)返回一个设计师，根据设计师ID（did）：/designers/1
- (GET)返回设计师目前点赞数量：/designers/1/likes
- (PUT)给设计师点赞（+1）：/designers/1/do_like
- (GET)返回设计师目前的关注数量：/designers/1/subscribes
- (PUT)给设计师关注（+1）：/designers/1/do_subscribe
- (GET)返回设计师所有作品集，根据设计师ID（did）：/designers/1/collections
- (GET)返回设计师的一个作品集，根据作品集ID（cid）: /designers/1/collections/1
- (GET)返回一个作品集里的所有服装：/designers/1/collections/1/garments
- (GET)返回一个作品集里的一套服装，根据服装ID（gid）：/designers/1/collections/1/garments/1
