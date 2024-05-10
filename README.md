# Local_MongoDB

## Description 
This will have the class to interact with MongoDB, it can be used to push csv files to mongoDB or preform other functions on a database

## Setup
- service name - MongoDB
- version - 7.0.9

## DB
- URI -> "mongodb://localhost:27017/"
When sending queries you can filter for greater than and less than with the following syntax
- All example below use the FB_Assets table
```
result = Client.query([{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}, {"Date": {"$lt":"2024-05-10"}}], "FB_Assets")
```
- [{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}] This query would find all ATOM's with a USDValue greater than 1000000
```
                         _id  Coin Contract        QTY    USDValue    Exchange Account  Unnamed: 6   Time        Date
0   663e187a99e266a47e259b19  ATOM     ATOM  195470.78  1752004.57  FireBlocks    SPOT         NaN  17-00  2024-05-09
1   663e22c9e60ff32ccc0d72c8  ATOM     ATOM  195470.78  1752004.57  FireBlocks    SPOT         NaN  17-00  2024-05-09
2   663e22cbe60ff32ccc0d7665  ATOM     ATOM  195474.77  1747348.97  FireBlocks    SPOT         NaN  18-00  2024-05-09
3   663e22cce60ff32ccc0d79fc  ATOM     ATOM  195478.20  1758326.45  FireBlocks    SPOT         NaN  19-00  2024-05-09
4   663e22cee60ff32ccc0d7d91  ATOM     ATOM  195481.62  1779664.64  FireBlocks    SPOT         NaN  20-00  2024-05-09
5   663e22cfe60ff32ccc0d8128  ATOM     ATOM  195485.05  1767575.84  FireBlocks    SPOT         NaN  21-00  2024-05-09
6   663e22d1e60ff32ccc0d84c0  ATOM     ATOM  195488.49  1762719.68  FireBlocks    SPOT         NaN  22-00  2024-05-09
7   663e22d2e60ff32ccc0d8858  ATOM     ATOM  195491.91  1767246.88  FireBlocks    SPOT         NaN  23-00  2024-05-09
8   663e22d4e60ff32ccc0d8bf1  ATOM     ATOM  195495.34  1785459.02  FireBlocks    SPOT         NaN  00-00  2024-05-10
9   663e22d5e60ff32ccc0d8f89  ATOM     ATOM  195498.79  1783926.48  FireBlocks    SPOT         NaN  01-00  2024-05-10
10  663e22d6e60ff32ccc0d9321  ATOM     ATOM  195500.50  1781987.04  FireBlocks    SPOT         NaN  02-00  2024-05-10
11  663e22d8e60ff32ccc0d96d2  ATOM     ATOM  195503.93  1782800.38  FireBlocks    SPOT         NaN  03-00  2024-05-10
12  663e22d9e60ff32ccc0d9a83  ATOM     ATOM  195507.37  1774424.85  FireBlocks    SPOT         NaN  04-00  2024-05-10
13  663e22dbe60ff32ccc0d9e34  ATOM     ATOM  195510.80  1776802.12  FireBlocks    SPOT         NaN  05-00  2024-05-10
14  663e22dce60ff32ccc0da1e5  ATOM     ATOM  195514.23  1778984.02  FireBlocks    SPOT         NaN  06-00  2024-05-10
15  663e22dee60ff32ccc0da595  ATOM     ATOM  195517.64  1773149.46  FireBlocks    SPOT         NaN  07-00  2024-05-10
16  663e22dfe60ff32ccc0da945  ATOM     ATOM  195524.47  1786702.60  FireBlocks    SPOT         NaN  09-00  2024-05-10
17  663e22e1e60ff32ccc0dacf5  ATOM     ATOM  195527.92  1785169.93  FireBlocks    SPOT         NaN  10-00  2024-05-10
18  663e22e2e60ff32ccc0db094  ATOM     ATOM  195531.36  1784419.21  FireBlocks    SPOT         NaN  11-00  2024-05-10
19  663e22e3e60ff32ccc0db433  ATOM     ATOM  195534.19  1780925.42  FireBlocks    SPOT         NaN  12-00  2024-05-10
20  663e22e5e60ff32ccc0db7d2  ATOM     ATOM  195537.63  1772548.63  FireBlocks    SPOT         NaN  13-00  2024-05-10
21  663e22e6e60ff32ccc0dbb71  ATOM     ATOM  195541.03  1779032.25  FireBlocks    SPOT         NaN  14-00  2024-05-10
```
- [{"Coin":"ATOM"}, {"USDValue": {"$lt": 1000000}}] This query would find all ATOM's with a USDValue lower than 1000000
```
                         _id  Coin Contract   QTY  USDValue         Exchange Account  Unnamed: 6   Time        Date
0   663e187a99e266a47e259b1a  ATOM     ATOM  0.75      6.73  FireBlocks_Cold    SPOT         NaN  17-00  2024-05-09
1   663e22c9e60ff32ccc0d72c9  ATOM     ATOM  0.75      6.73  FireBlocks_Cold    SPOT         NaN  17-00  2024-05-09
2   663e22cbe60ff32ccc0d7666  ATOM     ATOM  0.75      6.71  FireBlocks_Cold    SPOT         NaN  18-00  2024-05-09
3   663e22cce60ff32ccc0d79fd  ATOM     ATOM  0.75      6.75  FireBlocks_Cold    SPOT         NaN  19-00  2024-05-09
4   663e22cee60ff32ccc0d7d92  ATOM     ATOM  0.75      6.83  FireBlocks_Cold    SPOT         NaN  20-00  2024-05-09
5   663e22cfe60ff32ccc0d8129  ATOM     ATOM  0.75      6.78  FireBlocks_Cold    SPOT         NaN  21-00  2024-05-09
6   663e22d1e60ff32ccc0d84c1  ATOM     ATOM  0.75      6.76  FireBlocks_Cold    SPOT         NaN  22-00  2024-05-09
7   663e22d2e60ff32ccc0d8859  ATOM     ATOM  0.75      6.78  FireBlocks_Cold    SPOT         NaN  23-00  2024-05-09
8   663e22d4e60ff32ccc0d8bf2  ATOM     ATOM  0.75      6.85  FireBlocks_Cold    SPOT         NaN  00-00  2024-05-10
9   663e22d5e60ff32ccc0d8f8a  ATOM     ATOM  0.75      6.84  FireBlocks_Cold    SPOT         NaN  01-00  2024-05-10
10  663e22d6e60ff32ccc0d9322  ATOM     ATOM  0.75      6.84  FireBlocks_Cold    SPOT         NaN  02-00  2024-05-10
11  663e22d8e60ff32ccc0d96d3  ATOM     ATOM  0.75      6.84  FireBlocks_Cold    SPOT         NaN  03-00  2024-05-10
12  663e22d9e60ff32ccc0d9a84  ATOM     ATOM  0.75      6.81  FireBlocks_Cold    SPOT         NaN  04-00  2024-05-10
13  663e22dbe60ff32ccc0d9e35  ATOM     ATOM  0.75      6.82  FireBlocks_Cold    SPOT         NaN  05-00  2024-05-10
14  663e22dce60ff32ccc0da1e6  ATOM     ATOM  0.75      6.83  FireBlocks_Cold    SPOT         NaN  06-00  2024-05-10
15  663e22dee60ff32ccc0da596  ATOM     ATOM  0.75      6.81  FireBlocks_Cold    SPOT         NaN  07-00  2024-05-10
16  663e22dfe60ff32ccc0da946  ATOM     ATOM  0.75      6.86  FireBlocks_Cold    SPOT         NaN  09-00  2024-05-10
17  663e22e1e60ff32ccc0dacf6  ATOM     ATOM  0.75      6.85  FireBlocks_Cold    SPOT         NaN  10-00  2024-05-10
18  663e22e2e60ff32ccc0db095  ATOM     ATOM  0.75      6.85  FireBlocks_Cold    SPOT         NaN  11-00  2024-05-10
19  663e22e3e60ff32ccc0db434  ATOM     ATOM  0.75      6.83  FireBlocks_Cold    SPOT         NaN  12-00  2024-05-10
20  663e22e5e60ff32ccc0db7d3  ATOM     ATOM  0.75      6.80  FireBlocks_Cold    SPOT         NaN  13-00  2024-05-10
21  663e22e6e60ff32ccc0dbb72  ATOM     ATOM  0.75      6.82  FireBlocks_Cold    SPOT         NaN  14-00  2024-05-10
```
- [{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}, {"Time": {"$gt":"18-00"}}] This query would do the same as the first but only with times after 6pm
```
                        _id  Coin Contract        QTY    USDValue    Exchange Account  Unnamed: 6   Time        Date
0  663e22cce60ff32ccc0d79fc  ATOM     ATOM  195478.20  1758326.45  FireBlocks    SPOT         NaN  19-00  2024-05-09
1  663e22cee60ff32ccc0d7d91  ATOM     ATOM  195481.62  1779664.64  FireBlocks    SPOT         NaN  20-00  2024-05-09
2  663e22cfe60ff32ccc0d8128  ATOM     ATOM  195485.05  1767575.84  FireBlocks    SPOT         NaN  21-00  2024-05-09
3  663e22d1e60ff32ccc0d84c0  ATOM     ATOM  195488.49  1762719.68  FireBlocks    SPOT         NaN  22-00  2024-05-09
4  663e22d2e60ff32ccc0d8858  ATOM     ATOM  195491.91  1767246.88  FireBlocks    SPOT         NaN  23-00  2024-05-09
```
- [{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}, {"Date": {"$lt":"2024-05-10"}}]
```
                        _id  Coin Contract        QTY    USDValue    Exchange Account  Unnamed: 6   Time        Date
0  663e187a99e266a47e259b19  ATOM     ATOM  195470.78  1752004.57  FireBlocks    SPOT         NaN  17-00  2024-05-09
1  663e22c9e60ff32ccc0d72c8  ATOM     ATOM  195470.78  1752004.57  FireBlocks    SPOT         NaN  17-00  2024-05-09
2  663e22cbe60ff32ccc0d7665  ATOM     ATOM  195474.77  1747348.97  FireBlocks    SPOT         NaN  18-00  2024-05-09
3  663e22cce60ff32ccc0d79fc  ATOM     ATOM  195478.20  1758326.45  FireBlocks    SPOT         NaN  19-00  2024-05-09
4  663e22cee60ff32ccc0d7d91  ATOM     ATOM  195481.62  1779664.64  FireBlocks    SPOT         NaN  20-00  2024-05-09
5  663e22cfe60ff32ccc0d8128  ATOM     ATOM  195485.05  1767575.84  FireBlocks    SPOT         NaN  21-00  2024-05-09
6  663e22d1e60ff32ccc0d84c0  ATOM     ATOM  195488.49  1762719.68  FireBlocks    SPOT         NaN  22-00  2024-05-09
7  663e22d2e60ff32ccc0d8858  ATOM     ATOM  195491.91  1767246.88  FireBlocks    SPOT         NaN  23-00  2024-05-09
```
- [{"Date": "2024-05-10"}, {"Time": "12-00"}, {"Exchange": {"$ne": "Totals"}}] This query will exlude a specific value
```
                         _id         Exchange     USDT-M        SPOT  MARGIN        EARN     COIN-M       Total  Unnamed: 7   Time        Date
0   663e22e3e60ff32ccc0db3fb        Banks/adj       0.00    68374.36     0.0  -693017.60       0.00  -624643.24         NaN  12-00  2024-05-10
1   663e22e3e60ff32ccc0db3fc          Binance  322982.60   147131.71     0.0        0.01  308282.79   778397.12         NaN  12-00  2024-05-10
2   663e22e3e60ff32ccc0db3fd       Binance_HR       0.00        0.11     0.0        0.00       0.00        0.11         NaN  12-00  2024-05-10
3   663e22e3e60ff32ccc0db3fe     Binance_Sub1       0.00        0.00     0.0        0.00   67419.60    67419.60         NaN  12-00  2024-05-10
4   663e22e3e60ff32ccc0db3ff     Binance_Sub2       0.00        0.00     0.0        0.00   68616.06    68616.06         NaN  12-00  2024-05-10
5   663e22e3e60ff32ccc0db400     Binance_Sub3       0.00        0.00     0.0        0.00   20822.33    20822.33         NaN  12-00  2024-05-10
6   663e22e3e60ff32ccc0db401     Binance_Sub4   67840.45        0.11     0.0        0.00       0.00    67840.56         NaN  12-00  2024-05-10
7   663e22e3e60ff32ccc0db402            Bybit  209054.60        0.00     0.0        0.00       0.00   209054.60         NaN  12-00  2024-05-10
8   663e22e3e60ff32ccc0db403         Bybit_HR   43583.46        0.00     0.0        0.00       0.00    43583.46         NaN  12-00  2024-05-10
9   663e22e3e60ff32ccc0db404       Bybit_Sub1  215601.96        0.00     0.0        0.00       0.00   215601.96         NaN  12-00  2024-05-10
10  663e22e3e60ff32ccc0db405       FireBlocks       0.00  4993016.54     0.0        0.00       0.00  4993016.54         NaN  12-00  2024-05-10
11  663e22e3e60ff32ccc0db406  FireBlocks_Bond       0.00    52006.96     0.0        0.00       0.00    52006.96         NaN  12-00  2024-05-10
12  663e22e3e60ff32ccc0db407  FireBlocks_Cold       0.00     1028.23     0.0        0.00       0.00     1028.23         NaN  12-00  2024-05-10
13  663e22e3e60ff32ccc0db408             Gate  156359.35        0.00     0.0        0.00       0.00   156359.35         NaN  12-00  2024-05-10
14  663e22e3e60ff32ccc0db409              HRP       0.00     7786.21     0.0        0.00       0.00     7786.21         NaN  12-00  2024-05-10
15  663e22e3e60ff32ccc0db40a           Hercle  720195.19        0.00     0.0        0.00       0.00   720195.19         NaN  12-00  2024-05-10
16  663e22e3e60ff32ccc0db40b            Huobi       0.00        0.00     0.0        0.00       0.00        0.00         NaN  12-00  2024-05-10
17  663e22e3e60ff32ccc0db40c           Kraken       0.00        0.00     0.0  1678090.88       0.00  1678090.88         NaN  12-00  2024-05-10
```
