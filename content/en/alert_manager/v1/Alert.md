---
title: "Alert"
linkTitle: "Alert"
weight: 3
bookFlatSection: true
---
# [Alert](#Alert)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Alert





**Alert Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Alert#create) | [AlertCreateRequest](Alert#alertcreaterequest) | [AlertInfo](Alert#alertinfo) |
| [**update**](./Alert#update) | [AlertUpdateRequest](Alert#alertupdaterequest) | [AlertInfo](Alert#alertinfo) |
| [**delete**](./Alert#delete) | [AlertRequest](Alert#alertrequest) | [Empty](Alert#empty) |
| [**get**](./Alert#get) | [AlertRequest](Alert#alertrequest) | [AlertInfo](Alert#alertinfo) |
| [**list**](./Alert#list) | [AlertSearchQuery](Alert#alertsearchquery) | [AlertsInfo](Alert#alertsinfo) |
| [**history**](./Alert#history) | [AlertHistoryRequest](Alert#alerthistoryrequest) | [AlertHistoryInfo](Alert#alerthistoryinfo) |
| [**analyze**](./Alert#analyze) | [AlertAnalyzeQuery](Alert#alertanalyzequery) | [Struct](Alert#struct) |
| [**stat**](./Alert#stat) | [AlertStatQuery](Alert#alertstatquery) | [Struct](Alert#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/alert/create
>






    
<br>

### update





> **POST** /alert-manager/v1/alert/update
>






    
<br>

### delete





> **POST** /alert-manager/v1/alert/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/alert/get
>






    
<br>

### list





> **POST** /alert-manager/v1/alert/list
>






    
<br>

### history





> **POST** /alert-manager/v1/alert/history
>






    
<br>

### analyze





> **POST** /alert-manager/v1/alert/analyze
>






    
<br>

### stat





> **POST** /alert-manager/v1/alert/stat
>






    


<br>
<br>

## Message



### AlertAnalyzeQuery
* **query** (AnalyzeQuery)   `Required` 

    <br>

### AlertCreateRequest
* **title** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **description** (string)  

    
* **urgency** (AlertUrgency)  

    
* **severity** (EventSeverity)  

    
* **rule** (string)  

    
* **image_url** (string)  

    
* **resources** (AlertResource)  `Repeated`   

    
* **additional_info** (Struct)  

    <br>

### AlertEventInfo
* **alert_id** (string)   `Required` 

    
* **action** (AlertAction)   `Required` 

    
* **description** (string)   `Required` 

    
* **event_info** (EventInfo)   `Required` 

    
* **notification_info** (NotificationInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **created_by** (string)   `Required` 

    <br>

### AlertHistoryInfo
* **results** (AlertEventInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### AlertHistoryRequest
* **alert_id** (string)   `Required` 

    
* **action** (AlertAction)  

    
* **include_details** (bool)  

    
* **sort** (Sort)  `Repeated`   

    <br>

### AlertInfo
* **alert_id** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **status** (AlertStatus)   `Required` 

    
* **description** (string)   `Required` 

    
* **urgency** (AlertUrgency)   `Required` 

    
* **severity** (EventSeverity)   `Required` 

    
* **rule** (string)   `Required` 

    
* **image_url** (string)   `Required` 

    
* **resources** (AlertResource)  `Repeated`    `Required` 

    
* **triggered_type** (TriggeredType)   `Required` 

    
* **triggered_by** (string)   `Required` 

    
* **acknowledged_by** (string)   `Required` 

    
* **resolved_by** (string)   `Required` 

    
* **additional_info** (Struct)   `Required` 

    
* **labels** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **acknowledged_at** (string)   `Required` 

    
* **resolved_at** (string)   `Required` 

    
* **acknowledged_duration** (int64)   `Required` 

    
* **resolved_duration** (int64)   `Required` 

    <br>

### AlertRequest
* **alert_id** (string)   `Required` 

    <br>

### AlertResource
* **name** (string)   `Required` 

    
* **asset_id** (string)  

    
* **asset_type** (string)  

    <br>

### AlertSearchQuery
* **query** (Query)  

    
* **alert_id** (string)  

    
* **status** (AlertStatus)  

    
* **urgency** (AlertUrgency)  

    
* **severity** (EventSeverity)  

    
* **resource** (string)  

    
* **triggered_type** (string)  

    
* **triggered_by** (string)  

    
* **workspace_id** (string)  

    
* **service_id** (string)  

    
* **webhook_id** (string)  

    
* **escalation_policy_id** (string)  

    
* **asset_id** (string)  

    <br>

### AlertStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### AlertUpdateRequest
* **alert_id** (string)   `Required` 

    
* **title** (string)  

    
* **status** (AlertStatus)  

    
* **description** (string)  

    
* **urgency** (AlertUrgency)  

    <br>

### AlertsInfo
* **results** (AlertInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
