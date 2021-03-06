import os
"""
SQLALCHEMY_DATABASE_URI	
用于连接数据的数据库。例如：
sqlite:////tmp/test.db
mysql://username:password@server/db
SQLALCHEMY_BINDS	一个映射绑定 (bind) 键到 SQLAlchemy 连接 URIs 的字典。 更多的信息请参阅 绑定多个数据库。
SQLALCHEMY_ECHO	如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_RECORD_QUERIES	可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。更多信息请参阅 get_debug_queries()。
SQLALCHEMY_NATIVE_UNICODE	可以用于显式地禁用支持原生的 unicode。这是 某些数据库适配器必须的（像在 Ubuntu 某些版本上的 PostgreSQL），当使用不合适的指定无编码的数据库 默认值时。
SQLALCHEMY_POOL_SIZE	数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
SQLALCHEMY_POOL_TIMEOUT	指定数据库连接池的超时时间。默认是 10。
SQLALCHEMY_POOL_RECYCLE	自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
SQLALCHEMY_MAX_OVERFLOW	控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
SQLALCHEMY_TRACK_MODIFICATIONS	如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
"""
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///'+os.path.join(
    '/mnt/d/work/学习/python/WebLearning/Flask/chapter_5', 'data.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False