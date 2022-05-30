---
description:  
---
# Webhook

>  **Package : spaceone.api.monitoring.plugin**

## Webhook

{% hint style="info" %}
**Webhook Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**init**](webhook.md#init)|   [WebhookInitRequest](webhook.md#webhookinitrequest) |   [WebhookPluginInfo](webhook.md#webhookplugininfo) |  |
| [**verify**](webhook.md#verify)|   [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**init**](webhook.md#init) </div> | <div style="width:200px; text-align:center;">    [WebhookInitRequest](webhook.md#webhookinitrequest)  </div> | <div style="width:200px; text-align:center;">   [WebhookPluginInfo](webhook.md#webhookplugininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**verify**](webhook.md#verify) </div> | <div style="width:200px; text-align:center;">    [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### WebhookPluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### WebhookPluginVerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
