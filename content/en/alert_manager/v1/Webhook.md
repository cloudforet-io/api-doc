---
title: "Webhook"
linkTitle: "Webhook"
weight: 3
bookFlatSection: true
---
# [Webhook](#Webhook)



>  **Package : spaceone.api.alert_manager.v1**

<br>
<br>

## Webhook





**Webhook Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Webhook#create) | [WebhookCreateRequest](Webhook#webhookcreaterequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**update**](./Webhook#update) | [WebhookUpdateRequest](Webhook#webhookupdaterequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**update_plugin**](./Webhook#update_plugin) | [WebhookUpdatePluginRequest](Webhook#webhookupdatepluginrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**verify_plugin**](./Webhook#verify_plugin) | [WebhookRequest](Webhook#webhookrequest) | [Empty](Webhook#empty) |
| [**enable**](./Webhook#enable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**disable**](./Webhook#disable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**delete**](./Webhook#delete) | [WebhookRequest](Webhook#webhookrequest) | [Empty](Webhook#empty) |
| [**get**](./Webhook#get) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**list**](./Webhook#list) | [WebhookSearchQuery](Webhook#webhooksearchquery) | [WebhooksInfo](Webhook#webhooksinfo) |
| [**stat**](./Webhook#stat) | [WebhookStatQuery](Webhook#webhookstatquery) | [Struct](Webhook#struct) |



    
<br>

### create





> **POST** /monitoring/v1/webhook/create
>






    
<br>

### update





> **POST** /monitoring/v1/webhook/update
>






    
<br>

### update_plugin





> **POST** /monitoring/v1/webhook/update-plugin
>






    
<br>

### verify_plugin





> **POST** /monitoring/v1/webhook/verify-plugin
>






    
<br>

### enable





> **POST** /monitoring/v1/webhook/enable
>






    
<br>

### disable





> **POST** /monitoring/v1/webhook/disable
>






    
<br>

### delete





> **POST** /monitoring/v1/webhook/delete
>






    
<br>

### get





> **POST** /monitoring/v1/webhook/get
>






    
<br>

### list





> **POST** /monitoring/v1/webhook/list
>






    
<br>

### stat





> **POST** /monitoring/v1/webhook/stat
>






    


<br>
<br>

## Message



### WebhookCreateRequest
* **name** (string)   `Required` 

    
* **plugin_info** (WebhookPluginInfo)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### WebhookInfo
* **webhook_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (WebhookState)   `Required` 

    
* **access_key** (string)   `Required` 

    
* **webhook_url** (string)   `Required` 

    
* **plugin_info** (WebhookPluginInfo)   `Required` 

    
* **requests** (WebhookRequests)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### WebhookPluginInfo
* **plugin_id** (string)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (WebhookUpgradeMode)  

    <br>

### WebhookRequest
* **webhook_id** (string)   `Required` 

    <br>

### WebhookRequests
* **total** (int64)   `Required` 

    
* **error** (int64)   `Required` 

    <br>

### WebhookSearchQuery
* **query** (Query)  

    
* **webhook_id** (string)  

    
* **name** (string)  

    
* **state** (WebhookState)  

    
* **access_key** (string)  

    
* **workspace_id** (string)  

    
* **service_id** (string)  

    <br>

### WebhookStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### WebhookUpdatePluginRequest
* **webhook_id** (string)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (WebhookUpgradeMode)  

    <br>

### WebhookUpdateRequest
* **webhook_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>

### WebhooksInfo
* **results** (WebhookInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
