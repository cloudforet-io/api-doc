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
| [**create**](./Alert#create) | [AlertCreateRequest](Alert#alertcreaterequest) | [ServiceInfo](Alert#serviceinfo) |
| [**update**](./Alert#update) | [AlertUpdateRequest](Alert#alertupdaterequest) | [ServiceInfo](Alert#serviceinfo) |
| [**delete**](./Alert#delete) | [AlertRequest](Alert#alertrequest) | [Empty](Alert#empty) |
| [**get**](./Alert#get) | [AlertRequest](Alert#alertrequest) | [ServiceInfo](Alert#serviceinfo) |
| [**list**](./Alert#list) | [AlertSearchQuery](Alert#alertsearchquery) | [ServicesInfo](Alert#servicesinfo) |
| [**history**](./Alert#history) | [AlertChangeMemberRequest](Alert#alertchangememberrequest) | [ServiceInfo](Alert#serviceinfo) |
| [**analyze**](./Alert#analyze) | [AlertChangeMemberRequest](Alert#alertchangememberrequest) | [ServiceInfo](Alert#serviceinfo) |
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





> **POST** /alert_manager/v1/alert/stat
>






    


<br>
<br>

## Message



### AlertChangeMemberRequest
* **service_id** (string)   `Required` 

    
* **members** (Members)   `Required` 

    <br>

### AlertCreateRequest
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)  

    
* **members** (Struct)  

    
* **options** (Options)  

    <br>

### AlertInfo
* **high** (int32)   `Required` 

    
* **low** (int32)   `Required` 

    <br>

### AlertRequest
* **service_id** (string)   `Required` 

    <br>

### AlertSearchQuery
* **query** (Query)  

    
* **service_id** (string)  

    
* **escalation_policy_id** (string)  

    
* **include_details** (bool)  

    <br>

### AlertStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### AlertUpdateRequest
* **service_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **options** (Options)  

    <br>

### Alerts
* **TOTAL** (AlertInfo)   `Required` 

    
* **TRIGGERRED** (AlertInfo)   `Required` 

    
* **ACKNOWLEDGED** (AlertInfo)   `Required` 

    <br>

### Channels
* **service_channel_info** (ServiceChannelsInfo)  `Repeated`    `Required` 

    <br>

### Members
* **USER** (string)  `Repeated`    `Required` 

    
* **USER_GROUP** (string)  `Repeated`    `Required` 

    <br>

### Options<br>

### ServiceChannelsInfo
* **channel_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (string)   `Required` 

    
* **channel_type** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **schedule** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **protocol_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ServiceInfo
* **service_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **members** (Struct)   `Required` 

    
* **options** (Options)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **channels** (Struct)  

    
* **webhooks** (Struct)  

    
* **alerts** (Struct)  

    <br>

### ServicesInfo
* **results** (ServiceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WebhookInfo
* **webhook_id** (string)   `Required` 

    <br>

### Webhooks
* **webhook_info** (WebhookInfo)  `Repeated`    `Required` 

    <br>
