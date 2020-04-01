import redis

class RedisService:
    def test(self):
        print(f'here we are!')
        return 'testing!'

    def __init__(self, rHost, rPort):
        self.r = redis.StrictRedis(rHost, rPort, charset="utf-8", decode_responses=True)

    def get_info(self):
        info = self.r.info()
        return info

    def streams_produce(self, stream_name, data):
        res = self.r.xadd(stream_name, data, id='*')
        return res

    def streams_new_consumer_group(self, stream_name, group_name):
        try:
            res = self.r.xgroup_create(stream_name, group_name, id='$')
            return True
        except: 
            print(f'error creating group {group_name}. it likely already exists')
            return False

    def streams_consume(self, streams_list):
        # wait indefinitely for next update
        res = self.r.xread(streams_list, block=0)
        return res

    def streams_group_consume(self, group_name, consumer_name, streams_list):
        # wait indefinitely for next update
        res = self.r.xreadgroup(group_name, consumer_name, streams_list, block=0)
        return res