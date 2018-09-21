from authorization import Authorization
import gin

if __name__ == '__main__':
    gin.parse_config_file('../config.gin', True)

    authorization = Authorization()
    authorization.authorize()
