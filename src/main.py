from authorization import Authorization
from backup import Backup

import gin

if __name__ == '__main__':
    gin.parse_config_file('../config.gin', True)

    Authorization().authorize()
    Backup().save()
