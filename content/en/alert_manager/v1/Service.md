---
title: "Service"
linkTitle: "Service"
weight: 3
bookFlatSection: true
---
# [Service](#Service)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Service





**Service Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Service#create) | [ServiceCreateRequest](Service#servicecreaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**update**](./Service#update) | [ServiceUpdateRequest](Service#serviceupdaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**change_members**](./Service#change_members) | [ServiceChangeMembersRequest](Service#servicechangemembersrequest) | [ServiceInfo](Service#serviceinfo) |
| [**delete**](./Service#delete) | [ServiceDeleteRequest](Service#servicedeleterequest) | [Empty](Service#empty) |
| [**get**](./Service#get) | [ServiceGetRequest](Service#servicegetrequest) | [ServiceInfo](Service#serviceinfo) |
| [**list**](./Service#list) | [ServiceSearchQuery](Service#servicesearchquery) | [ServicesInfo](Service#servicesinfo) |
| [**stat**](./Service#stat) | [ServiceStatQuery](Service#servicestatquery) | [Struct](Service#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/service/create
>






    
<br>

### update





> **POST** /alert-manager/v1/service/update
>






    
<br>

### change_members





> **POST** /alert-manager/v1/service/change-members
>






    
<br>

### delete





> **POST** /alert-manager/v1/service/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/service/get
>






    
<br>

### list





> **POST** /alert-manager/v1/service/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/service/stat
>






    


<br>
<br>

## Message



### AlertStats
* **HIGH** (int32)   `Required` 

    
* **LOW** (int32)   `Required` 

    <br>

### Alerts
* **TOTAL** (AlertStats)   `Required` 

    
* **TRIGGERED** (AlertStats)   `Required` 

    
* **ACKNOWLEDGED** (AlertStats)   `Required` 

    
* **RESOLVED** (AlertStats)   `Required` 

    <br>

### ServiceChangeMembersRequest
* **service_id** (string)   `Required` 

    
* **members** (ServiceMembers)   `Required` 

    <br>

### ServiceCreateRequest
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)  

    
* **members** (ServiceMembers)  

    
* **options** (ServiceOptions)  

    
* **tags** (Struct)  

    <br>

### ServiceDeleteRequest
* **service_id** (string)   `Required` 

    
* **force** (bool)  

    <br>

### ServiceGetRequest
* **service_id** (string)   `Required` 

    
* **details** (bool)  

    <br>

### ServiceInfo
* **service_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **members** (ServiceMembers)   `Required` 

    
* **options** (ServiceOptions)   `Required` 

    
* **channels** (string)  `Repeated`    `Required` 

    
* **webhooks** (string)  `Repeated`    `Required` 

    
* **alerts** (Alerts)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### ServiceMembers
* **USER** (string)  `Repeated`    `Required` 

    
* **USER_GROUP** (string)  `Repeated`    `Required` 

    <br>

### ServiceOptions
* **notification_urgency** (NotificationUrgency)   `Required` 

    
* **recovery_mode** (RecoveryMode)   `Required` 

    <br>

### ServiceSearchQuery
* **query** (Query)  

    
* **service_id** (string)  

    
* **name** (string)  

    
* **details** (bool)  

    
* **escalation_policy_id** (string)  

    <br>

### ServiceStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ServiceUpdateRequest
* **service_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **options** (ServiceOptions)  

    
* **tags** (Struct)  

    
* **escalation_policy_id** (string)  

    <br>

### ServicesInfo
* **results** (ServiceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
