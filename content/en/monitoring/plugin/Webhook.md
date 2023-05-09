---
title: "Webhook"
linkTitle: "Webhook"
weight: 3
bookFlatSection: true
---
# [Webhook](#Webhook)
desc: A Webhook is a plugin receiving data from external monitoring systems.


>  **Package : spaceone.api.monitoring.plugin**

<br>
<br>

## Webhook





**Webhook Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Webhook#init) | [WebhookInitRequest](Webhook#webhookinitrequest) | [WebhookPluginInfo](./Webhook#webhookplugininfo) |
| [**verify**](./Webhook#verify) | [WebhookPluginVerifyRequest](Webhook#webhookpluginverifyrequest) | [Empty](./Webhook#empty) |



    
<br>

### init

desc: Verifies a specific Webhook. You must specify the parameter `secret_data`, encrypted account data of the Webhook to validate.








    
<br>

### verify

desc: Initializes a specific Webhook. During initialization, the Webhook information to be passed to the Webhook user is delivered as `metadata`. Webhook information includes its name and version.








    


<br>
<br>

## Message



### WebhookInitRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    <br>

### WebhookPluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### WebhookPluginVerifyRequest
* **options** (Struct)  `Required` 

  *is_required: true*

    <br>
