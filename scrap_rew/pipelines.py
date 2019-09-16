import pymysql
import time

class RewhousePipeline(object):

    def process_item(self, item, spider):

        db = pymysql.connect(host='localhost', user='root', password='qijingjing8081', database='rew')
        cursor = db.cursor()
        #cursor.execute('create table house_info (price varchar(100), addr varchar(200), link varchar(200))')

        for i in range(0, len(item['addr'])):
            price = item['price'][i]
            addr = item['addr'][i]
            link = item['link'][i]
            try:
                sql = 'insert into house_info(price, addr, link) values("'+price+'", "'+addr+'", "'+link+'")'
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
            time.sleep(5)

        db.close()
        return item
