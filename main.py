import os
import traceback
import time
import mytime
import fgourl
from user import user

userIds = os.environ['GAME_USERIDS'].split(',')
authKeys = os.environ['GAME_AUTHKEYS'].split(',')
secretKeys = os.environ['GAME_SECRETKEYS'].split(',')

userNums = len(userIds)
authKeyNums = len(authKeys)
secretKeyNums = len(secretKeys)

fgourl.ver_code_ = os.environ['GAME_VERCODE']
fgourl.TelegramBotToken = os.environ['TELEGRAM_BOT_TOKEN']
fgourl.TelegramAdminId = os.environ['TELEGRAM_ADMIN_ID']
fgourl.github_token_ = os.environ['VERY_IMPORTANT_TOKEN']
fgourl.github_name_ = os.environ['VERY_IMPORTANT_NAME']
UA = os.environ['GAME_USERAGENT']
if UA != 'nullvalue':
    fgourl.user_agent_ = UA


def main():
    fgourl.SendMessageToAdmin(f'铛铛铛 *{mytime.GetNowTimeHour()}点* 了')
    if userNums == authKeyNums and userNums == secretKeyNums:
        fgourl.ReadConf()
        fgourl.gameData()
        print(f'待签到: {userNums}个')
        res = '【登录信息】\n'
        for i in range(userNums):
            try:
                instance = user(userIds[i], authKeys[i], secretKeys[i])
                time.sleep(3)
                res += instance.topLogin()
                time.sleep(2)
                instance.topHome()
                time.sleep(2)
            except Exception as ex:
                print(f'{i}th user login failed: {ex}')
                traceback.print_exc()

        fgourl.UploadFileToRepo(mytime.GetNowTimeFileName(), res, mytime.GetNowTimeFileName())
        fgourl.SendMessageToAdmin(res)
    else:
        print('账号密码数量不匹配')


if __name__ == '__main__':
    main()
