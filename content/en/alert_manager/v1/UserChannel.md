---
title: "UserChannel"
linkTitle: "UserChannel"
weight: 3
bookFlatSection: true
---
# [UserChannel](#UserChannel)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## UserChannel





**UserChannel Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserChannel#create) | [UserChannelCreateRequest](UserChannel#userchannelcreaterequest) | [UserChannelInfo](UserChannel#userchannelinfo) |
| [**update**](./UserChannel#update) | [UserChannelUpdateRequest](UserChannel#userchannelupdaterequest) | [UserChannelInfo](UserChannel#userchannelinfo) |
| [**enable**](./UserChannel#enable) | [UserChannelRequest](UserChannel#userchannelrequest) | [UserChannelInfo](UserChannel#userchannelinfo) |
| [**disable**](./UserChannel#disable) | [UserChannelRequest](UserChannel#userchannelrequest) | [UserChannelInfo](UserChannel#userchannelinfo) |
| [**delete**](./UserChannel#delete) | [UserChannelRequest](UserChannel#userchannelrequest) | [Empty](UserChannel#empty) |
| [**get**](./UserChannel#get) | [UserChannelRequest](UserChannel#userchannelrequest) | [UserChannelInfo](UserChannel#userchannelinfo) |
| [**list**](./UserChannel#list) | [UserChannelSearchQuery](UserChannel#userchannelsearchquery) | [UserChannelsInfo](UserChannel#userchannelsinfo) |
| [**stat**](./UserChannel#stat) | [UserChannelStatQuery](UserChannel#userchannelstatquery) | [Struct](UserChannel#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/user-group/create
>






    
<br>

### update





> **POST** /alert-manager/v1/user-group/update
>






    
<br>

### enable





> **POST** /alert-manager/v1/user-group/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/user-group/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/user-group/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/user-group/get
>






    
<br>

### list





> **POST** /alert-manager/v1/user-group/list
>






    
<br>

### stat





> **POST** /alert_manager/v1/user-group/stat
>






    


<br>
<br>

## Message



### UserChannelCreateRequest
* **protocol_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **schedule** (ChannelSchedule)  

    
* **tags** (Struct)  

    <br>

### UserChannelInfo
* **channel_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (UserChannelState)   `Required` 

    
* **schedule** (ChannelSchedule)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **protocol_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **user_secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UserChannelRequest
* **channel_id** (string)   `Required` 

    <br>

### UserChannelSearchQuery
* **query** (Query)  

    
* **channel_id** (string)  

    
* **name** (string)  

    
* **state** (UserChannelState)  

    
* **protocol_id** (string)  

    <br>

### UserChannelStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UserChannelUpdateRequest
* **channel_id** (string)   `Required` 

    
* **name** (string)  

    
* **schedule** (ChannelSchedule)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    <br>

### UserChannelsInfo
* **results** (UserChannelInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
