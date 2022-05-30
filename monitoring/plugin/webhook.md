---
description:  
---
# Webhook

>  **Package : spaceone.api.monitoring.plugin**

## Webhook

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](webhook.md#init)|   [WebhookInitRequest](webhook.md#webhookinitrequest) |   [WebhookPluginInfo](webhook.md#webhookplugininfo) |
| [**verify**](webhook.md#verify)|   [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init


| Type | Message |
| :--- | :--- |
| Request | [WebhookInitRequest](webhook.md#webhookinitrequest) |
| Response |  [WebhookPluginInfo](webhook.md#webhookplugininfo)  |
 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### WebhookInitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### WebhookPluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### WebhookPluginVerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
