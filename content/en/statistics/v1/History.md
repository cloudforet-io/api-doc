---
title: "History"
linkTitle: "History"
weight: 3
bookFlatSection: true
---
# [History](#History)
desc: A History is a record of data collection based on a Schedule.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## History





**History Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./History#create) | [CreateHistoryRequest](History#createhistoryrequest) | [Empty](./History#empty) |
| [**list**](./History#list) | [QueryHistoryRequest](History#queryhistoryrequest) | [HistoryInfo](./History#historyinfo) |
| [**stat**](./History#stat) | [HistoryStatRequest](History#historystatrequest) | [Struct](./History#struct) |



    
<br>

### create

desc: Creates a new History. Gets a Schedule as an input and creates a History as an output. You can use this method to manually run a specific Schedule.
request_example: >-
{
"schedule_id": "sch-b1d8be347bed",
"domain_id": "domain-58010aa2e451"
}



> **POST** /statistics/v1/history/create
>






    
<br>

### list

desc: Gets a list of all Histories. You can use a query to get a filtered list of Histories.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"results": [
{
"topic": "daily_cloud_service_summary",
"values": {
"label": "Storage",
"project_id": "project-f7111a9aa0c6",
"provider": "azure",
"value": 32213303296.0,
"cloud_service_group": "Compute",
"cloud_service_type": "Disk"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-18T01:01:57.579Z"
},
{
"topic": "daily_cloud_service_summary",
"values": {
"cloud_service_type": "Bucket",
"cloud_service_group": "CloudStorage",
"label": "Storage",
"provider": "google_cloud",
"project_id": "project-4cd006b4993b",
"value": 401399880.0
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-18T01:01:57.579Z"
}
],
"total_count": 2
}



> **POST** /statistics/v1/history/list
>






    
<br>

### stat





> **POST** /statistics/v1/history/stat
>






    


<br>
<br>

## Message



### CreateHistoryRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### HistoryInfo
* **results** (HistoryValueInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### HistoryStatRequest
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### HistoryValueInfo
* **topic** (string)  `Required` 

    
* **values** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### QueryHistoryRequest
* **query** (Query)  `Required` 

  *is_required: false*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
