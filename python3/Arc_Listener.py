import os
import json
import re
import falcon
import mimetypes
import sys
import MySQLdb
import datetime
from wsgiref import simple_server


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
        file = open("temp.txt", "a")
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

        sql = "select stateId from videos where upc = '%s' and isrc = '%s'" % (
            upc,
            unique_key,
        )
        cursor.execute(sql)

        video = cursor.fetchall()

        stateid = ""

        print(("Row count :" + str(cursor.rowcount)))
        for row in video:
            print("here --> %s" % row[0])
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
                # import pdb; pdb.set_trace()
                if status == "success":

                    cursor.execute(
                        "UPDATE videos SET arcId = '%s', isrcDistPolicy = '%s', receiptDateArc ='%s' WHERE upc = '%s' AND isrc = '%s' AND stateId >= 30"
                        % (musicvideo_uuid, isrc_dp_uuid, timestamp, upc, unique_key)
                    )
                    db.commit()
                    strCommit = "Data committed to DB successfully \n"
                    file.write(strCommit)
                else:
                    cursor.execute(
                        "UPDATE videos SET errorStatusArc = '%s', receiptDateArc ='%s' WHERE upc = '%s' AND isrc = '%s' AND stateId >= 30"
                        % (error_spec, timestamp, upc, unique_key)
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


app = falcon.API()
app.add_route("/MVI/report", Uploads())
if __name__ == "__main__":

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

    app.add_sink(static)

    host = "166.77.182.110"  # Change appropriately
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s:%s" % (host, port))
    httpd.serve_forever()
