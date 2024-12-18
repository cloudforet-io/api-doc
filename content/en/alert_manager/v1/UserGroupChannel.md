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





**UserGroupChannel Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserGroupChannel#create) | [UserGroupChannelCreateRequest](UserGroupChannel#usergroupchannelcreaterequest) | [UserGroupChannelInfo](UserGroupChannel#usergroupchannelinfo) |
| [**update**](./UserGroupChannel#update) | [UserGroupChannelUpdateRequest](UserGroupChannel#usergroupchannelupdaterequest) | [UserGroupChannelInfo](UserGroupChannel#usergroupchannelinfo) |
| [**enable**](./UserGroupChannel#enable) | [UserGroupChannelRequest](UserGroupChannel#usergroupchannelrequest) | [UserGroupChannelInfo](UserGroupChannel#usergroupchannelinfo) |
| [**disable**](./UserGroupChannel#disable) | [UserGroupChannelRequest](UserGroupChannel#usergroupchannelrequest) | [UserGroupChannelInfo](UserGroupChannel#usergroupchannelinfo) |
| [**delete**](./UserGroupChannel#delete) | [UserGroupChannelRequest](UserGroupChannel#usergroupchannelrequest) | [Empty](UserGroupChannel#empty) |
| [**get**](./UserGroupChannel#get) | [UserGroupChannelRequest](UserGroupChannel#usergroupchannelrequest) | [UserGroupChannelInfo](UserGroupChannel#usergroupchannelinfo) |
| [**list**](./UserGroupChannel#list) | [UserGroupChannelSearchQuery](UserGroupChannel#usergroupchannelsearchquery) | [UserGroupChannelsInfo](UserGroupChannel#usergroupchannelsinfo) |
| [**stat**](./UserGroupChannel#stat) | [UserGroupChannelStatQuery](UserGroupChannel#usergroupchannelstatquery) | [Struct](UserGroupChannel#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/user-group-channel/create
>






    
<br>

### update





> **POST** /alert-manager/v1/user-group-channel/update
>






    
<br>

### enable





> **POST** /alert-manager/v1/user-group-channel/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/user-group-channel/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/user-group-channel/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/user-group-channel/get
>






    
<br>

### list





> **POST** /alert-manager/v1/user-group-channel/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/user-group-channel/stat
>






    


<br>
<br>

## Message



### UserGroupChannelCreateRequest
* **protocol_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **user_group_id** (string)   `Required` 

    
* **schedule** (ChannelSchedule)  

    
* **tags** (Struct)  

    <br>

### UserGroupChannelInfo
* **channel_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (UserGroupChannelState)   `Required` 

    
* **schedule** (ChannelSchedule)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_group_id** (string)   `Required` 

    
* **protocol_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### UserGroupChannelRequest
* **channel_id** (string)   `Required` 

    <br>

### UserGroupChannelSearchQuery
* **query** (Query)  

    
* **channel_id** (string)  

    
* **name** (string)  

    
* **state** (UserGroupChannelState)  

    
* **workspace_id** (string)  

    
* **user_group_id** (string)  

    
* **protocol_id** (string)  

    <br>

### UserGroupChannelStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### UserGroupChannelUpdateRequest
* **channel_id** (string)   `Required` 

    
* **name** (string)  

    
* **schedule** (ChannelSchedule)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    <br>

### UserGroupChannelsInfo
* **results** (UserGroupChannelInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
