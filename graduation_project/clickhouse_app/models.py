from django_clickhouse.clickhouse_models import ClickHouseModel
from django_clickhouse import engines
from infi.clickhouse_orm import fields

class Common(ClickHouseModel):
    stat_index = fields.UInt64Field()
    come_to_server_time = fields.StringField()
    slmVersion = fields.StringField()
    slmMode()