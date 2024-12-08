---
title: "NotificationProtocol"
linkTitle: "NotificationProtocol"
weight: 3
bookFlatSection: true
---
# [NotificationProtocol](#NotificationProtocol)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## NotificationProtocol





**NotificationProtocol Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./NotificationProtocol#create) | [NotificationProtocolCreateRequest](NotificationProtocol#notificationprotocolcreaterequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**update**](./NotificationProtocol#update) | [NotificationProtocolUpdateRequest](NotificationProtocol#notificationprotocolupdaterequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**update_plugin**](./NotificationProtocol#update_plugin) | [NotificationProtocolUpdatePluginRequest](NotificationProtocol#notificationprotocolupdatepluginrequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**enable**](./NotificationProtocol#enable) | [NotificationProtocolRequest](NotificationProtocol#notificationprotocolrequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**disable**](./NotificationProtocol#disable) | [NotificationProtocolRequest](NotificationProtocol#notificationprotocolrequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**delete**](./NotificationProtocol#delete) | [NotificationProtocolRequest](NotificationProtocol#notificationprotocolrequest) | [Empty](NotificationProtocol#empty) |
| [**get**](./NotificationProtocol#get) | [NotificationProtocolRequest](NotificationProtocol#notificationprotocolrequest) | [NotificationProtocolInfo](NotificationProtocol#notificationprotocolinfo) |
| [**list**](./NotificationProtocol#list) | [NotificationProtocolSearchQuery](NotificationProtocol#notificationprotocolsearchquery) | [NotificationProtocolsInfo](NotificationProtocol#notificationprotocolsinfo) |
| [**stat**](./NotificationProtocol#stat) | [NotificationProtocolStatQuery](NotificationProtocol#notificationprotocolstatquery) | [Struct](NotificationProtocol#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/notification-protocol/create
>






    
<br>

### update





> **POST** /alert-manager/v1/notification-protocol/update
>






    
<br>

### update_plugin





> **POST** /alert-manager/v1/notification-protocol/update-plugin
>






    
<br>

### enable





> **POST** /alert-manager/v1/notification-protocol/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/notification-protocol/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/notification-protocol/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/notification-protocol/get
>






    
<br>

### list





> **POST** /alert-manager/v1/notification-protocol/list
>






    
<br>

### stat





> **POST** /alert_manager/v1/notification-protocol/stat
>






    


<br>
<br>

## Message



### NotificationProtocolCreateRequest
* **name** (string)   `Required` 

    
* **plugin_info** (NotificationProtocolRequestPluginInfo)   `Required` 

    
* **tags** (Struct)  

    <br>

### NotificationProtocolInfo
* **protocol_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (NotificationProtocolState)   `Required` 

    
* **plugin_info** (NotificationProtocolResponsePluginInfo)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### NotificationProtocolRequest
* **protocol_id** (string)   `Required` 

    <br>

### NotificationProtocolRequestPluginInfo
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **upgrade_mode** (NotificationProtocolUpgradeMode)   `Required` 

    
* **secret_data** (Struct)  

    
* **schema** (Struct)  

    <br>

### NotificationProtocolResponsePluginInfo
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **upgrade_mode** (NotificationProtocolUpgradeMode)   `Required` 

    
* **metadata** (Struct)  

    
* **secret_id** (string)  

    <br>

### NotificationProtocolSearchQuery
* **query** (Query)  

    
* **protocol_id** (string)  

    
* **name** (string)  

    
* **state** (NotificationProtocolState)  

    <br>

### NotificationProtocolStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### NotificationProtocolUpdatePluginRequest
* **protocol_id** (string)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    <br>

### NotificationProtocolUpdateRequest
* **protocol_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### NotificationProtocolsInfo
* **results** (NotificationProtocolInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>