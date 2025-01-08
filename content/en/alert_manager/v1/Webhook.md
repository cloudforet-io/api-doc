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
| [**update_message_format**](./Webhook#update_message_format) | [WebhookMessageFormatUpdateRequest](Webhook#webhookmessageformatupdaterequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**update_plugin**](./Webhook#update_plugin) | [WebhookUpdatePluginRequest](Webhook#webhookupdatepluginrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**enable**](./Webhook#enable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**disable**](./Webhook#disable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**delete**](./Webhook#delete) | [WebhookRequest](Webhook#webhookrequest) | [Empty](Webhook#empty) |
| [**get**](./Webhook#get) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](Webhook#webhookinfo) |
| [**list**](./Webhook#list) | [WebhookSearchQuery](Webhook#webhooksearchquery) | [WebhooksInfo](Webhook#webhooksinfo) |
| [**list_errors**](./Webhook#list_errors) | [WebhookErrorSearchQuery](Webhook#webhookerrorsearchquery) | [WebhookErrorsInfo](Webhook#webhookerrorsinfo) |
| [**stat**](./Webhook#stat) | [WebhookStatQuery](Webhook#webhookstatquery) | [Struct](Webhook#struct) |



    
<br>

### create





> **POST** /alert-manager/v1/webhook/create
>






    
<br>

### update





> **POST** /alert-manager/v1/webhook/update
>






    
<br>

### update_message_format





> **POST** /alert-manager/v1/webhook/update-message-format
>






    
<br>

### update_plugin





> **POST** /alert-manager/v1/webhook/update-plugin
>






    
<br>

### enable





> **POST** /alert-manager/v1/webhook/enable
>






    
<br>

### disable





> **POST** /alert-manager/v1/webhook/disable
>






    
<br>

### delete





> **POST** /alert-manager/v1/webhook/delete
>






    
<br>

### get





> **POST** /alert-manager/v1/webhook/get
>






    
<br>

### list





> **POST** /alert-manager/v1/webhook/list
>






    
<br>

### list_errors





> **POST** /alert-manager/v1/webhook/list-errors
>






    
<br>

### stat





> **POST** /alert-manager/v1/webhook/stat
>






    


<br>
<br>

## Message



### WebhookCreateRequest
* **name** (string)   `Required` 

    
* **plugin_info** (WebhookPluginInfo)   `Required` 

    
* **message_formats** (WebhookMessageFormat)  `Repeated`    `Required` 

    
* **service_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### WebhookErrorInfo
* **error_id** (string)   `Required` 

    
* **message** (string)   `Required` 

    
* **raw_data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **webhook_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### WebhookErrorSearchQuery
* **webhook_id** (string)   `Required` 

    
* **query** (Query)  

    
* **error_id** (string)  

    <br>

### WebhookErrorsInfo
* **results** (WebhookErrorInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### WebhookInfo
* **webhook_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (WebhookState)   `Required` 

    
* **access_key** (string)   `Required` 

    
* **webhook_url** (string)   `Required` 

    
* **plugin_info** (WebhookPluginInfo)   `Required` 

    
* **requests** (WebhookRequests)   `Required` 

    
* **message_formats** (WebhookMessageFormat)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **service_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### WebhookMessageFormat
* **from** (string)   `Required` 

    
* **to** (string)   `Required` 

    <br>

### WebhookMessageFormatUpdateRequest
* **webhook_id** (string)   `Required` 

    
* **message_formats** (WebhookMessageFormat)  `Repeated`    `Required` 

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
