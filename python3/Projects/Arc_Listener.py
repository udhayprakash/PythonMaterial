import datetime
import json
import mimetypes
import os
import re
from wsgiref import simple_server

import falcon
import MySQLdb


class Uploads:
    def on_post(self, req, res):
        request_body = json.loads(req.stream.read())
        report = request_body["report"]
        # This will confirm if it is an ISRC or ISRC_label
        unique_key = report["unique_key"]
        isrc_pattern = "^[A-Z]{2,}\w*\d{6,}\_\d{1,2}$"
        musicvideo_pattern = "^[A-Z]{2,}\w*\d{6,}$"

        if re.search(isrc_pattern, unique_key):
            self.video_report(report)
        elif re.search(musicvideo_pattern, unique_key):
            self.asset_report(report)

    def video_report(self, report_json):
        file = open("temp.txt", "a", encoding="utf_8")
        strEnterVideo = "Entering video_report function \n"
        file.write(strEnterVideo)

        unique_key = report_json["unique_key"].split("_")[0]
        print(unique_key)
        status = report_json["asset_status"]
        upc = report_json["upc"]
        musicvideo_uuid = report_json["musicvideouuid"]
        isrc_dp_uuid = report_json["isrcdpuuid"]
        folder = report_json["timestamp"]
        error_spec = report_json["error_spec"]

        strDataCapture = "Captured Data for video: " + upc + " and " + unique_key + "\n"
        file.write(strDataCapture)
        # Database connection
        db = MySQLdb.connect("localhost", "pyuser", "unicornbacon", "mvi_live")
        db.autocommit(False)

        cursor = db.cursor()

        sql = (
            f"select stateId from videos where upc = '{upc}' and isrc = '{unique_key}'"
        )
        cursor.execute(sql)

        video = cursor.fetchall()

        stateid = ""

        print(("Row count :" + str(cursor.rowcount)))
        for row in video:
            print(f"here --> {row[0]}")
            stateid = row[0]
            if stateid < 30:
                strStateLess = "Video record exists where stateId is less than 30 \n"
                file.write(strStateLess)

        # while video is not None:
        # print(video)
        # video = cursor.fetchone()
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        if video is None:
            strVidNone = "Video record does not exist in DB \n"
            file.write(strVidNone)
        else:
            try:
                strRecExist = "Video record exists in DB \n"
                file.write(strRecExist)
                if status == "success":
                    cursor.execute(
                        f"""UPDATE videos
                            SET arcId = '{musicvideo_uuid}',
                                isrcDistPolicy = '{isrc_dp_uuid}',
                                receiptDateArc ='{timestamp}'
                            WHERE upc = '{upc}' AND isrc = '{unique_key}' AND stateId >= 30"""
                    )
                    db.commit()
                    strCommit = "Data committed to DB successfully \n"
                    file.write(strCommit)
                else:
                    cursor.execute(
                        f"""UPDATE videos
                            SET errorStatusArc = '{error_spec}',
                            receiptDateArc ='{timestamp}'
                            WHERE upc = '{upc}' AND isrc = '{unique_key}' AND stateId >= 30"""
                    )
                    db.commit()
                    strUnCom = "Response returned with error status \n"
                    file.write(strUnCom)
            except MySQLdb.Error as e:
                db.rollback()
                # e = sys.exc_info()[0]
                file.write("Error encountered : \n")
                file.write("%s" % e)
                file.write("\n")
            finally:
                db.close()
                strProcComplete = "Process Complete !\n\n"
                file.write(strProcComplete)
                file.close()

    def asset_report(self, report):
        strAsset = "Asset data received -> Skipped"
        file.write(strAsset)


def static(req, res, static_dir="static", index_file="index.html"):
    path = static_dir + req.path
    if req.path == "/":
        path += index_file
    if os.path.isfile(path):
        res.content_type = mimetypes.guess_type(path)[0]
        res.status = falcon.HTTP_200
        res.stream = open(path)
    else:
        res.status = falcon.HTTP_404


if __name__ == "__main__":
    app = falcon.API()
    app.add_route("/MVI/report", Uploads())
    app.add_sink(static)

    host = "127.0.0.1"  # Change appropriately
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s:%s" % (host, port))
    httpd.serve_forever()
