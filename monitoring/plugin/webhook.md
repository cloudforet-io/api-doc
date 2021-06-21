---
description:  
---
# Webhook

>  **Package : spaceone.api.monitoring.plugin**

## Webhook

{% hint style="info" %}
**Webhook Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**init**](webhook.md#init)|   [WebhookInitRequest](webhook.md#webhookinitrequest) |   [WebhookPluginInfo](webhook.md#webhookplugininfo) |  |
| 2 | [**verify**](webhook.md#verify)|   [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### WebhookPluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### WebhookPluginVerifyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
