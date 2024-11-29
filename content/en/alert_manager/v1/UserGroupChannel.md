---
title: "UserGroupChannel"
linkTitle: "UserGroupChannel"
weight: 3
bookFlatSection: true
---
# [UserGroupChannel](#UserGroupChannel)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## UserGroupChannel





**Service Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Service#create) | [CommentCreateRequest](Service#commentcreaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**update**](./Service#update) | [CommentUpdateRequest](Service#commentupdaterequest) | [ServiceInfo](Service#serviceinfo) |
| [**change_member**](./Service#change_member) | [CommentChangeMemberRequest](Service#commentchangememberrequest) | [ServiceInfo](Service#serviceinfo) |
| [**delete**](./Service#delete) | [CommentRequest](Service#commentrequest) | [Empty](Service#empty) |
| [**get**](./Service#get) | [CommentRequest](Service#commentrequest) | [ServiceInfo](Service#serviceinfo) |
| [**list**](./Service#list) | [CommentSearchQuery](Service#commentsearchquery) | [ServicesInfo](Service#servicesinfo) |
| [**stat**](./Service#stat) | [CommentStatQuery](Service#commentstatquery) | [Struct](Service#struct) |



    
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

### CommentChangeMemberRequest
* **service_id** (string)   `Required` 

    
* **members** (Members)   `Required` 

    <br>

### CommentCreateRequest
* **name** (string)   `Required` 

    
* **service_key** (string)   `Required` 

    
* **description** (string)  

    
* **members** (Struct)  

    
* **options** (Options)  

    <br>

### CommentRequest
* **service_id** (string)   `Required` 

    <br>

### CommentSearchQuery
* **query** (Query)  

    
* **service_id** (string)  

    
* **escalation_policy_id** (string)  

    
* **include_details** (bool)  

    <br>

### CommentStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### CommentUpdateRequest
* **service_id** (string)   `Required` 

    
* **escalation_policy_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **options** (Options)  

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
