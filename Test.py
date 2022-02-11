import speedtest
import time
import pandas as pd
from datetime import datetime
Test_Date = []
Test_Server = []
Test_Server_Location = []
Test_Server_Latency = []
Ping_Result = []
Download_Speed = []
Upload_Speed = []
Current_Tests_Number = 0
while (Current_Tests_Number <= 5):
    test_connection = speedtest.Speedtest()
    best_server = test_connection.get_best_server()
    Test_Server.append(best_server['host'])
    Test_Server_Location.append(best_server['country'])
    Test_Server_Latency.append(best_server['latency'])
    Test_Date_And_Time = datetime.now()
    Test_Date.append(Test_Date_And_Time)
    download_result = test_connection.download()
    download_result = download_result / 1024 / 1024
    download_result = "{:.2f}".format(download_result)
    Download_Speed.append(download_result)
    upload_result = test_connection.upload()
    upload_result = upload_result / 1024 / 1024
    upload_result = "{:.2f}".format(upload_result)
    Upload_Speed.append(upload_result)
    ping_result = test_connection.results.ping
    Ping_Result.append(ping_result)
    print(f"{download_result} Mbit/s")
    print(f"{upload_result} Mbit/s")
    print(f"{ping_result} ms")
    Current_Tests_Number += 1
    print(f"On A Déja Effectuer {Current_Tests_Number} Test ")
    print(f"Last Test Was Performed On {Test_Date_And_Time}")
    time.sleep(180)
dict = {"Test Date": Test_Date , "Test Host" : Test_Server , "Test Server Country" : Test_Server_Location,
        "Test Server Latency" : Test_Server_Latency , "Ping (ms)" : Ping_Result ,
        "Download (mbit/s)" : Download_Speed,"Upload(mbit/s)":Upload_Speed}
Result_dataframe = pd.DataFrame(dict)
Result_dataframe.to_csv('Test Resulttt.csv')
