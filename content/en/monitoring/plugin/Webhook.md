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




 {{< tabs " init " >}}




{{< /tabs >}}

    
<br>

### verify




 {{< tabs " verify " >}}




{{< /tabs >}}

    


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
