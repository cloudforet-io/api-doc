---
title: "ServiceChannel"
linkTitle: "ServiceChannel"
weight: 3
bookFlatSection: true
---
# [ServiceChannel](#ServiceChannel)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## ServiceChannel





**ServiceChannel Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ServiceChannel#create) | [ServiceChannelCreateRequest](ServiceChannel#servicechannelcreaterequest) | [ServiceChannelInfo](ServiceChannel#servicechannelinfo) |
| [**create_forward_channel**](./ServiceChannel#create_forward_channel) | [ServiceChannelCreateForwardChannelRequest](ServiceChannel#servicechannelcreateforwardchannelrequest) | [Empty](ServiceChannel#empty) |
| [**update**](./ServiceChannel#update) | [ServiceChannelUpdateRequest](ServiceChannel#servicechannelupdaterequest) | [ServiceChannelInfo](ServiceChannel#servicechannelinfo) |
| [**enable**](./ServiceChannel#enable) | [ServiceChannelRequest](ServiceChannel#servicechannelrequest) | [ServiceChannelInfo](ServiceChannel#servicechannelinfo) |
| [**disable**](./ServiceChannel#disable) | [ServiceChannelRequest](ServiceChannel#servicechannelrequest) | [ServiceChannelInfo](ServiceChannel#servicechannelinfo) |
| [**delete**](./ServiceChannel#delete) | [ServiceChannelRequest](ServiceChannel#servicechannelrequest) | [Empty](ServiceChannel#empty) |
| [**get**](./ServiceChannel#get) | [ServiceChannelRequest](ServiceChannel#servicechannelrequest) | [ServiceChannelInfo](ServiceChannel#servicechannelinfo) |
| [**list**](./ServiceChannel#list) | [ServiceChannelSearchQuery](ServiceChannel#servicechannelsearchquery) | [ServiceChannelsInfo](ServiceChannel#servicechannelsinfo) |
| [**stat**](./ServiceChannel#stat) | [ServiceChannelStatQuery](ServiceChannel#servicechannelstatquery) | [Struct](ServiceChannel#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/service-channel/create
>






    
<br>

### create_forward_channel





> **POST** /alert-manager/v1/service-channel/create-forward-channel
>






    
<br>

### update





> **POST** /alert-manager/v1/service-channel/update
>






    
<br>

### enable





> **POST** /alert-manager/v1/service-channel/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/service-channel/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/service-channel/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/service-channel/get
>






    
<br>

### list





> **POST** /alert-manager/v1/service-channel/list
>






    
<br>

### stat





> **POST** /alert-manager/v1/service-channel/stat
>






    


<br>
<br>

## Message



### ChannelSchedule
* **SCHEDULE_TYPE** (ChannelScheduleType)   `Required` 

    
* **SUN** (ChannelScheduleInfo)   `Required` 

    
* **MON** (ChannelScheduleInfo)   `Required` 

    
* **TUE** (ChannelScheduleInfo)   `Required` 

    
* **WED** (ChannelScheduleInfo)   `Required` 

    
* **THU** (ChannelScheduleInfo)   `Required` 

    
* **FRI** (ChannelScheduleInfo)   `Required` 

    
* **SAT** (ChannelScheduleInfo)   `Required` 

    <br>

### ChannelScheduleInfo
* **is_scheduled** (bool)   `Required` 

    
* **start** (int32)   `Required` 

    
* **end** (int32)   `Required` 

    <br>

### ServiceChannelCreateForwardChannelRequest
* **name** (string)   `Required` 

    
* **schedule** (ChannelSchedule)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    <br>

### ServiceChannelCreateRequest
* **protocol_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **schedule** (ChannelSchedule)  

    
* **tags** (Struct)  

    <br>

### ServiceChannelInfo
* **channel_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (ChannelState)   `Required` 

    
* **channel_type** (ServiceChannelType)   `Required` 

    
* **schedule** (ChannelSchedule)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **protocol_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### ServiceChannelRequest
* **channel_id** (string)   `Required` 

    <br>

### ServiceChannelSearchQuery
* **query** (Query)  

    
* **channel_id** (string)  

    
* **name** (string)  

    
* **state** (ChannelState)  

    
* **channel_type** (ServiceChannelType)  

    
* **workspace_id** (string)  

    
* **service_id** (string)  

    
* **protocol_id** (string)  

    <br>

### ServiceChannelStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ServiceChannelUpdateRequest
* **channel_id** (string)   `Required` 

    
* **name** (string)  

    
* **schedule** (ChannelSchedule)  

    
* **data** (Struct)  

    
* **tags** (Struct)  

    <br>

### ServiceChannelsInfo
* **results** (ServiceChannelInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
