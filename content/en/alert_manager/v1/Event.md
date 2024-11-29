---
title: "Event"
linkTitle: "Event"
weight: 3
bookFlatSection: true
---
# [Event](#Event)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Event





**Service Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Service#create) | [ServiceCreateRequest](Service#servicecreaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**update**](./Service#update) | [ServiceUpdateRequest](Service#serviceupdaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**change_member**](./Service#change_member) | [ServiceChangeMemberRequest](Service#servicechangememberrequest) | [ServiceInfo](Service#serviceinfo) |
| [**delete**](./Service#delete) | [ServiceRequest](Service#servicerequest) | [Empty](Service#empty) |
| [**get**](./Service#get) | [ServiceRequest](Service#servicerequest) | [ServiceInfo](Service#serviceinfo) |
| [**list**](./Service#list) | [ServiceSearchQuery](Service#servicesearchquery) | [ServicesInfo](Service#servicesinfo) |
| [**stat**](./Service#stat) | [ServiceStatQuery](Service#servicestatquery) | [Struct](Service#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/comment/create
>






    
<br>

### update





> **POST** /alert-manager/v1/comment/update
>






    
<br>

### change_member





> **POST** /alert-manager/v1/comment/change-member
>






    
<br>

### delete





> **POST** /alert-manager/v1/comment/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/comment/get
>






    
<br>

### list





> **POST** /alert-manager/v1/comment/list
>






    
<br>

### stat





> **POST** /alert_manager/v1/comment/stat
>






    


<br>
<br>

## Message



### AlertInfo
* **high** (int32)   `Required` 

    
* **low** (int32)   `Required` 

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

### ServiceChangeMemberRequest
* **service_id** (string)   `Required` 

    
* **members** (Members)   `Required` 

    <br>

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

### ServiceCreateRequest
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)  

    
* **members** (Struct)  

    
* **options** (Options)  

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

### ServiceRequest
* **service_id** (string)   `Required` 

    <br>

### ServiceSearchQuery
* **query** (Query)  

    
* **service_id** (string)  

    
* **escalation_policy_id** (string)  

    
* **include_details** (bool)  

    <br>

### ServiceStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ServiceUpdateRequest
* **service_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **options** (Options)  

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
