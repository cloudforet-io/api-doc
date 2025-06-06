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





> **POST** /alert-manager/v1/user-channel/create
>






    
<br>

### update





> **POST** /alert-manager/v1/user-channel/update
>






    
<br>

### enable





> **POST** /alert-manager/v1/user-channel/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/user-channel/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/user-channel/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/user-channel/get
>






    
<br>

### list





> **POST** /alert-manager/v1/user-channel/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/user-channel/stat
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

    
* **plugin_id** (string)   `Required` 

    
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

    
* **plugin_id** (string)  

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
