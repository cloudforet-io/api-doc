---
description: A Webhook is a plugin receiving data from external monitoring systems.
---
# Webhook

>  **Package : spaceone.api.monitoring.plugin**

## Webhook

{% hint style="info" %}
**Webhook Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](webhook.md#init)|   [WebhookInitRequest](webhook.md#webhookinitrequest) |   [WebhookPluginInfo](webhook.md#webhookplugininfo) |
| [**verify**](webhook.md#verify)|   [WebhookPluginVerifyRequest](webhook.md#webhookpluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init

> Verifies a specific Webhook. You must specify the parameter `secret_data`, encrypted account data of the Webhook to validate.

| Type | Message |
| :--- | :--- |
| Request | [WebhookInitRequest](webhook.md#webhookinitrequest) |
| Response |  [WebhookPluginInfo](webhook.md#webhookplugininfo)  |
 
 

 
### verify

> Initializes a specific Webhook. During initialization, the Webhook information to be passed to the Webhook user is delivered as `metadata`. Webhook information includes its name and version.

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
