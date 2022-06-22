

## 啟動環境

```
source /Users/alberthuang/Desktop/WorkSpace/fastAPI/venv/bin/activate
```

## 目錄底下

```
uvicorn gain_miles.main:app --host 0.0.0.0 --port 8080 --reload
```

## 瀏覽器開啟
http://127.0.0.1:8080/docs#/

可以測試API

* 需先加入 ItemCategory 的資料
* 再依據格式 加入 item 的資料