import gin

from backup import Backup

if __name__ == '__main__':
    gin.parse_config_file('config.gin', True)

    Backup().backup()
