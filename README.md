# modeflip

REST API

- 返回所有设计师：/designers
- 返回一个设计师，根据设计师ID（did）：/designers/1
- 返回设计师目前点赞数量：/designers/1/likes
- 给设计师点赞（+1）：/designers/1/do_like
- 返回设计师目前的关注数量：/designers/1/subscribes
- 给设计师关注（+1）：/designers/1/do_subscribe
- 返回设计师所有作品集，根据设计师ID（did）：/designers/1/collections
- 返回设计师的一个作品集，根据作品集ID（cid）: /designers/1/collections/1
- 返回一个作品集里的所有服装：/designers/1/collections/1/garments
- 返回一个作品集里的一套服装，根据服装ID（gid）：/designers/1/collections/1/garments/1
