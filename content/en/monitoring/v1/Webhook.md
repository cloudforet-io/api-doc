---
title: "Webhook"
linkTitle: "Webhook"
weight: 3
bookFlatSection: true
---
# [Webhook](#Webhook)
desc: A Webhook is a plugin instance receiving data from external monitoring systems.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Webhook


**Webhook Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Webhook#create) | [CreateWebhookRequest](Webhook#createwebhookrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**update**](./Webhook#update) | [UpdateWebhookRequest](Webhook#updatewebhookrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**update_plugin**](./Webhook#update_plugin) | [UpdateWebhookPluginRequest](Webhook#updatewebhookpluginrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**verify_plugin**](./Webhook#verify_plugin) | [WebhookRequest](Webhook#webhookrequest) | [Empty](./Webhook#empty) |
| [**enable**](./Webhook#enable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**disable**](./Webhook#disable) | [WebhookRequest](Webhook#webhookrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**delete**](./Webhook#delete) | [WebhookRequest](Webhook#webhookrequest) | [Empty](./Webhook#empty) |
| [**get**](./Webhook#get) | [GetWebhookRequest](Webhook#getwebhookrequest) | [WebhookInfo](./Webhook#webhookinfo) |
| [**list**](./Webhook#list) | [WebhookQuery](Webhook#webhookquery) | [WebhooksInfo](./Webhook#webhooksinfo) |
| [**stat**](./Webhook#stat) | [WebhookStatQuery](Webhook#webhookstatquery) | [Struct](./Webhook#struct) |



    
<br>

### create

> **POST** /monitoring/v1/webhook/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/webhook/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### update_plugin

> **POST** /monitoring/v1/webhook/update-plugin
>




 {{< tabs " update_plugin " >}}




{{< /tabs >}}

    
<br>

### verify_plugin

> **POST** /monitoring/v1/webhook/verify-plugin
>




 {{< tabs " verify_plugin " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /monitoring/v1/webhook/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /monitoring/v1/webhook/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/webhook/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/webhook/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/webhook/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/webhook/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateWebhookRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **plugin_info** (WebhookPluginInfo)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetWebhookRequest
* **webhook_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateWebhookPluginRequest
* **webhook_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateWebhookRequest
* **webhook_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### WebhookInfo
* **webhook_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (WebhookState)  `Required` 

    
* **access_key** (string)  `Required` 

    
* **webhook_url** (string)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **plugin_info** (WebhookPluginInfo)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### WebhookPluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **upgrade_mode** (UpgradeMode)  `Required` 

    <br>

### WebhookQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **webhook_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (WebhookState)  `Required` 

  *is_required: false*

    
* **access_key** (string)  `Required` 

  *is_required: false*

    
* **webhook_url** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### WebhookRequest
* **webhook_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### WebhookStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### WebhooksInfo
* **results** (WebhookInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
